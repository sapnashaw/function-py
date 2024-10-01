#4. Write a Python program using multithreading where one thread adds numbers to a list, and another
#   thread removes numbers from the list. Implement a mechanism to avoid race conditions using
#   threading.Lock


'''
Certainly! Below is a Python program that demonstrates multithreading, where one thread adds numbers to a list and another thread removes numbers from the same list. The program uses threading.Lock to avoid race conditions when accessing the shared list.

python
Copy code
import threading
import time
import random

# Shared resource
shared_list = []
lock = threading.Lock()
'''
def add_numbers():
    for i in range(10):
        time.sleep(random.uniform(0.1, 0.5))  # Simulate some delay
        with lock:  # Acquire the lock before modifying shared_list
            shared_list.append(i)
            print(f"Added: {i}, List: {shared_list}")

def remove_numbers():
    for i in range(10):
        time.sleep(random.uniform(0.1, 0.5))  # Simulate some delay
        with lock:  # Acquire the lock before modifying shared_list
            if shared_list:
                removed = shared_list.pop(0)
                print(f"Removed: {removed}, List: {shared_list}")

if __name__ == "__main__":
    # Create threads
    thread_add = threading.Thread(target=add_numbers)
    thread_remove = threading.Thread(target=remove_numbers)

    # Start threads
    thread_add.start()
    thread_remove.start()

    # Wait for both threads to complete
    thread_add.join()
    thread_remove.join()

    print("Final List:", shared_list)
'''
Explanation:
Shared Resource: shared_list is a list that both threads will access.

Lock Initialization: A Lock object named lock is created to control access to the shared resource.

Adding Thread:

The add_numbers function adds numbers (0 to 9) to shared_list.
It uses lock to ensure that only one thread can modify the list at a time, preventing race conditions.
Removing Thread:

The remove_numbers function removes numbers from the front of the list.
It also uses lock to ensure safe access to shared_list.
Thread Creation and Execution:

Two threads are created: one for adding and one for removing numbers.
Both threads are started and then joined to wait for their completion.
Output:
The program will output messages showing which numbers were added or removed from the list while maintaining thread safety through the use of lock.

This implementation ensures that concurrent modifications to the list do not lead to race conditions, providing a simple example of how to use threading with locks in Python.

'''


