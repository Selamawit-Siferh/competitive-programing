class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        return (2 * n) // gcd(2, n)