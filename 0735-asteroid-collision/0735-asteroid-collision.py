class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = len(asteroids) - 1
        while i > 0:
            if (asteroids[i] < 0 and asteroids[i - 1] > 0):
                if abs(asteroids[i]) > abs(asteroids[i-1]):
                    del(asteroids[i-1])
                elif abs(asteroids[i]) < abs(asteroids[i-1]):
                    del(asteroids[i])
                else:
                    del(asteroids[i])
                    del(asteroids[i-1])
                    i -= 1
                if i < len(asteroids):
                    i += 1
            i -= 1
        return asteroids        