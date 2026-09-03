class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_n(n):
            sums = 0
            while n:
                digit = n % 10
                sums += digit ** 2
                n //= 10
            return sums
        
        # set of seen values for stop rule
        seen_set = set()
        seen_set.add(n)
        
        while n != 1:
            n = sum_of_squares_of_n(n)
            if n in seen_set:
            ## if we see the same n twice -> it's a loop                
                return False
            else:
                seen_set.add(n)
        return True