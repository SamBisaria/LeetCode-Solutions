class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = -1
        c = 0
        for a in range(len(s)):
            if t.find(s[a], index+1) != -1:
                if index < 0:
                    index = 0
                index = t.find(s[a], index+1)
                c += 1
        return len(s) == c
        