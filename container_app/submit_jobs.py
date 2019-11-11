import time

from container_app.goldenNonce import goldenEgg

if __name__ == '__main__':
    start_time = time.time()
    for i in range(100):
        GN, hashV, time = goldenEgg.delay(i*100, data, "0000", i*100, i*100 + 100)
        if GN == 0:
            break
    print("golden Nonce: {GN}\n Hash Value: {hashV}")

    #result_output = result.wait(timeout=None, interval=0.5)
    #print(f'Last scheduled task result: {result_output}')
    elapsed_time = time.time() - start_time
    print(f"elapsed time: {elapsed_time}")
