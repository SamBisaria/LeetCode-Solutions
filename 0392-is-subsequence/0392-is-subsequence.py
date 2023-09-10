class Solution(object):
    def isSubsequence(self, s, t):
        j = 0
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
        return j == len(s)
        