# Find Second Smallest and Second Largest Element in an array
# Problem Statement: Given an array, find the second smallest and second largest element in the array. 
# Print ‘-1’ in the event that either of them doesn’t exist.

def second_largest(arr):
    second_max = -1
    max = arr[0]
    for i in range(len(arr)):
        if max<arr[i]:
            second_max = max
            max = arr[i]
        else:
            if second_max < arr[i] and second_max!=-1:
                second_max = arr[i]

    return second_max


print(second_largest([1,1,1,1,1]))