import time
import hashlib
import sys
from .sellerie import app
from celery.task.control import revoke
from container_app.goldenNonce import goldenEgg

if __name__ == '__main__':
    data = "COMSM0010cloud"
    start_time = time.time()
    max_difficulty = 15
    difficulty = 4
    timeGivenByUser = 60 * 1
    numberOfTasksInParallel = 100
    total_nonce_options = 4294967296  # 2 ^ 32
    if len(sys.argv) > 1:
        if (int(sys.argv[1]) > max_difficulty):
            print("This is too much for my capacity. Exciting...\n")
            exit(0)
        difficulty = int(sys.argv[1])
        try:
            timeGivenByUser = sys.argv[2]
        except:
            print("Max time is 1 min")
        try:
            numberOfTasksInParallel = int(sys.argv[3])
        except:
            print("Using 100 tasks/VMs")
    else:
        print("python -m program difficulty time_in_seconds number_of_VMs_or_tasks")

    flag = 0
    loops = total_nonce_options // numberOfTasksInParallel
    for j in range(0, loops):
        tasks = []
        startNonce = j * numberOfTasksInParallel * 100
        for i in range(0, numberOfTasksInParallel):
            startNonceValue = startNonce + i * 100
            endNonceValue = startNonce + i*100 + 100
            tasks.append(goldenEgg.delay(
                startNonceValue, data, difficulty, endNonceValue))

        goldenNonce = 0
        tasks_backup = tasks

        while len(tasks) > 0:
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
        if flag == 0:
            print(
                f"Couldn't get Nonce below {startNonce + 10000} :( \n")
        else:
            #data = ' '.join(format(ord(x), 'b') for x in data)
            z = str(goldenNonce) + data
            hashValue = hashlib.sha256(z.encode()).hexdigest()
            print(f"Hash Value : {hashValue}")
            print("We got a Nonce: ", goldenNonce)
            break
        if ((time.time() - start_time) > int(timeGivenByUser)):
            print("Time exceeded")
            break
    elapsed_time = time.time() - start_time
    print(f"elapsed time: {elapsed_time}")
