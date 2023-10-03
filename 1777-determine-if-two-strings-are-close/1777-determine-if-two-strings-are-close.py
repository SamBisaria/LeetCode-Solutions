class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        letters1 = []
        occurences1 = []
        letters2 = []
        occurences2 = []
        for element in word1:
            if element not in letters1:
                letters1.append(element)
                occurences1.append(word1.count(element))
        for element in word2:
            if element not in letters2:
                letters2.append(element)
                occurences2.append(word2.count(element))
        occurences1.sort()
        occurences2.sort()
        letters1.sort()
        letters2.sort()
        return occurences1 == occurences2 and letters1 == letters2
        
        