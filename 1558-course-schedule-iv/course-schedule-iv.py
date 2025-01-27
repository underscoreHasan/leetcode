class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        res = []
        isReq = [[False] * numCourses for _ in range(numCourses)]
        preReqMap = defaultdict(list)
        
        for p in prerequisites:
            preReqMap[p[0]].append(p[1])
    

        for prereq, course in prerequisites:
            queue = deque()
            queue.append(prereq)
            while queue:
                curr = queue.popleft()
                for next in preReqMap[curr]:
                    if not isReq[prereq][next]:
                        isReq[prereq][next] = True
                        queue.append(next)

        for q in queries:
            res.append(isReq[q[0]][q[1]])
        
        return res
