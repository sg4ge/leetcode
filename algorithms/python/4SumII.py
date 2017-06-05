class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype:
        """
        res = 0
        result = {}
        for num1 in A:
            for num2 in B:
                num = num1 + num2
                result[num] = result.get(num,0) + 1
                
        for num1 in C:
            for num2 in D:
                num = num1 + num2
                res = res + result.get(-1*num,0)
                
        return res
