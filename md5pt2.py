import hashlib
import multiprocessing
import time

# paswword: $1$4fTgjp6q$JgdO/UQGRxKX2ZfmBIjt40

def to64(v,n):
    base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ret = ""
    for i in range(0,n):
        ret += base64[v&0x3f]
        v>>=6
    return ret

def initilization(file):
        f = open(file)
        password = f.readline()
        count = 1

        while password:
            pass_bytes = bytes(password, 'utf-8')

            salt = '4fTgjp6q'
            salt_bytes = bytes(salt, 'utf-8')
            
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

            while i != 0:
                if i&1:
                    res2 += b'\x00'
                else:
                    res2 += password[0].encode()
                i >>= 1

            finalmd5 = hashlib.md5(res2)
            md5_res = finalmd5.digest()

            for j in range(0,1000):
                tmp = b''
                if (j %2) ==1: 
                    tmp += pass_bytes
                else: 
                    tmp += md5_res 
                if (j % 3) != 0: 
                    tmp += salt_bytes
                if (j % 7) != 0: 
                    tmp += pass_bytes
                if (j %2) == 1: 
                    tmp+=md5_res
                else: 
                    tmp += pass_bytes

                md5_res = hashlib.md5(tmp).digest()

            final_hex = (to64((md5_res[0] << 16) | (md5_res[6] << 8) | (md5_res[12]), 4) +\
            to64((md5_res[1] << 16) | (md5_res[7] << 8) | (md5_res[13]), 4) +\
            to64((md5_res[2] << 16) | (md5_res[8] << 8) | (md5_res[14]), 4) +\
            to64((md5_res[3] << 16) | (md5_res[9] << 8) | (md5_res[15]), 4) +\
            to64((md5_res[4] << 16) | (md5_res[10] << 8) | (md5_res[5]), 4) +\
            to64(md5_res[11], 2))
        #daaaad
            if final_hex == 'JgdO/UQGRxKX2ZfmBIjt40':
                print('{}: MATCH FOUND'.format(password))
                return

            print("{}. {}: No Match".format(count,password))
            password = f.readline()
            count += 1

#initilization("File A1.txt")   

if __name__ == '__main__':
    t0 = time.time()


    firstprocess = multiprocessing.Process(target= initilization, args=('File B1.txt', ))
    secondprocess = multiprocessing.Process(target= initilization, args=('File C1.txt', ))
    thirdprocess = multiprocessing.Process(target= initilization, args=('File D1.txt', ))
    fourthprocess = multiprocessing.Process(target= initilization, args=('File E1.txt', ))
    fifthprocess = multiprocessing.Process(target= initilization, args=('File F1.txt', ))
    sixthprocess = multiprocessing.Process(target= initilization, args=('File G1.txt', ))

    firstprocess.start()
    secondprocess.start()
    thirdprocess.start()
    fourthprocess.start()
    fifthprocess.start()
    sixthprocess.start()

    firstprocess.join()
    secondprocess.join()
    thirdprocess.join()
    fourthprocess.join()
    fifthprocess.join()
    sixthprocess.join()

    t1 = time.time()
    print (t1-t0)
