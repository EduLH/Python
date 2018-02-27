parenteses = input()
limit = 0
for i in parenteses:
    if limit >= 0:  #a media de parenteses devera sempre ser maior ou igual a zero
        if i == "(":
            limit = limit+1
        else:
            limit = limit-1
    else:       #caso nao seja, mais parenteses estao sendo fechados q o necessario
        print('false')  #ou houve 'fechamento' nesnecessario de parenteses
        break
if limit >=0:   
    print('true')
