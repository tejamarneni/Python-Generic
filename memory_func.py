#generated from Microsoft Copilot

import tracemalloc

def my_function():
    tracemalloc.start()
    
    a = [0] * 1000000
    b = [1] * 1000000
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 10**6} MB; Peak: {peak / 10**6} MB")
    
    tracemalloc.stop()

if __name__ == "__main__":
    my_function()
