palavra1 = input('insira a palavra: ')
palavra1 = palavra1.replace(" ", "")
palavra2 = input('insira a palavra: ')
palavra2 = palavra2.replace(" ", "")
verif = None
if palavra1[::-1] == palavra2:
    verif = True
else:
    verif = False
print (verif)
