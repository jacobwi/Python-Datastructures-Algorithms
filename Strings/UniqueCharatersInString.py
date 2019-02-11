# String to test
str = "I would like to test me OR you can replace me"

# Brute Force Method: This is O(n^2) time and O(1) space. NOT THE BEST in terms of time
def checkIfStringIsUnique(str):
    
    # Begin an iterator from index 0 to the length of the string
    for character in range(len(str)):

        # Begin another iterator from index of character plus one to the length of the string
        for secondCharacter in range(character + 1, len(str)):

            # Check if both characters are equal
            if (str[character] == str[secondCharacter]):
                return False


    # Return true when all the above conditions are not met
    return True
        

# Hash table/list to memic ASCII values in the keys of the table
# It iterate through the characters in the strings flipping the index
# where it equals the character's ASCI value 
# Twice faster than the above method
# O(n) time
def bitCharacterUniqueFlipper(str):
    if (len(str) > 128):
        return False
    
    charBitsHash = [False] * (128)
    for character in str:
        index = ord(character)
        if (charBitsHash[index]):
            return False
        charBitsHash[index] = True
    return True

# Check it
print("Is Unique?: ", checkIfStringIsUnique(str))

print("Is Unique? (Bitmap): ", bitCharacterUniqueFlipper(str))
