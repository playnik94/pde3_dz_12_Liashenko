import concurrent.futures
import time

Fact = [14,25,16,17,18,19,20,21,22,23,24,25]

def Factorial_find(n):
    if n > 1:
        x = Factorial_find(n - 1) * n
    else:
        return 1
    return x

if __name__ == '__main__':
    start_thread = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
       future = executor.map(Factorial_find, Fact)
    end_thread = time.time()
    result = start_thread - end_thread
    print(result)

    start_process = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:
       future = executor.map(Factorial_find, Fact)
    end_process = time.time()
    result2 = start_process - end_process
    print(result2)

    if result > result2:
        print('ProcessPoolExecutor faster')
    else:
        print('ThreadPoolExecutor')


