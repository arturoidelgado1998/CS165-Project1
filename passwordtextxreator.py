from itertools import product

f = open("testpass.txt", "a")
g = open("possiblepasswords.txt", "a")
i = open("finalpass.txt", "a")

h = 1
for _set in product(list('abcdef'), repeat =6):
    w = ''.join(_set)
    i.write(w+ "\n")
    if  h < 23329:
        f.write(w + "\n")
        h = h+1
    else:
        g.write(w + "\n")

f.close()
g.close()
i.close()