from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            w = "".join(sorted(word))
            groups[w].append(word)

        return list(groups.values())