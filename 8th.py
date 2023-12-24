import threading
import time

def func_1():
    for i in range(10):
        print("Thread 1")
        time.sleep(1)

def func_2():
    for i in range(10):
        print("Thread 2")
        time.sleep(1)

thread_1 = threading.Thread(target=func_1)
thread_2 = threading.Thread(target=func_2)

thread_1.start()
thread_2.start()