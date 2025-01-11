from collections import defaultdict, Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Helper function to check if b's frequencies are all covered by a
        def checkSubset(a_count: Counter, b_count: Counter) -> bool:
            for char, count in b_count.items():
                if a_count[char] < count:
                    return False
            return True

        # Combine all the requirements in words2 into a single maximum frequency count
        max_b_count = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                max_b_count[char] = max(max_b_count[char], count)

        # Result list
        res = []

        # Check each word in words1
        for word in words1:
            word_count = Counter(word)
            if checkSubset(word_count, max_b_count):
                res.append(word)

        return res
