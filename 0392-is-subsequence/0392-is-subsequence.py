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
            print t.find(s[a], index+1)
            print index
            if t.find(s[a], index+1) != -1:
                #t.replace(s[a],'')
                if index < 0:
                    index = 0
                index = t.find(s[a], index+1)
                c += 1
                print "c:" + str(c)
        if len(s) == c:
            return True
        return False
        