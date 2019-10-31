import sys
import random
import time
import pickle
import math

def generate_test_cases():
    #DO NOT RUN THIS
    sizes = [10]*5+[100]*10+[1000]*5
    test_cases = []
    for s in sizes:
        gen = random.sample(range(-1*s*s, s*s), s)
        random_points = [(i%s + 1, i//s + 1) for i in gen]
        test_cases.append(random_points)
    with open("test_cases.txt", "wb") as fp:
        pickle.dump(test_cases, fp)


def ref_closest_pair(plane):
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


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


with open("test_cases.txt", "rb") as fp:
    #Download test_cases.txt again from repository if there is an error
    test_cases = pickle.load(fp)

if len(sys.argv) <= 1:
    print("No test file passed.")

print("Testing...", sys.argv[1])

test_module = __import__(sys.argv[1][:-3])


test_module.naive_closest_pair(points)

avg_time_approach1 = 0
avg_time_approach2 = 0
count = 0

for i in range(len(test_cases)):

    t_a1 = test_module.naive_closest_pair(test_cases[i])
    t_a2 = test_module.naive_closest_pair(test_cases[i])

    r = ref_closest_pair(test_cases[i])