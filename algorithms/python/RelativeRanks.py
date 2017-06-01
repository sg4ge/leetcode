class Solution(object):
    topThreeRank = ['Gold Medal','Silver Medal','Bronze Medal']
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numRankDict = {}
        sortedNums = sorted(nums,reverse=True)
        rank = 1
        for num in sortedNums:
            numRankDict[num] = rank
            rank += 1
        ranks = []
        for num in nums:
            rank = numRankDict.get(num)
            if rank <= 3:
                ranks.append(self.topThreeRank[rank-1])
            else:
                ranks.append(str(rank))
        return ranks
