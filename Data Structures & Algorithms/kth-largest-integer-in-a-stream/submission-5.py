class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        # cast nums into a min heap
        heapq.heapify(self.nums)

        # drop min values until the kth min value is reached
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        ## now minheap contains the k largest items in the nums

    def add(self, val: int) -> int:
        # add the value to the min heap
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
