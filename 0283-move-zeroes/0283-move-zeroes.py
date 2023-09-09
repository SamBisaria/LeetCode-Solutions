class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroes += 1
                nums.pop(i)
            else:
                i += 1
        for num in range(zeroes):
            nums.append(0)
        