class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: L==t[int]
        :type n: int
        :rtype: bool
        """
        flowers = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True
        for i in range(len(flowerbed)):
            if flowerbed[i] is not 1:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
                elif i == (len(flowerbed) - 1):
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
                else:
                    if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
        if flowers >= n:
            return True
        else:
            return False
