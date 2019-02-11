# String to test
str = "I would like to test me OR you can replace me"

# This is O(n^2). NOT THE BEST
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
        

# Check it
print("Is Unique?: ", checkIfStringIsUnique(str))
