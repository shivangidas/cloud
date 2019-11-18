import hashlib
import datetime

from .sellerie import app
from celery.result import AsyncResult


@app.task
def goldenEgg(Nonce=0, data="COMSM0010cloud", difficulty=4, start=0, end=10000):
    # convert to binary
    # data = ' '.join(format(ord(x), 'b') for x in data)
    print(f"Run {start} {end}")
    prefix = "0" * difficulty
    prefLength = difficulty
    flag = 0
    hashValue = ""
    startTime = datetime.datetime.now()
    # while flag == 0:
    for i in range(start, end+1):
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
        print("Not found Nonce")
    else:
        print("prefix : ", prefix)
        print("Nonce : ", Nonce)
        print("Hash Value : ", hashValue)
        print("Time spent : ", timeSpent)
        print("\n")
        return Nonce
