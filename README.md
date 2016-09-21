# parallelpump
Asistant module. Pump items in a list with multi processes.

Quick Start
-----------

Parallel printing with mutex:

```python
from parallelpump import Parapump

def concurrentFunc(item, mutex, sharedInfo):
    mutex.acquire()
    print("I am eating " + item)
    mutex.release()

if __name__ == '__main__':
    todoList = ["banana", "apple", "fried chicken", "pie", "battery", "flower"]

    pumper = Parapump(
        func = concurrentFunc, 
        listToParallelize = todoList, 
        numJobs = 3)

    pumper.run()
```
