"""
CSE101: Introduction to Programming
Assignment 3

Name        :N Sudeep Reddy
Roll-no     :2019313
"""



import math
import random



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    dist=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return dist



def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    x=0
    def xcoor(tup):
        return tup[x]
    points.sort(key=xcoor)
    return points  



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    x=1
    def ycoor(tup):
        return tup[x]
    points.sort(key=ycoor)
    return points  



def naive_closest_pair(plane):
    
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    q=math.inf
    p1=0
    p2=0
    t=0
    lst=[]
    if(len(plane)<=1):
        lst.append((q,plane[0]))
        return lst[0]
    else:
            for i,j in enumerate(plane):
                for x,y in enumerate(plane):
            
                    if (i==x):
                        pass
                    else:
                        if(dist(j,y)<q):
                            q=dist(j,y)
                            p1=j
                            p2=y
                            t=(q,p2,p1)
            lst.append(t)
    lst.sort()
    return lst[0]
    


def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    min=d
    lst=[]
    point=sort_points_by_Y(points)
    for i,j in enumerate(point):
        for x,y in enumerate(point):
            if(x==i):
                pass
            elif((y[0]-j[0])<d):
                if(dist(j,y)<d):
                    min=dist(j,y)
                    lst.append((min,j,y))
    lst.sort()
    if(min<d):
        return lst[0]
    else:
        return -1
                



def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    n=len(points)
    if(n<2 or n==2):
        return naive_closest_pair(points)
    mid=(n//2)
    d1=efficient_closest_pair_routine(points[0:mid])
    d2=efficient_closest_pair_routine(points[mid:])
    d=min(d1,d2)
    strip=[]
    for i in range(n):
        if(abs(points[i][0]-points[int(n/2)][0])<d[0]):
            strip.append(points[i])
            
    if(closest_pair_in_strip(strip,d[0])==-1):
        return d
    else:
        return min(d,closest_pair_in_strip(strip,d[0]))
        
    



def efficient_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    points=sort_points_by_X(plane)
    return efficient_closest_pair_routine(points)
    



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10    #size of plane for generation of points
    plane_size = (1000, 1000) 
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    print(naive_closest_pair(plane))
    print(efficient_closest_pair(plane))
