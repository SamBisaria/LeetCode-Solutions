class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        numbers = []
        occurences = []
        for element in arr:
            if element not in numbers:
                numbers.append(element)
                occurences.append(arr.count(element))
        return len(set(occurences)) == len(occurences)