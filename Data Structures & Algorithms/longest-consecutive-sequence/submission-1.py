class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        sorted_nums = self.binary_insertion_sort_safak(nums)
        
        # Remove duplicates
        uniques_hash = {}
        for num in sorted_nums:
            uniques_hash[num] = None
        sorted_unique_nums = list(uniques_hash.keys())

        # Finding the longest consecutive sequence  
        differences = []
        counter = 1
        longest = 1

        # store differences between elements in a
        for i in range(len(sorted_unique_nums) - 1):
            differences.append(sorted_unique_nums[i+1] - sorted_unique_nums[i])    

        # based on how many consequtive 1s there're 
        for i in range(len(differences)):
            if differences[i] == 1:
                counter += 1
                longest = max(longest, counter)
            else:
                counter = 1
                
        longest = max(longest, counter)        

        return longest



    def binary_search_for_insertion_safak(self, arr: list[int], target: int, left: int, right: int) -> int:
        # Keep searching as long as there's a valid range
        while left <= right:
            # Aim to the middle
            aim = (left + right) // 2
            
            # Compare with the target and adjust the range
            if target == arr[aim]:
                return aim # found
            elif target > arr[aim]:
                left = aim + 1
            else:
                right = aim - 1
        
        # Return the left index if the target is not found
        return left


    def binary_insertion_sort_safak(self, arr: list[int]) -> list[int]:
        for i in range(1, len(arr)):
            current_value = arr[i]
            
            # Find the position to insert
            j = self.binary_search_for_insertion_safak(arr, current_value, 0, i - 1)

            # Shift everything to the right        
            for k in range(i, j, -1):
                arr[k] = arr[k - 1]

            # Insertion
            arr[j] = current_value
        return arr       