from threading import Thread, Lock
import time
import random
import sys

forks = [[1,"free"],[2,"free"],[3,"free"],[4,"free"],[5,"free"]]


philosophers = [1,2,3,4,5]
eaten_philosophers = []

lock = Lock()

def philosopher(i):
    global eaten_philosophers
    global forks
    if forks[i-1][1] == "free" and i not in eaten_philosophers:
        forks[i-1][1] = "used"
        if forks[i % 5][1] == "free":
            lock.acquire()
            forks[i % 5][1] = "used"
            print(f"Philosopher {i} is eating")
            time.sleep(random.uniform(2.25, 3.5))
            forks[i-1][1] = "free"
            forks[i % 5][1] = "free"
            eaten_philosophers.append(i)
            lock.release()
        else:
            forks[i-1][1] = "free"
            time.sleep(random.uniform(0.5, 1.5))
            
            

threads = []
def main():
    while eaten_philosophers != philosophers:
            random.shuffle(philosophers)
            for i in philosophers:
                thread = Thread(target=philosopher, args=(i,))
                thread.start()
                threads.append(thread)
    
            
    print("all philsophers are ok")
    for thread in threads:
        thread.join()
    
    print("All philosophers have finished eating")
    sys.exit(0)  # Ensure the program exits


if __name__ == "__main__":
    main()
