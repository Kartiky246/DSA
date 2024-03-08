# Find the Largest element in an array
# Problem Statement: Given an array, we have to find the largest element in the array.

def find_max(arr):
    max=arr[0]
    for i in range(len(arr)):
        if max<arr[i]:
         max = arr[i]

    return max

print(find_max([2,3,3,2,34,55,2,5]))