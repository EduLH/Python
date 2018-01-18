import collections

palavra1 = input()
palavra2 = input()

c = collections.Counter(palavra1)
d = collections.Counter(palavra2)

if c == d:
    print ('true')
else:
    print('false')
