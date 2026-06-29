class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSub = nums[0]

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0

            curSum += nums[i]
            maxSub = max(curSum, maxSub)

        return maxSub