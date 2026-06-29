class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_list = []
        for i in range(len(nums)):
            tmp_list = nums.copy()
            tmp_list.pop(i)
            value = 1
            for j in range(len(tmp_list)):
                value *= tmp_list[j]
            out_list.append(value)
        return out_list