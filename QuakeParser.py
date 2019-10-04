import os
from itertools import islice


class Game:

    def __init__(self, game_slice, class_id):
        self.kills = 0
        self.get_players(game_slice)
        self.id = class_id
        self.make_fill_dict(self.players)

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
                print(line.split()[5])
                print(line.split()[7])
                if(line.split()[5] == '<world>'):
                    print(line)
                    player = self.get_player( get_name_victim(line) )
                    player.update_kills( get_name_kill(line) )
                else:
                    player = self.get_player( get_name_kill(line) )
                    player.update_kills( get_name_victim(line) )
                print("------------------")

    def get_name_kill(self, line):
        name = ''
        line_split = line.split()
        i = 5
        while(line_split[i] != 'killed'):
            name += line_split[i]
            i += 1
        return(name)

    def get_name_victim(self, line):
        name = ''
        i = 0
        line_split = line.split()
        while(line_split[i] != 'killed'):
            i += 1
        while(line_split[i] != 'by'):
            name += line_split[i]
            i += 1
        return(name)

    def make_fill_dict(self, players):
        players_kills = {}
        for player in players:
            players_kills[player] = 0

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

class Player:

    def __init__(self, line):
        self.name = self.get_name(line)
        self.kills = 0

    def get_name(self, line):
        return(line.split('\\')[1].split('\t')[0])

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




log = 'quake.log'
games = []
with open(log, 'r') as quake_log:
    ids = 0
    linStart = 0
    linEnd = 0
    readingLine = 0
    for line in quake_log:
        l_splt = line.split()
        if(len(l_splt) > 1):
            if(l_splt[1] == 'InitGame:'):
                linStart = readingLine

            if(l_splt[1] == 'ShutdownGame:' or l_splt[1] == '0:00'):
                linEnd = readingLine
                game = Game(islice(quake_log, linStart, linEnd), ids)
                games.append(game)
                ids += 1

        readingLine = readingLine + 1
