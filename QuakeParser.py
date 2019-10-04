import os
import operator
from itertools import islice


def get_name_kill(line):
    name = ''
    line_split = line.split()
    i = 5
    while(line_split[i] != 'killed'):
        name += line_split[i]
        i += 1
    return(name)

def get_name_victim(line):
    name = ''
    i = 0
    line_split = line.split()
    while(line_split[i] != 'killed'):
        i += 1
    i += 1
    while(line_split[i] != 'by'):
        name += line_split[i]
        i += 1
    return(name)

def get_game(id_game, games):
    for game in games:
        if game.id == id_game:
            return(game)

def dict_games(games):
    games_dicts = []
    score = []
    players_names = []
    for game in games:
        for player in game.players:
            players_names.append(player.name)
        for player in game.players:
            score.append(player.print_player())
        game_stats={'id':game.id,
                    'kills':game.kills,
                    'players':players_names,
                    'score':sorted(score, key = lambda x: x[1]) }
        score = []
        games_dicts.append(game_stats)
    return(games_dicts)



class Game:

    def __init__(self, game_slice, class_id):
        self.kills = 0
        self.get_players(game_slice)
        self.id = class_id

    def get_players(self, game_slice):
        self.players = []
        for line in game_slice:
            command = line.split()[1]
            if (command == 'ClientUserinfoChanged:'):
                player = Player(line)
                if(player not in self.players):
                    self.players.append(player)

            if(command == 'Kill:'):
                self.kills += 1
                if(line.split()[5] == '<world>'):
                    player = self.get_player( get_name_victim(line) )
                    player.update_kills( get_name_kill(line) )
                else:
                    player = self.get_player( get_name_kill(line) )
                    player.update_kills( get_name_victim(line) )

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player



class Player:

    def __init__(self, line):
        self.name = self.get_name(line)
        self.kills = 0

    def print_player(self):
        player = [self.name, self.kills]
        return(player)

    def get_name(self, line):
        return(line.split('\\')[1].split('\t')[0].replace(' ', ''))

    def update_kills(self, victim):
        if(victim == self.name):
            return
        if(victim == '<world>'):
            self.kills -= 1
        else:
            self.kills += 1

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def main_func():
    log = 'quake.log'
    games = []

    with open(log, 'r') as quake_log:
        ids = 0
        linStart = 0
        linEnd = 0
        game_line_buffer = []

        for line in quake_log:

            game_line_buffer.append(line)

            if(line.split()[1] == 'ShutdownGame:' or line.split()[1] == '0:00'):
                game = Game(game_line_buffer, ids)
                games.append(game)
                ids += 1
                game_line_buffer = []
    return(dict_games(games))
