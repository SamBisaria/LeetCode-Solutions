class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        if len(word1) > len(word2):
            longer = word1
            shorter = word2
        else:
            longer = word2
            shorter = word1
        for i in range(len(longer)):
            if i >= len(shorter):
                while i < len(longer):
                    result += longer[i]
                    i+=1
                break
            result += word1[i]
            result += word2[i]
        return result
