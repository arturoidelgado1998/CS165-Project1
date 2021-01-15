from itertools import product

f = open("testpass.txt", "a")

for _set in product(list('abcdefghijklmnopqrstuvwxyz'), repeat = 6):
    w = ''.join(_set)
    f.write(w + "\n")

f.close()