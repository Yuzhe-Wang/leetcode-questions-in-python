class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        result = []
        
        for i in range(len(intervals)):
            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]
            
            # non-overlapping
            if end < currentStart:
                result.append(newInterval)
                return result + intervals[i:]
            elif start > currentEnd:
                result.append(intervals[i])
                
            # overlapping
            else:
                start = min(start, currentStart)
                end = max(end, currentEnd)
                newInterval = [start, end]
            
        result.append(newInterval)
        return result