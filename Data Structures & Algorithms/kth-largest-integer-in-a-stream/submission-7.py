class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        # cast nums into a min heap
        heapq.heapify(self.min_heap)

        # drop min values until the kth min value is reached
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        ## now minheap contains the k largest items in the nums

    def add(self, val: int) -> int:
        # add the value to the min heap
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
