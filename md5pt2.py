import hashlib


# paswword: $1$4fTgjp6q$JgdO/UQGRxKX2ZfmBIjt40


def to64(v,n):
    base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ret = ""
    for i in range(1,n+1):
        ret += base64[v&0x3f]
        v>>=6
    return ret

def initilization():

    password = "vnotpu"
    pass2 =password.encode()
    salt = "hfT7jp2q"

    res = password + "$1$" + salt
    res2 = res.encode()
    hash= password+ salt + password

    md5hashed = hashlib.md5(hash.encode())
    md5hashed2 = md5hashed.digest()

    lenpass = len(password)

    while lenpass > 0:
        res2 = res2 + md5hashed2[0:min(16,lenpass)]
        lenpass = lenpass - 16

    i = len(password)

    while i > 0:
        if i&1:
            res2 += b'\x00'
        else:
            res2 += password[0].encode()
        i >>= 1

    finalmd5 = hashlib.md5(res2)
    finalmd52 = finalmd5.digest()

    hash = b'\xed\x7a\x53\x07\x58\x8e\x49\xed\x3a\x27\x77\xd9\x26\xd6\x2f\x96'

    for j in range(0,1000):
        tmp = b''
        if (j %2) ==1:
            tmp += password.encode()
            finalmd53 = hashlib.md5(tmp).digest()
        else:
            tmp += finalmd52
            finalmd53 = hashlib.md5(tmp).digest()
        if j % 3 != 0:
            tmp += salt.encode()
            finalmd53 = hashlib.md5(tmp).digest()
        if j % 7 != 0:
            tmp += password.encode()
            finalmd53 = hashlib.md5(tmp).digest()
        if (j %2) == 1:
            tmp+=finalmd52
            finalmd53 = hashlib.md5(tmp).digest()
        else:
            tmp += password.encode()
            finalmd53 = hashlib.md5(tmp).digest()



    finalfinal = to64((finalmd53[0] << 16) | (finalmd53[6] << 8) | (finalmd53[12]), 4) +\
    to64((finalmd53[1] << 16) | (finalmd53[7] << 8) | (finalmd53[13]), 4) +\
    to64((finalmd53[2] << 16) | (finalmd53[8] << 8) | (finalmd53[14]), 4) +\
    to64((finalmd53[3] << 16) | (finalmd53[9] << 8) | (finalmd53[15]), 4) +\
    to64((finalmd53[4] << 16) | (finalmd53[10] << 8) | (finalmd53[5]), 4) +\
    to64(finalmd53[11], 2)

    print(finalfinal)


initilization()