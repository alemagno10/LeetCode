from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        transformations = 1
        words = defaultdict(set)

        def gen_patterns(w):
            wl, patterns = list(w), set()
            for i,c in enumerate(w):
                wl[i] = "*"
                patterns.add("".join(wl))
                wl[i] = c
            return patterns 

        for w in wordList:
            for p in gen_patterns(w):
                words[p].add(w)

        queue = deque([beginWord])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return transformations
                if curr in visited:
                    continue
                visited.add(curr)
                patterns = gen_patterns(curr)
                for p in patterns:
                    adj = words[p].difference(set(curr))
                    queue.extend(adj)
            transformations += 1

        return 0
