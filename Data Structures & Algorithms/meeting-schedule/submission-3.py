class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        cur = 0
        for i in range(len(intervals)):
            if intervals[i].start >= cur:
                cur = intervals[i].start
            else:
                return False
            if intervals[i].end >= cur:
                cur = intervals[i].end
            else:
                return False
        return True