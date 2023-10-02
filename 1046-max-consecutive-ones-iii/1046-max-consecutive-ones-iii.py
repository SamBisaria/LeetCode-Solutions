class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        counter = 0
        kcounter = k
        maximum = 0
        pointer = -1
        zeroes = []
        if k >= len(nums):
            pass
            #return len(nums)
        while counter < len(nums):
            if nums[counter] == 0:
                if kcounter > 0:
                    kcounter -= 1
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
                


        