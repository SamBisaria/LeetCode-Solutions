class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pairs = 0
        columns = []
        for i in range(len(grid)):
            columns.append([a[i] for a in grid])
            pairs += grid.count(columns[i])
        return pairs
        

        