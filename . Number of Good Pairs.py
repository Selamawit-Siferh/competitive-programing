from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = defaultdict(int)
        result = 0
        
        for num in nums:
            count_dict[num] += 1
        
        for count in count_dict.values():
            result += count * (count - 1) // 2
        
        return result