'''
    This function checks if two strings are anagrams.
'''

# This function performs the anagram check in O(n) time complexitiy using pythonic built-in functions
def anagram_check_pythonic(s1, s2):
    # Pythonic way to replace empty spaces
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


# This function perform more manual way of checking 
# NOTE: assuming both strings do not include any spaces
def anagram_check_without_spaces(s1, s2):
    if (len(s1) != len(s2)):
        return False

    count = {}
    for index in s1:
        if index in count:
            count[index] += 1
        else:
            count[index] = 1

    for index in s2:
        if index in count:
            count[index] -= 1
        else:
            count[index] = 1

    for x in count:
        if count[x] != 0:
            return False
    return True


# This function perform more manual way of checking 
# NOTE: assuming both strings may include any spaces
def anagram_check_without_spaces(s1, s2):
    # Pythonic way to replace empty spaces
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if (len(s1) != len(s2)):
        return False

    count = {}
    for index in s1:
        if index in count:
            count[index] += 1
        else:
            count[index] = 1

    for index in s2:
        if index in count:
            count[index] -= 1
        else:
            count[index] = 1

    for x in count:
        if count[x] != 0:
            return False
    return True


# Below should return true
print(anagram_check_pythonic("god", " d o g"))

# Below should retun false
print(anagram_check_pythonic("god", "o g"))  

    