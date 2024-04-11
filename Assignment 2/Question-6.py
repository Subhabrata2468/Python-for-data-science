'''
Write a program to find median of a given list of integers. Combine both odd and even number of terms.
'''
def find_median(nums):
    nums.sort()
    #print(nums)
    n = len(nums)
    #print(n)
    if n % 2 == 0:
        mid = n // 2
        #print(mid)
        median = (nums[mid - 1] + nums[mid]) / 2
        #print(median)
    else:
        mid = n // 2
        median = nums[mid]
    return median

# Example usage:
numbers = [5,3,8,1,2,9,4,7]
median = find_median(numbers)
print("Median of the list:", median)

'''
Median of the list: 4.5
'''
