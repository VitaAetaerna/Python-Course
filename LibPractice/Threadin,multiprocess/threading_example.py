import threading

def cube(a,b):  # Define Cube Function
    print(a*b)

def square(a): # Define Square Function
    print(a*a) 

if __name__ == "__main__":
    # Create Threads
    thread_cube = threading.Thread(target=cube, args=(5,5,))
    thread_square = threading.Thread(target=square, args=(10,))
    # Start Threads
    thread_cube.start()
    thread_square.start()
    thread_cube.join()
    thread_square.join()