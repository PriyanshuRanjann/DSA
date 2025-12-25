"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

def two_sums(nums: list, target: float):
    for i in range (len(nums)):
        for j in range(i+1,len(nums)) :
            if nums[i] + nums[j] == target:
                return [i, j]
    return "Unavailable"
                
                

if __name__=="__main__":
    nums = [1,0,4,6,9]
    print(nums)
    target = 7
    print(target)
    result = two_sums(nums,target)
    print(result)