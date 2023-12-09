"""
Program 2
Given a collection of two numbers that specify an interval, merge all overlapping intervals. 
For example, 
Input [[1,3],[2,6],[8,10],[15,20],[16,25] ]
Output [[1,6],[8,10],[15,25]].
"""
# [1,3][2,6]-1,2,3,2,3,4,5,6-1,2,3,4,5,6-[1,6]
# [1,6][8,10]-1,2,3,4,5,6 8,9,10 -[1,6][8,10]
# [8,10][15,20]-8,9,10 15,16,17,18,19,20-[1,6][8,10][15,20]
# [1,6][8,10][15,20][16,25]-15,16,17,18,19,20 16,17,18,19,20,21,22,23,24,25-[1,6][8,10][15,25]





no_of_intervals = int(input("Enter the number of intervals: "))
intervals=[[1,3],[2,6],[8,10],[15,20],[16,25]]
# for j in range(no_of_intervals):
#     start = int(input(f"Enter the start point for Interval {j+1}: "))
#     end = int(input(f"Enter the end point for Interval {j+1}: "))
#     interval = [start,end]
#     intervals.append(interval)
merged_intervals=[]
current_inter=[]
overlapped_intervals=[]
for inter in intervals:
    prev_inter = current_inter
    start=int(inter[0])
    end=int(inter[1])
    range_=[]
    for i in range(start,end+1):
        range_.append(i)
    
    if merged_intervals:
        current_inter=range_
        merged_intervals.clear() 
    else:
        current_inter=range_
        
    
    if set(prev_inter) & set(current_inter):
        merged_intervals.append([prev_inter[0],current_inter[-1]])
        overlapped_intervals.extend(merged_intervals)
        
    

print(merged_intervals)
print(overlapped_intervals)