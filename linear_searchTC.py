array=[10,20,30,40,50]
print("Array:", array)
target = int(input("Enter the target value to search: "))

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target: 
            print("Target found at index:", i)
    return -1

linear_search(array, target)