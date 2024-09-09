class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        seen = set()
        levels = {}
        
        for start_node in range(len(graph)):
            if start_node not in seen:
                q.append(start_node)
                levels[start_node] = 0
                while len(q) > 0:
                    u = q.popleft()
                    seen.add(u)
                    for v in graph[u]:
                        if v not in levels:
                            levels[v] = levels[u] + 1
                            q.append(v)
                        elif abs(levels[v] - levels[u]) % 2 == 0: 
                            return False 
        return True