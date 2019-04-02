'''
    This function checks if two strings are anagrams.
'''

# This function performs the anagram check in O(n) time complexitiy using pythonic built-in functions
def anagram_check_pythonic(s1, s2):
    # Pythonic way to replace empty spaces
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


# Below should return true
print(anagram_check_pythonic("god", " d o g"))

# Below should retun false
print(anagram_check_pythonic("god", "o g"))  

    