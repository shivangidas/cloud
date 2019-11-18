import hashlib
import datetime

from .sellerie import app


@app.task
# def findNonce(start, end):
# for i in range(start, end):
#     prefix = "0" * i
#     GN, hashV, time = goldenEgg(Nonce, data, prefix)
#print (bin(Nonce))
def goldenEgg(Nonce=0, data="COMSM0010cloud", prefix="0000", start=0, end=10000):
    # convert to binary
    # data = ' '.join(format(ord(x), 'b') for x in data)
    prefLength = len(prefix)
    flag = 0
    hashValue = ""
    startTime = datetime.datetime.now()
    # while flag == 0:
    for i in range(start, end):
        z = str(Nonce) + data  # need prev hash and rest of the block
        hashValue = hashlib.sha256(z.encode()).hexdigest()
        if hashValue[:prefLength] == prefix:
            flag = 1
            break
        Nonce += 1
    endTime = datetime.datetime.now()
    timeSpent = endTime - startTime
    if (flag == 0):
        return 0
    else:
        print("prefix : ", prefix)
        print("Nonce : ", Nonce)
        print("Hash Value : ", hashValue)
        print("Time spent : ", timeSpent)
        print("\n")
        return Nonce
