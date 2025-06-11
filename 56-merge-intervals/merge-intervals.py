class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''same start and end = overlapping
        [[1,3],[2,6],[8,10],[15,18]]
        [1,3]+[2,6]=>1,6
        [8,10]=>[8,10]
        [15,18]=>[15,18]
        [1,10],[2,6],[7,9],[8,10]
        '''
        '''psuedocode:
        sort the array elements by the first index
        greedy appraoch:
        for interval in intervals:
            look at the second index of current interval
            look ahead to find the interval which has a start > end of our current interval
            keep track of the max end index you've seen alredy
            merge the intervals inbetween (by taking the start index of the first and end index of the max end)    
        '''

        intervals.sort(key = lambda x:x[0])

        res = []
        curr = intervals[0]

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start <= curr[1]:
                curr[1] = max(curr[1], end) #update end index of global interval
            else:
                res.append(curr)
                curr = intervals[i]
        
        res.append(curr)
        
        return res







