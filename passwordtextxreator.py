from itertools import product

f = open("firstpass.txt", "a")
g = open("secondpass.txt", "a")
i = open("thirdpass.txt", "a")
m = open("fourthpass.txt", "a")
h = 1
for _set in product(list('abcdefghijklmnopqrstuvwxyz'), repeat =6):
    w = ''.join(_set)
    if  h <= 77228944:
        f.write(w + "\n")
        h = h+1
    elif h >= 77228945 and h <= 154457888 :
        g.write(w + "\n")
        h = h+1
    elif h >= 154457889 and h <= 231686832:
        i.write(w + "\n")
        h = h+1
    else:
        m.write(w + "\n")

f.close()
g.close()
i.close()
m.close()