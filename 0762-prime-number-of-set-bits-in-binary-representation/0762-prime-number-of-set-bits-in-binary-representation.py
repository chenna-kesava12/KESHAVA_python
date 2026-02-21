class Solution:
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        def countBits(n):
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count
        
        result = 0
        for num in range(left, right + 1):
            if countBits(num) in primes:
                result += 1
        
        return result