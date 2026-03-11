# Title: Two Sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice. You can return the answer in any order. 
# Example 1: Input: nums = [2,7,11,15], 
# target = 9 
# Output: [0,1] 
# Explanation: Because nums[0] + nums[1] == 9, 
# we return [0, 1]. 
# Example 2: Input: nums = [3,2,4], 
# target = 6 
# Output: [1,2] 
# Example 3: Input: nums = [3,3], 
# target = 6 
# Output: [0,1] 
# Constraints: 
# 2 <= nums.length <= 10^4 
# -10^9 <= nums[i] <= 10^9 
# -10^9 <= target <= 10^9 
# Only one valid answer exists. Follow-up: Can you come up with an 
# algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

# Solution explanation:

# Step #1
# create an emply dictionary to store the numbers we've already encountered as KEYS,
# and their indices as values

# Step #2
# create a for loop for i(as the index), and num(as the value at that index). Using
# enumerate() method to iterate through the list of arrays

# Step #3
# assign a variable complement to target - num, (e.g., 9-2 = 7). The complement on the 1st 
# iteration is 7. Do we already encountered 7? No, so we the iteration continues.

# Step #4
# Add a condition that checks if we already seen a complement in previous iteration, if yes,
# we stop, if no, we continue

# Step #5
# if we finally found the complement, return a list containing seen[complement], so in this
# case that we have 7, so seen stored 2: 0
# In 2nd iteration will be, i = 1, num = 7, complement = 9 - 7 = 2
# Have we seen 2 before? Yes is the answer
# So seen dictionary will tell us that 2 was at index 0

# Step #6
# the line seen[num] = 1 gives us the two indices that add up to target.
# SO in the current situation, it will return [0, 1], which will satisfy the first test case
# and so on to other test cases

# If we didn't find a match, store the current number and its index in dictionary for future
# lookups

# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(n) - dictionary stores up to n elements

# The algorithm works by building up a "memory" of numbers as it goes, checking each new 
# number against what it's already seen.