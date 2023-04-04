import time

def gridTraveler(n, m):
    if (n == 1 and m == 1): 
        return 1
    if (n == 0 or m == 0):
        return 0
    return gridTraveler(n - 1, m) + gridTraveler(n, m-1)


# Test the function
n = 14
m = 14

# Start the timer
start_time = time.time()

result = gridTraveler(n,m)

# Calculate the elapsed time in milliseconds
elapsed_time_ms = (time.time() - start_time) * 1000

print(f"For {n} by {m} grid number of ways: {result}")
print(f"Execution time: {elapsed_time_ms:.2f} ms")
