#Threading:- A thread is the smallest unit of execution managed by the operating system’s scheduler.

#Multi-threading -- Multi means many , threading means process   ,Any task in execution state by machine or anything.

#An Operating system is capability to handle multiple processes concurrently.

#NOTE - It is Light-weight version --> sub-process(thread) where, thread is like [thread-based Parallelism]
#  small part of a single existing process i.e. called thread.

# A process start with a single thread(main).

#Thrad life-cycle:--> object-> it has different stages.

# *States of a thread life-cycle:->
#      (1)creating a thread
#      (2)starting a thread --> start() --> run()
#      (3)Blocked/Paused --> join()
#      (4)Synchronizing threads:-
#                            --> ensures orderly execution of thread
#                            --> shared resource managment amoung threads
#     (5)Termination:--> task complete
#                      or  with an execption. 

#(1)--------------->
import threading
from threading import Thread
import time

def add_numbers(a,b):
    time.sleep(1)    #1sec. time limit
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")

def basic_func():
    print("Basic function is running currently...")

def subtract_numbers(a,b):
    time.sleep(12)    
    result = a-b
    print(f"The difference of {a} and {b} is: {result}")

def multiple_numbers(a,b):
    time.sleep(8)
    result = a*b
    print(f"The product of {a} and {b} is: {result}")

def cube_numbers(a):
    time.sleep(3)
    result = a**3
    print(f"The cube of {a} is: {result}")

Thread(target = add_numbers, args=[5,3]).start()
Thread(target = subtract_numbers,args=(5,3)).start()
Thread(target = multiple_numbers,args=(5,3)).start()
Thread(target = cube_numbers,args=(5,3)).start()
Thread(target = basic_func).start()
exitflag = 0

#(2)---------------->
