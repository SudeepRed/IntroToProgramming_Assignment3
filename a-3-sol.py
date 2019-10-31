"""
CSE101: Introduction to Programming
Assignment 3
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
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    return sorted(points)


def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    return sorted(points, key = lambda x:x[1])


def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Closest pair of points: [(p1_x, p1_y), (p2_x, p2_y)]
    """
    point_1 = (-1,-1)
    point_2 = (-1,-1)

    min_dist = math.inf

    for i in range(len(plane)):
        for j in range(i+1, len(plane)):
            d = dist(plane[i], plane[j]) 
            if d < min_dist:
                min_dist = d
                point_1 = plane[i]
                point_2 = plane[j]

    return [min_dist, point_1, point_2] 


def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a given
    upper bound.

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine


    Returns:
        Closest pair of points: [(p1_x, p1_y), (p2_x, p2_y)] if
            distance between p1 and p2 is less than d. Otherwise
            return -1.
    """
    op = d
    p1 = (-1, -1)
    p2 = (-1, -1)

    """
    for (int i = 0; i < size; ++i)  
        for (int j = i+1; j < size && (strip[j].y - strip[i].y) < min; ++j)  
            if (dist(strip[i],strip[j]) < min)  
                min = dist(strip[i], strip[j]);  
  
    return min; 
    """

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # if points[j][1] - points[i][1] < op:
            #     break
            if dist(points[i], points[j]) < op:
                op = dist(points[i], points[j])
                p1 = points[i]
                p2 = points[j]

    if op == d:
        return -1
    else:
        return [op, p1, p2]

def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Closest pair of points from given points: [(p1_x, p1_y), (p2_x, p2_y)]
    """
    # print("points")
    # print(points)
    # print()
    # print()

    size = len(points)
    mid_point = points[size//2]
    
    if size <= 1:
        return [math.inf]
    elif size == 2:
        return [dist(points[0], points[1]), points[0], points[1]]

    left = efficient_closest_pair_routine(points[0:size//2])
    right = efficient_closest_pair_routine(points[size//2:])
    # print('left', left)
    # print('right', right)

    if left[0] < right[0]:
        d = left
    else:
        d = right

    strip = []

    for i in range(size):
        if abs(mid_point[0] - points[i][0]) < d[0]:
            strip.append(points[i])
    
    # print("strip")
    # print(strip)

    k = closest_pair_in_strip(sort_points_by_Y(strip), d[0])

    if k != -1:
        d = k

    return d



def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Closest pair of points: [(p1_x, p1_y), (p2_x, p2_y)]
    """
    points = sort_points_by_X(points)
    ans = efficient_closest_pair_routine(points)
    return ans



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points
    """
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]
    return random_points


import time

if __name__ == "__main__":
    num_pts = 10000
    # 'plane_size' = (X_max, Y_max)
    plane_size = (10000, 10000)
    # 'plane' is a list of points 
    plane = generate_plane(plane_size, num_pts)
    # plane = [(86, 65), (44, 33), (26, 38), (86, 67), (94, 42), (63, 69)]
    # plane = [(1,3), (2,10), (3,4), (3,8), (4,5), (7,3), (8,8), (8,9), (8,5), (9,3)]
    print(plane)
    
    p1 = time.time()
    print(naive_closest_pair(plane))
    p2 = time.time()
    print(efficient_closest_pair(plane))
    p3 = time.time()
    print(p2-p1)
    print(p3-p2)
