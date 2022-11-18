# Uses python3
import sys
import math

def get_distance(p1,p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def find_closest_pair(sorted_x_points, sorted_y_points):

    # get the length of points
    n = len(sorted_x_points)

    # ------------ base case ------------- #
    if n <= 3:
        return min_among3_or_less(sorted_x_points)



    # ------------ divide ------------- #
    # get the middle index
    mid = int(n/2)

    ## get x points
    dl = sorted_x_points[:mid]
    dr = sorted_x_points[mid:]
    
    # get the midpoint
    midpoint = sorted_x_points[mid][0]

    # the two half arrays of left and right
    left_y_points, right_y_points=[],[]
    for x in sorted_y_points:
        if x[0] <= midpoint:
            left_y_points.append(x)
        else:
            right_y_points.append(x)

    # get the closest pair from left
    x1,y1,dist_left = find_closest_pair(dl,left_y_points)

    # get the closest pair from right
    x2,y2,dist_right = find_closest_pair(dr,right_y_points)


    # ------------ combine ------------- #

    # compare distance 
    if dist_left <= dist_right:
        # assign the distance to distance form left
        d = dist_left

        # set points to be the closest
        point = (x1,y1)
    else:
        # assign the distance to distance form right
        d = dist_right

        # set points to be the closest
        point = (x2,y2)


    p, q, m = lineclosestpair(sorted_x_points, sorted_y_points, d, point)

    # return the distance and the two points
    if d <= m:
        return point[0], point[1], d
    else:
        return p, q, m

def min_among3_or_less(x_points):

    # set the min to the first 2 points
    min_dist = get_distance(x_points[0],x_points[1])

    p1, p2, n = x_points[0], x_points[1], len(x_points)
    
    # if there are only 2 points then they are the closest
    if n == 2:
        return p1, p2, min_dist


    for i in range(2):

        for j in range(i+1,3):
            # see the min distance
            if i!=0 and j!=1 :
                d = get_distance(x_points[i],x_points[j])
                if d < min_dist:
                     p1, p2, min_dist = x_points[i], x_points[j], d

    return p1,p2,min_dist

def lineclosestpair(xsort, ysort, d, best):

    # get the number of points
    n = len(xsort)
    
    # get the middle point of x
    mid_x = xsort[int(n/2)][0]

    # filter the y
    s = []
    for i in ysort:
        if mid_x - d <= i[0] <= mid_x+d:
            s.append(i)

    len_s = len(s)
    for i in range(len_s-1):
        for j in range(i+1,min(i+6,len_s)):

            p, q = s[i], s[j]
            new_d = get_distance(p,q)
            if new_d < d:
                d = new_d
                best = p, q

    return best[0], best[1], d

def minimum_distance(x, y):
    # combine x & y to make a point
    point = list(zip(x,y))

    # sort x and y
    xsort = sorted(point,key = lambda x:x[0])
    ysort = sorted(point,key = lambda x:x[1])
    
    # recive the points and minimum distance between them
    p1, p2, min = find_closest_pair(xsort,ysort)

    return min

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
