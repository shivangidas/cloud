import time
from celery.result import ResultBase
from container_app.goldenNonce import goldenEgg

if __name__ == '__main__':
    start_time = time.time()
    for i in range(100):
        result = goldenEgg.delay(i*1000, "COMSM0010cloud", "0000", i*1000, i*1000 + 1000)
        print (f'golden nonce {i}: ')
        print (result.children)

        
    #print(f'golden Nonce: {GN}')

    result_output = result.wait(timeout=None, interval=0.5)
    print(f'Last scheduled task result: {result_output}')
    elapsed_time = time.time() - start_time
    print(f"elapsed time: {elapsed_time}")
