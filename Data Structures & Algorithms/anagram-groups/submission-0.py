class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return

        freqMaster = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in freqMaster:
                freqMaster[key] = []
            freqMaster[key].append(word)

        return list(freqMaster.values())
            
