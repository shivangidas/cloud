import time
import hashlib
import sys
from .sellerie import app
from celery.task.control import revoke
from container_app.goldenNonce import goldenEgg

if __name__ == '__main__':
    data = "COMSM0010cloud"
    data = ''.join(format(ord(x), 'b') for x in data)
    start_time = time.time()
    max_difficulty = 15
    difficulty = 4
    timeGivenByUser = 60 * 5
    numberOfTasksInParallel = 10
    total_nonce_options = 4294967296  # pow(2,32)
    hashes_per_task = 10000  # computer can make 280000 hashes/second
    print("python -m program difficulty time_in_seconds number_of_tasks")
    if len(sys.argv) > 1:
        if (int(sys.argv[1]) > max_difficulty):
            print(
                f"Diificulty {sys.argv[1]} is too much for my capacity. Exiting...\n")
            exit(0)
        difficulty = int(sys.argv[1])
        try:
            timeGivenByUser = sys.argv[2]
            print(f"Max time is {timeGivenByUser} sec\n")
        except:
            print(f"Max time is {timeGivenByUser} sec\n")
        try:
            numberOfTasksInParallel = int(sys.argv[3])
            print(f"Using {numberOfTasksInParallel} tasks\n")
        except:
            print(f"Using {numberOfTasksInParallel} tasks\n")
    flag = 0
    endNonceValue = 0
    round_no = 0
    while (endNonceValue < total_nonce_options):
        tasks = []
        startNonce = endNonceValue
        round_no += 1
        #print(f"Round {round_no} starting at : {startNonce}")
        for i in range(0, numberOfTasksInParallel):
            startNonceValue = startNonce + i * hashes_per_task
            endNonceValue = startNonce + i * hashes_per_task + hashes_per_task
            print(f"Task {i} starting at {startNonceValue}")
            tasks.append(goldenEgg.delay(
                startNonceValue, data, difficulty, endNonceValue))

        goldenNonce = 0
        tasks_backup = tasks
        print(f"Round {round_no} end at : {endNonceValue}")
        while len(tasks) > 0:
            completed_tasks = []
            for task in tasks:
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
                    # print(f"After revoke, the task {task.id} : {task.state}")
                tasks = []
            else:
                # remove completed tasks
                tasks = list(set(tasks) - set(completed_tasks))
        if flag == 0:
            print(
                f"Couldn't get Nonce below {endNonceValue} \n")
        else:
            # data = ' '.join(format(ord(x), 'b') for x in data)
            hashValue = hashlib.sha256(
                (str(goldenNonce) + data).encode()).hexdigest()
            print(f"Hash Value : {hashValue}")
            print(f"We got a Nonce: {goldenNonce} for difficulty {difficulty}")
            break
        if ((time.time() - start_time) > int(timeGivenByUser)):
            print("Time exceeded")
            break
    elapsed_time = time.time() - start_time
    print(f"elapsed time: {elapsed_time}")
