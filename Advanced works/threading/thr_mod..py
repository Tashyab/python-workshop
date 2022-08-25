import concurrent.futures
import time

start_time = time.time()

def do_something(sec):
    print("Doing something....")
    time.sleep(sec)
    return f"Done in {sec} seconds!"

if __name__=="__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 2)
        # f2 = executor.submit(do_something, 2)

        secs = list(reversed([1, 2, 3, 4, 5]))
        # results = [executor.submit(do_something, sec) for sec in secs]

        results =  executor.map(do_something, secs) # Return as the sequence in the list

    
    # print(f1.result())
    # print(f2.result())

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    for result in results:
        print(result)

    print(f"Process finished --- {round((time.time() - start_time), 2)} seconds ---")