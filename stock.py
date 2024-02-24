class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        currentValue=float('inf')
        for i in prices:
            if i<currentValue:
                currentValue=i
            maxProfit=max(maxProfit,i-currentValue)
        return maxProfit