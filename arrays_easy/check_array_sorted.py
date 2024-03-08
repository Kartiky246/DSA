# Problem Statement: Given an array of size n, write a program to check if the given array is sorted
# in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True,
# Else return False.

# Note: Two consecutive equal values are considered to be sorted.


def array_is_rotated_sorted(nums):
    no_of_negative_inversion=0
    for i in range(len(nums)-1):
        if(nums[i]>nums[i+1]):
            no_of_negative_inversion+=1
            if no_of_negative_inversion>1:
                return False
            if(nums[0]<nums[len(nums)-1]):
                return False
            
    return True