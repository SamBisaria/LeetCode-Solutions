class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = list(s.split())
        words.reverse()
        result = ""
        for i in range(len(words)):
            if i is 0:
                result += words[i]
            else:
                result += " " + words[i]
        return result
