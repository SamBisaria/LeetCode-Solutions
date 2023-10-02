class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        maximum = 0
        pointer = -1
        zeroes = []

        if k >= len(nums):
            return len(nums)
        while counter < len(nums):
            if nums[counter] == 0:
                if len(zeroes) < k:
                    zeroes.append(counter)
                else:
                    if k == 0:
                        pointer = counter
                    else:
                        pointer = zeroes[len(zeroes) - (k)]
                        zeroes.append(counter)
            maximum = max(counter - pointer, maximum)
            counter += 1
        return maximum
                


        