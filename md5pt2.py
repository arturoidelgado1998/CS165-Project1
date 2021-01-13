import hashlib

# paswword: $1$4fTgjp6q$JgdO/UQGRxKX2ZfmBIjt40
def initilization():

    password = input("password?")
    salt = input("salt?")

    hash=  password + "1$1" + salt

    initilization1 = password

    md5hashed = hashlib.md5(hash.encode('UTF-8'))
    print(md5hashed.hexdigest())
    lenpass = len(password)

    while lenpass > 0:
        lenpass = lenpass +


initilization()