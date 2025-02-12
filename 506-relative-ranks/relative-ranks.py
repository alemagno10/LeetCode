class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        idx = { value: i for i,value in enumerate(score)}
        ordered = sorted(score, reverse=True)

        for i,points in enumerate(ordered):
            if i == 0:
                score[idx[points]] = "Gold Medal"
            elif i == 1:
                score[idx[points]] = "Silver Medal"
            elif i == 2:
                score[idx[points]] = "Bronze Medal"
            else:
               score[idx[points]] = str(i+1)
        
        return score
        