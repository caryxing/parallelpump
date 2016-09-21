# parallelpump
Asistant module. Pump items in a list with multi processes.

# Example
```
from parallelpump import Parapump

def concurrentFuc(item, mutex, sharedInfo):
    mutex.acquire()
    print("I am eating " + item)
    mutex.release()

if __name__ == '__main__':
    todoList = ["banana", "apple", "fried chicken", "pie", "battery", "flower"]

    pumper = Parapump(
        func = concurrentFuc, 
        listToParallelize = todoList, 
        numJobs = 3)

    pumper.run()
```
