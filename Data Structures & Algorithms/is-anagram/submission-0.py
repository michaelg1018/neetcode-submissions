class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        tFreq = {}

        for letter in s:
            if letter in sFreq:
                sFreq[letter] += 1
            else:
                sFreq[letter] = 1

        for letter in t:
            if letter in tFreq:
                tFreq[letter] += 1
            else:
                tFreq[letter] = 1

        return sFreq == tFreq