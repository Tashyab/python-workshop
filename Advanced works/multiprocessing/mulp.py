import multiprocessing
import time

start_time = time.time()


def do_something(secs):
    print("Doing something...")
    time.sleep(secs)
    print("Done!")


if __name__ == "__main__":
    # do_something()
    # do_something()
    # do_something()
    # do_something()
    # do_something()
    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target= do_something, args=[2])
        p.start()
        processes.append(p)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    for process in processes:
        process.join()

    print(f"Process finished --- {round((time.time() - start_time), 2)} seconds ---")
