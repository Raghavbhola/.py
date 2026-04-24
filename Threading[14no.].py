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

#Thread naming
#(1)------------------------------------------------------
import time
import threading
from threading import Thread

def myfunction_1(arg1):
    print(f"Thread Name: {threading.current_thread().name}")
    time.sleep(1)
Thread1 = threading.Thread(target= myfunction_1, args=(10, ),name = "LoginThread")
thread2 = threading.Thread(target= myfunction_1, args=(10, ),name = "SignupThread")
Thread1.start()
Thread1.join()
thread2.start()
thread2.join()
print("Existing Main Thread")    

#(2)-----------------------------------------------
import time
import threading
from threading import Thread

def myfunction_1(arg1):
    #threading.current_thread().name = "Application Thread"
    print(f"Thread Name: {threading.current_thread().name}")
    time.sleep(1)

thread1 = threading.Thread(target= myfunction_1, args=(10, ), name = "LoginThread")
thread2 = threading.Thread(target= myfunction_1, args=(10, ), name = "SignupThread")
thread3 = threading.Thread(target= myfunction_1, args=(10, ), name = "ApplicationThread")
print(" the Thread name is:",threading.current_thread().name)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
print("Existing Main Thread")        

#------------------------------
#Scheduling Threads:- 
#(1) Way to schedule threads is by using time.sleep() method. It will pause the thread for a specified amount of time.

import time
import threading

def myfunction_1(name, StartTime):
    now = time.time()
    elapsed_time = now - StartTime
    print(f"Elapsed Time: {elapsed_time}seconds, Name = {name}")
    time.sleep(1)

start = time.time()
print("Start",time.ctime(start))

thread1 = threading.Timer(2,myfunction_1, args=("Thread-1",start))
thread2 = threading.Timer(4,myfunction_1, args=("Thread-1",start))
thread3 = threading.Thread(target=myfunction_1,args=("Thread-3",start))

thread1.start()
thread1.join()
thread2.start()
thread2.join()
end = time.time()
print("End",time.ctime(end))
print("Existing Main Thread") 

#(2) Way to schedule thread is by using the schedule module. It allows you to schedule tasks at specific intervals ot times.
import sched
import time
scheduler = sched.scheduler(time.time, time.sleep)

def myfunction_1(name,startTime):
    now = time.time()
    elapsed_time = now - startTime
    print(f"Elapsed.Time: {elapsed_time}seconds, Name = {name}")

start = time.time()
print("Start", time.ctime(start))
scheduler.enter(2,1,myfunction_1, argument = ("Thread-1", start))
scheduler.enter(4,1,myfunction_1, argument = ("Thread-2", start))
scheduler.run()
end = time.time()
print("end", time.ctime(end))
print("Existing Main Thread")

#(3) way....
from datetime import datetime
import sched
import time

def add_numbers(a,b):
    print("Performing addition...", datetime.now())
    print("Time :", time.monotonic())
    print(f"The sum of {a} and {b} is : {a+b}")

scheduler = sched.scheduler()
print("Start Time:", datetime.now())
event1 = scheduler.enter(5,1,add_numbers, argument = (15,30))
print("Event created:", event1)
scheduler.run()
print("End time:", datetime.now())

#------------------------------------------------------------------------
#Thread pools - Its a mechanism to execute multiple threads concurrently. It is a way to manage a pool of worker threads that can be used to execute tasks in parallel. 
#               The main advantage of using a thread pool is that it can improve the performance of a program by reducing the overhead of creating and destroying threads.

# Multiproccessing.dummy and concurrent.futures.ThreadPoolExecutor are two different ways to create a thread pool in Python. 
# The main difference between the two is that multiprocessing.dummy is a wrapper around the threading module, while concurrent.futures.
# ThreadPoolExecutor is a higher-level interface for managing threads.
# The multiprocessing.dummy module provides a simple way to create a thread pool using the threading module. 
# It allows you to create a pool of worker threads and submit tasks to be executed by those threads
