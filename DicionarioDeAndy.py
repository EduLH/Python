import sys

def insertion (list):
    for index in range (1,len(list)):
        palavra = list[index]
        i = index -1
        while i >=0:
            if palavra < list[i]:
                list[i+1] = list[i]
                list[i] = palavra
                i = i-1
            else:
                break
words = []

for line in sys.stdin:
    for word in line.split():
        if word not in words:
            words.append(word.lower())
insertion(words)
for i in words:
    print(i)
