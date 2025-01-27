class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        res = []
        isReq = [[False] * numCourses for _ in range(numCourses)]
        preReqMap = defaultdict(list)
        queue = []
        
        for p in prerequisites:
            preReqMap[p[0]].append(p[1])
    
        # for p in preReqMap:
        #     queue.append(p)

        #     while queue:
        #         curr = queue.pop(0)
        #         for next in preReqMap.get(curr, []):
        #             queue.append(next)
        #             isReq[curr][next] = True

        for prereq, course in prerequisites:
            queue = deque()
            queue.append(prereq)
            while queue:
                curr = queue.popleft()
                for neighbor in preReqMap[curr]:
                    if not isReq[prereq][neighbor]:
                        isReq[prereq][neighbor] = True
                        queue.append(neighbor)

        for q in queries:
            res.append(isReq[q[0]][q[1]])
        
        return res
