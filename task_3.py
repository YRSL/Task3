import time
from concurrent.futures import ThreadPoolExecutor


def function(arg):
    a = 0
    print("before: " + str(a))
    for _ in range(arg):
        a += 1
    time.sleep(3)
    print("after: " + str(a))
    return a


def main():
    start = time.time()
    a = 0
    max_workers = 5
    arg = [1000000]

    with ThreadPoolExecutor(max_workers) as executor:
        th_results = executor.map(function, arg*max_workers)
        answer = sum(th_results)

    end = time.time()
    print(end - start)

    print("----------------------", answer)  # ???


if __name__ == "__main__":
        main()
