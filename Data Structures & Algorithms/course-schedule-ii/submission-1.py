class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)      # b -> a

        visited = [False] * numCourses
        inRecursion = [False] * numCourses

        order = []

        def dfs(u):

            visited[u] = True
            inRecursion[u] = True

            for v in adj[u]:

                if not visited[v]:
                    if dfs(v):
                        return True

                elif inRecursion[v]:
                    return True

            inRecursion[u] = False

            # postorder insertion
            order.append(u)

            return False

        for i in range(numCourses):

            if not visited[i]:

                if dfs(i):
                    return []

        return order[::-1]