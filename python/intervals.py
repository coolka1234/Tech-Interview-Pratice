# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

def insert_interval(intervals, new_interval):
    def is_included(interval, sec_interval):
        return (interval[0]>=sec_interval[0] and interval[1]<=sec_interval[1])

    result=[]
    for interval in intervals:
        print(f'{interval} with new {new_interval}')
        print(f'comparing: {new_interval[1]} with {interval[0]}')
        if is_included(interval, new_interval):
            print('includes')
            continue
        elif(new_interval[0]>=interval[0] and new_interval[0]<=interval[1]):
            new_interval[0]=interval[0]
            print(f'new interval: {interval[0]}')
        elif(new_interval[1]>=interval[0] and new_interval[1]<=interval[1]):
            new_interval[1]=interval[1]
            print(f'new r-interval: {new_interval[1]}, compared to {interval[1]}')
            result.append([new_interval[0], new_interval[1]])
        else:
            print(f'appended: {interval}')
            result.append(interval)
    return result
            
            
    
# intervals=[[1,3], [3,5], [6,8], [9, 12], [12, 16]]
# new_interval=[2,10]
# intervals=[[1,3],[6,9]]
# new_interval=[2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
new_interval = [4,8]

print(insert_interval(intervals, new_interval))
