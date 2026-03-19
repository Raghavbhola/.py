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