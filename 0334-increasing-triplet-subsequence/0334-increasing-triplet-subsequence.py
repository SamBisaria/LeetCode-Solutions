class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 1
        a = nums[0]
        b = None
        c = None
        while i < len(nums):
            if nums[i] < a:
                a = nums[i]
                c = None
            elif (nums[i] > a and b is None) or (nums[i] > a and nums[i] < b):
                b = nums[i]
            elif nums[i] > b:
                c = nums[i]
            if a < b and b < c:
                return True
            i += 1
        return False