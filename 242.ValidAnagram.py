class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # we use count function to check how many letters appears how many times in the string
        countS = {}
        countT = {}

        for ch in s:
            countS[ch] = 1 + countS.get(ch, 0) + 1

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0) + 1

        
        return countS == countT