firstString = "god"
secondString = "dog"


# Pythonic Extended Slice
# O(n) time complex.
# [begin:end:step] leaving begin and end and decrementing by 1 to reverse the string
def slicePermutation (str1, str2):
    if (str1 == str2[::-1]):
        return True
    return False

print(slicePermutation(firstString, secondString))