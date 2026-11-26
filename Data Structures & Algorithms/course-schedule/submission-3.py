class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited_from = set()
        visited_to = set()

        for a, b in prerequisites:
            if (a in visited_from and b in visited_to) or a==b:
                return False
            visited_from.add(b)
            visited_to.add(a)

        return True