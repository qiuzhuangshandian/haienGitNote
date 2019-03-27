import itertools
import sys

line = sys.stdin.readline()
tmp_points = list(map(int,line.split(" ")))
points = [(tmp_points[2*i],tmp_points[2*i+1]) for i in range(5) ]

indeces = [1,2,3,4,5]
points = [(0,0)]+points
iter_conditions = itertools.permutations(indeces)


distance = lambda x,y:((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5


for i, item in enumerate(iter_conditions):
    tmp_item = [0]+list(item)+[0]

    if i == 0:
        min_l = 0
        for j in range(len(tmp_item)-1):
            min_l += distance(points[tmp_item[j]],points[tmp_item[j+1]])
        sel_path = item
    else:
        l = 0
        for j in range(len(tmp_item)-1):
            l += distance(points[tmp_item[j]],points[tmp_item[j+1]])

        if l<min_l:
            min_l = l 
            sel_path = item

print(int(min_l))

