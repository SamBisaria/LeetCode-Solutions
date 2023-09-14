class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxAverage = -999099999.999999
        total = 0.0000000
        length = 0
        for i in range(len(nums)):
            total += nums[i]
            length += 1
            if length > k:
                length -= 1
                total -= nums[i-k]
            average = total/k
            if average > maxAverage and length == k:
                maxAverage = average
        return maxAverage

        