'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
Approach: Loop over both strings and find matches while incrementing the var count whenever the condition is true
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for jewel in J:
            for stone in S:
                if (jewel == stone):
                    count += 1
        
        return count