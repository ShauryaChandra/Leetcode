# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        word1 = {}
        word2 = {}

        for ch in ransomNote:
            word1[ch] = word1.get(ch, 0) + 1

        for ch in magazine:
            word2[ch] = word2.get(ch,0) + 1

        for ch in word1:
            if word1[ch] > word2.get(ch, 0):
                return False
            
        return True

