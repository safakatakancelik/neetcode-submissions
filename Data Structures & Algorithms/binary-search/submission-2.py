class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, (len(nums) - 1)

        while left <= right:
            aim = (left + right) // 2
            if target == nums[aim]:
                return aim # found
            elif target > nums[aim]:
                left = aim + 1
            else:
                right = aim - 1

        return -1
