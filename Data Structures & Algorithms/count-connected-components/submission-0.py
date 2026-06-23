class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*len(adj)
        def dfs(u):
            visited[u]=True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        count=0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count
    
        