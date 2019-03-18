class Solution(object):
    def maxprofit(self,prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

if __name__ == '__main__':
    print(Solution().maxprofit([7, 1, 5,3,6,4]))