class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[]for _ in range(numCourses)]
        for a , b in prerequisites:
            adj[b].append(a) # b->a
        visited=[False]* numCourses
        inRecursion=[False]*numCourses
        def dfs(u):
            visited[u]=True
            inRecursion[u]=True
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
                elif inRecursion[v]:
                    return True
            inRecursion[u]=False
            return False
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True