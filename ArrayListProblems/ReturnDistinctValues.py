class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0;
        
        # Iterate through the array between the range of 0 and length of array
        for i in range(0, len(nums)):
            
            # if the current element at the i pointer not equal to the j pointer
            if nums[i] != nums[j]:
                
                # increment the j (meaning they're distinct)
                j += 1
                
                # Set the pointer i value to the j's pointer value
                nums[j] = nums[i]
        return j + 1