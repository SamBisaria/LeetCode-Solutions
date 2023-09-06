class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""            
        length = 1
        for i in range(len(chars)):
            if i == len(chars) - 1:
                s += chars[i]
                if length > 1:
                    s += str(length)
                    length = 1
            elif chars[i] == chars[i+1]:
                length += 1
            else:
                s += chars[i]
                if length > 1:
                    s += str(length)
                    length = 1
        for i in range(len(s)):
            chars[i] = s[i]
        chars = chars[:len(s)]
        return len(chars)

        