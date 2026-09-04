def two_sum(nums, target):
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
        
nums = [2, 7, 11, 15] 
target = 9 
output = two_sum(nums, target) 
print(output)


#Time Complexity: O(n) - I only iterate through the nums list a single time. 
#Inside the loop, checking if the complement exists in the num_to_index dictionary and inserting a new key-value pair both take O(1) average time.
#Space Complexity: O(n) - In the worst-case scenario.its O(1) as we didn.t use any extra memory
