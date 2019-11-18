import time
import hashlib
import sys
from .sellerie import app
from celery.task.control import revoke
from container_app.goldenNonce import goldenEgg

if __name__ == '__main__':
    data = "COMSM0010cloud"
    start_time = time.time()
    tasks = []
    max_difficulty = 15
    difficulty = 5
    total_nonce_options = 4294967296  # 2 ^ 32
    if len(sys.argv) > 1:
        if (int(sys.argv[1]) > max_difficulty):
            print("This is too much for my capacity. Exciting...\n")
            exit(0)
        difficulty = int(sys.argv[1])

    for i in range(0, 500):
        tasks.append(goldenEgg.delay(
            i*8000000, data, difficulty, i*8000000, i*8000000 + 8000000))
    #print(f'golden Nonce: {GN}')
    # print(tasks)
    # amass.delay([], tasks)
    flag = 0
    goldenNonce = 0
    i = 0
    tasks_backup = tasks
    if difficulty > 6:
        time.sleep(20)
    while len(tasks) > 0:
        if difficulty > 7:
            time.sleep(20)
        completed_tasks = []
        for task in tasks:
            #result = AsyncResult(id=task, app=app)
            if task.ready():
                completed_tasks.append(task)
                if task.get() != 0:
                    goldenNonce = task.get()
                    flag = 1
                    # https://stackoverflow.com/questions/7149074/deleting-all-pending-tasks-in-celery-rabbitmq
                    app.control.purge()
                    break
        if (flag == 1):
            # if one nonce is discovered remove all other tasks in queue
            # https://stackoverflow.com/questions/26512324/celery-abort-or-revoke-all-tasks-in-a-chord/26515646
            for task in tasks:
                revoke(task.id, terminate=True)
                #print(f"After revoke, the task {task.id} : {task.state}")
            tasks = []
        else:
            # remove completed tasks
            tasks = list(set(tasks) - set(completed_tasks))
        i = i+1
        print(f"Run : {i}")
    if flag == 0:
        print("Couldn't get Nonce in 4 billion options :( \n")
        # print("Try with more? [y/n]")
        # x = input()
    else:
        z = str(goldenNonce) + data
        hashValue = hashlib.sha256(z.encode()).hexdigest()
        print(f"Hash Value : {hashValue}")
        print("We got a Nonce: ", goldenNonce)
    elapsed_time = time.time() - start_time
    print(f"elapsed time: {elapsed_time}")
