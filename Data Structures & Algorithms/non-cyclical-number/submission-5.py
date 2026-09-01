class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_n(n: int) -> int:
            str_n = str(n)
            sums = 0
            for char in str_n:
                sums += int(char)**2
            return sums
        
        seen_set = set()
        seen_set.add(n)
        while n != 1:
            n = sum_of_squares_of_n(n)
            if n in seen_set:
                return False
            else:
                seen_set.add(n)
        return True
            

