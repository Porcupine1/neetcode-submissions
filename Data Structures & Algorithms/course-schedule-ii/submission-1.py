class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        res = []
        prereqs = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereqs[course].append(pre)
    
        print(prereqs)

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            if prereqs[course] == []:
                res.append(course)
                visited.add(course)
                return True

            cycle.add(course)
            for nxt in prereqs[course]:
                if not dfs(nxt):
                    return False
            
            res.append(course)
            prereqs[course] = []
            cycle.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
            