class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        counter = 0
        maximum = 0
        pointer = -1
        zeroes = []
        if len(nums) < 2:
            return 0
            
        while counter < len(nums):
            if nums[counter] == 0:
                if len(zeroes) < 1:
                    zeroes.append(counter)
                else:
                    pointer = zeroes[len(zeroes) - 1]
                    zeroes.append(counter)
            maximum = max(counter - pointer, maximum)
            counter += 1
        return maximum - 1
        