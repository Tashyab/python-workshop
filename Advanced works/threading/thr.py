import threading 
import time

start_time = time.time()

def do_something(sec):
    print("Doing something...")
    time.sleep(sec)
    print("Done!")

if __name__=="__main__":
    # do_something()
    # do_something()
    # do_something()
    # do_something()
    # do_something()

    threads=[]
    for _ in range(5):
        t=threading.Thread(target=do_something, args=[2])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print(f"Process finished --- {round((time.time() - start_time), 2)} seconds ---")