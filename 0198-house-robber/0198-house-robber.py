class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        S = [0] * n
        S[0] = nums[0]
        S[1] = max(S[0], nums[1])
        for i in range(2, n):
            S[i] = max(S[:i-1]) + nums[i]
        print(S)
        return max(S)
