class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        input-array given named prerequisite 
        prerequisite[i]=[a,b]
        you must take course b if i want to take course a
        [0,1] indicates that must have to take course 1 before taking
        course 0 
        total =numCourses from 0 to numcourses-1
        true?possible to finish all the courses
        false? not possible to finish the courses

        """
        #Map each course to its pre requisite
        preMap={i:[] for i in range(numCourses)}
        for crs , pre in prerequisites:
            preMap[crs].append(pre)
        visiting=set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs]==[]:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        