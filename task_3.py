from concurrent.futures import ThreadPoolExecutor


def function(arg):
    a = 0
    for _ in range(arg):
        a += 1
    return a


def main():
    max_workers = 5
    arg = [1000000]

    with ThreadPoolExecutor(max_workers) as executor:
        th_results = executor.map(function, arg*max_workers)
        answer = sum(th_results)

    print("----------------------", answer)


if __name__ == "__main__":
        main()
