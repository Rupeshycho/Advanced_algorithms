import numpy as np
def find_max(arr):
    maximum = arr[0]

    for x in arr:
        if x > maximum:
            maximum = x

    return maximum

arr = np.array(range(1, 1000000000))
print("Maximum value:", find_max(arr))

