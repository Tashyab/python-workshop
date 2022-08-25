from asyncio import futures
import time
import concurrent.futures

start_time = time.time()


def do_something(secs):
    print("Doing something...")
    time.sleep(secs)
    return f"Done in {secs} seconds!"


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 2)
        # f2 = executor.submit(do_something, 2)

        secs = list(reversed([1, 2, 3, 4, 5]))
        # results = [executor.submit(do_something, sec) for sec in secs]

        # Return as the sequence in the list
        results = executor.map(do_something, secs)

        # print(f1.result())
        # print(f2.result())

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        for result in results:
            print(result)

    print(f"Process finished --- {round((time.time() - start_time), 2)} seconds ---")
