s = 'pigbrauipbiaaaaaaaspisbgiasbgrisusbigsbusipabgspibrsiuabgaipsbsipgbsrigpgbsrigsb'
print(len(s))
letters = []
for letter in s:
    if(letter not in letters):
        letters.append(letter)
    cordMin = 0

letters

cordMax = len(s)-1
resMin = 0
resMax = len(s)-1
verif = True

while(cordMax-cordMin >= len(letters)):
    while(cordMax < len(s)):
        for letter in letters:
            if letter not in s[cordMin:cordMax]:
                verif = False
        if verif == True:
            resMin = cordMin
            resMax = cordMax
        verif = True
        cordMax = cordMax + 1
        cordMin = cordMin + 1
    cordMax = cordMax - cordMin -1
    cordMin = 0
print(resMax - resMin)
