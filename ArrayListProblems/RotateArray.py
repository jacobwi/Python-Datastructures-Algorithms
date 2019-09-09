
class Solution(object):

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        print("elements we're rotating to the left\n",nums[-k:])
        print("elements we're rotating to the right\n",nums[:-k])
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
ex = Solution()
print(ex.rotate(nums, k))