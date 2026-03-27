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

Thread(target = add_numbers, args=(5,3)).start()
Thread(target = subtract_numbers,args=(5,3)).start()
Thread(target = multiple_numbers,args=(5,3)).start()
Thread(target = cube_numbers,args=(5,)).start()
Thread(target = basic_func).start()
exitflag = 0

#(2)---------------->
import time
import threading
from threading import Thread

exitflag = 0
class KunalThread(Thread):
    def __init__(self, threadID, name, counter):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"starting thread : {self.name}")
        self.print_time(self.counter,2) 
        print(f"Existing thread: {self.name}")

    def print_time(self, counter, delay):
        while counter:
            if exitflag:
                break
            time.sleep(delay)
            print(f"{self.name}: {time.ctime(time.time())}")    
            counter -=1
thread1 = KunalThread(1,"Thread-1", 5)
thread2 = KunalThread(2,"Thread-2",10)
thread1.start()
thread2.start()
print("Existing Main Thread")

#Joining Threads:- making one thread wait until another finishes execution, ensuring tasks run in the correct order.

import time
import threading
from threading import Thread

def myfunction_1(arg1):
    for i in range(arg1):
        print(f"Function 1 is running for :{i}")
        time.sleep(1)
def myfunction_2(arg1):
    for i in range(arg1):
        print(f"Function 2 in running for : {i}")
        time.sleep(1)
Thread1 = threading.Thread(target= myfunction_1, args=(10, ))
thread2 = threading.Thread(target= myfunction_2, args=(10, ))
Thread1.start()
Thread1.join(timeout= 5)
thread2.start()
thread2.join()
print("Existing Main Thread")                