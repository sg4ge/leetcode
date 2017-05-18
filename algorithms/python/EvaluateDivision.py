class Solution(object):
    divisionResultDict = {}
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.divisionResultDict = {}
        self.resolve(equations,values)
        return self.getResult(queries)

    def findRight(self,left):
        if self.divisionResultDict.has_key(left) == False:
            return None
        right = left
        rightDivisionResult = [right,1.0]
        while self.divisionResultDict.has_key(right):
            divisionResult = self.divisionResultDict.get(right)
            if right == divisionResult[0]:
                break
            right = divisionResult[0]
            value = rightDivisionResult[1] * divisionResult[1]
            rightDivisionResult[0] = right
            rightDivisionResult[1] = value
            self.divisionResultDict[left] = rightDivisionResult
        return rightDivisionResult

    def resolve(self,equations,values):
        for (equation,value) in zip(equations,values):
            leftDivisionResult = self.findRight(equation[0])
            rightDivisionResult = self.findRight(equation[1])
            if leftDivisionResult == None:
                leftDivisionResult = [equation[0],1.0]
                self.divisionResultDict[equation[0]] = leftDivisionResult
            if rightDivisionResult == None:
                rightDivisionResult = [equation[1],1.0]
                self.divisionResultDict[equation[1]] = rightDivisionResult
            if leftDivisionResult[0] != rightDivisionResult[0]:
                left = leftDivisionResult[0]
                right = rightDivisionResult[0]
                value = (rightDivisionResult[1] / leftDivisionResult[1]) * value
                divisionResult = [right,value]
                self.divisionResultDict[left] = divisionResult

    def getResult(self,queries):
        result = []
        for query in queries:
            left = self.findRight(query[0])
            right = self.findRight(query[1])
            if left == None or right == None:
                result.append(-1.0)
            elif left[0] != right[0]:
                result.append(-1.0)
            else:
                result.append(left[1]/right[1])
        return result 
