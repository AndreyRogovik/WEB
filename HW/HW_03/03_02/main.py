import time
import multiprocessing
import concurrent.futures

def factorize(n):
    factors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060, 128, 255, 99999, 10651060]

    # Measure the time for synchronous execution
    start_time = time.time()
    result = [factorize(x) for x in numbers]
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")

    # Measure the time for parallel execution
    pool = multiprocessing.Pool(processes=len(numbers))
    start_time_2 = time.time()
    result_2 = pool.map(factorize, numbers)
    end_time_2 = time.time()
    pool.close()
    pool.join()
    print(f"Parallel execution time: {end_time_2 - start_time_2} seconds")

    with concurrent.futures.ProcessPoolExecutor(max_workers=len(numbers)) as executor:
        start_time_3 = time.time()
        result_3 = list(executor.map(factorize, numbers))
        end_time_3 = time.time()
    
    print(f"Parallel execution time using a context manager: {end_time_3 - start_time_3} seconds")