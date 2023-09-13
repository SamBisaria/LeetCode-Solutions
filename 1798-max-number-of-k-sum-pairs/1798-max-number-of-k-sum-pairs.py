from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_count = Counter(nums)
        operations = 0
        
        for num in nums:
            complement = k - num
            if num_count[complement] > 0 and num_count[num] > 0:
                if num == complement:
                    if num_count[num] >= 2:
                        operations += 1
                        num_count[num] -= 2
                else:
                    operations += 1
                    num_count[num] -= 1
                    num_count[complement] -= 1
        return operations
