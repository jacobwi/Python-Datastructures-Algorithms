# Pythonic implementation
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] = digits[len(digits) - 1] + 1
        return digits