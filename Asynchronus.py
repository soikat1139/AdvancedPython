Asynchronous Programming:

It still takes one execution step at a time. The difference is that the system may not wait for an execution step to be completed before moving on to the next one.
This means that the program will move on to future execution steps even though a previous step hasn't yet finished and is still running elsewhere.
This also means that the program knows what to do when a previous step does finish running.


Concurrency:
Concurrency involves allowing multiple jobs to take turns accessing the same shared resources, like disk, network, or a single CPU core.

--->A common example is completing multiple network requests. The crude way to do it is to launch
    one request, wait for it to finish, launch another, and so on. The concurrent way to do it is to
    launch all requests at once, then switch among them as they get responses back.
---->Concurrency works by splitting a task into smaller subtasks that can be executed out of order so that multiple tasks can be partially advanced without waiting for the previous tasks to finish.
---->The goal of concurrency is to prevent tasks from blocking each other by switching among them when one is forced to wait on an external resource.

Example: Implementing network request function that takes a number and returns a dictionary about the success of the operation and result:

    import time
    def network_request(number):
          time.sleep(1.0)
           return{"Success":True,:result:number*2}

    def  fetch_square(number):
         response=network_request(number)
         if response["Success"]:
           print(response['result']



    fetch_square(2)
    fetch_square(3)
    fetch_square(4)

  In this it will always wait for like 1.0 time for every function to execute .
           To reduce CPU's wait time we can prepare the next function call while executing the current call:
           
  

          
