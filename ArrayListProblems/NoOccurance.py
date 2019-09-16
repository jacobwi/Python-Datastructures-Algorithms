class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        does_not_occur = 0
        for i in nums:
            does_not_occur ^= i
        return does_not_occur