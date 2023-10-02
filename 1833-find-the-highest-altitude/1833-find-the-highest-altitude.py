class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        peak = 0
        for point in gain:
            altitude += point
            peak = max(altitude, peak)
        return peak
        