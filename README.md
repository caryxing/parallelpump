# Parallel Pump
Asistant module. Startup N multiple processes to handle items in a list.

Example
-----------

Parallel printing with mutex:

```python
from parallelpump import Parapump

# Build your own function to handle each item
def myConcurrentFunc(item, mutex, sharedInfo):
    mutex.acquire()
    print("I am eating " + item)
    mutex.release()

if __name__ == '__main__':
    food = ["banana", "apple", "fried chicken", "pie", "battery", "flower"]

    # Create 3 sub processes to handle "food".
    pumper = Parapump(
        func = myConcurrentFunc, 
        listToParallelize = food, 
        numJobs = 3)

    # This run() function is blocked. 
    pumper.run()
```
