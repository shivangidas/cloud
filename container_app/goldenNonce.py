import hashlib

from .sellerie import app


@app.task
def goldenEgg(Nonce=0, data="COMSM0010cloud", difficulty=4, end=10000):
    prefix = "0" * difficulty
    flag = 0
    while Nonce <= end:
        z = str(Nonce) + data
        hashValue = hashlib.sha256(z.encode()).hexdigest()
        if hashValue[:difficulty] == prefix:
            flag = 1
            break
        Nonce += 1
    if (flag == 0):
        return -1
    else:
        return Nonce
