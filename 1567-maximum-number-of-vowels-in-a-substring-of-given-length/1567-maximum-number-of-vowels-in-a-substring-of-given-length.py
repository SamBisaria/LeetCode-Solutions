class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        maxLength = 0
        length = 0
        for i in range(k - 1, len(s)):
            if i == k-1:
                for j in range(i-k+1, i+1):
                    if s[j] in vowels:
                        length += 1
            else:
                if s[i] in vowels:
                    if s[i-k] not in vowels:
                        length += 1
                elif s[i-k] in vowels:
                        length -= 1
            maxLength = max(length, maxLength)
        return maxLength

        