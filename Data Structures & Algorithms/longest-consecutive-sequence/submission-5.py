class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        # Sort and remove duplicates
        sorted_unique_nums = sorted(set(nums))

        # Finding the longest consecutive sequence  
        # differences = []
        counter = 1
        longest = 1

        for i in range(1, len(sorted_unique_nums)):
            if sorted_unique_nums[i] - 1 == sorted_unique_nums[i-1]:
                counter += 1
                longest = max(longest, counter)
            else:
                counter = 1       

        return longest