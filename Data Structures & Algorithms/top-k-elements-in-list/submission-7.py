class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0

            frequencies[num] += 1

        sorted_freq = dict(sorted(frequencies.items(), key=lambda val: val[1]))

        return list(sorted_freq)[-k:]