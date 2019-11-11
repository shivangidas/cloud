import hashlib
import datetime

from .sellerie import app


@app.Nonce
# def findNonce(start, end):
    # for i in range(start, end):
    #     prefix = "0" * i
    #     GN, hashV, time = goldenEgg(Nonce, data, prefix)
#print (bin(Nonce))



def goldenEgg(Nonce = 0, data ="COMSM0010cloud", prefix= "0000", start=0, end=10000):
    #convert to binary
    # data = ' '.join(format(ord(x), 'b') for x in data)
    prefLength = len(prefix)
    flag = 0
    hashValue = ""
    start = datetime.datetime.now()
    #while flag == 0:
    for i in range(start, end):
        z = str(Nonce) + data #need prev hash and rest of the block
        hashValue = hashlib.sha256(z.encode()).hexdigest()
        if hashValue[:prefLength] == prefix:
            flag = 1
        Nonce += 1
    end = datetime.datetime.now()
    timeSpent = end - start
    if (flag = 0):
        return 0, 0, timeSpent
    else:
        print ("prefix : ", prefix)
        print ("Nonce : ", Nonce)
        print ("Hash Value : ", hashValue)
        print ("Time spent : ", timeSpent)
        print ("\n")
        return Nonce , hashValue, timeSpent
