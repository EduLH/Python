path = "/home/eduardo/Área de Trabalho/"
frats = open(path+"frats.txt", 'r')
dict_frats = {}
save = 0
for line in frats:
    for num in line.split():
        if "[[" in num:
            dict_frats[num] = []
            save = num
        else:
            dict_frats[save].append(num)

frats = open(path+"frats_iter.txt", 'r')
dict_iter = {}
save = 0
for line in frats:
    for num in line.split():
        if "[[" in num:
            dict_iter[num] = []
            save = num
        else:
            dict_iter[save].append(num)

gamb = 0
output = open(path+"frat_clean.txt", 'w')
for frat_i in dict_iter:
    if(frat_i != '[[58]]'):
        for inter in dict_iter[frat_i]:
            for frat in dict_frats:
                if (inter in dict_frats[frat]):
                    A = frat_i.replace("[","")
                    B = A.replace("]","")
                    C = frat.replace("[","")
                    D = C.replace("]","")
                    output.write(B + " "  + D + "\n")
                    gamb += 1
