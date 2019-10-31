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

# generate_test_cases()

with open("test_cases.txt", "rb") as fp:
    #Download test_cases.txt again from repository if there is an error
    test_cases = pickle.load(fp)

if len(sys.argv) <= 1:
    print("No test file passed.")

print("Testing...{}\n".format(sys.argv[1]))

test_module = __import__(sys.argv[1][:-3])

avg_time_approach1 = 0
avg_time_approach2 = 0
count = 0
wrong = 0
wrong_flag = False

for i in range(len(test_cases)):
    wrong_flag = False
    p1 = time.time()
    t_a1 = test_module.naive_closest_pair(test_cases[i])
    p2 = time.time()
    t_a2 = test_module.efficient_closest_pair(test_cases[i])
    p3 = time.time()
    r = ref_closest_pair(test_cases[i])
    # r = [0, (1,1), (1,1)]

    if len(t_a1) !=3 or len(t_a2) !=3 or r[0] != t_a1[0] or t_a1[0] != t_a2[0] or dist(t_a1[1], t_a1[2]) != dist(t_a2[1], t_a2[2]):
        wrong_flag = True
        wrong += 1
    
    print("Case [{}]:\t{}\n".format(i, "WA" if wrong_flag == True else "AC"), end="")

    if(len(test_cases[i]) >= 1000):
        count += 1
        avg_time_approach1 += (p2 - p1)
        avg_time_approach2 += (p3 - p2)

correct = len(test_cases) - wrong
print("\nCorrect:\t{}\nIncorrect:\t{}".format(correct, wrong))
marks = 0
if wrong == 0:
    marks = 3
elif correct/(correct + wrong) >= 0.75:
    marks = 2

print("* Section 1: {}/3".format(marks))

assert count > 0
avg_time_approach1 = avg_time_approach1/count
avg_time_approach2 = avg_time_approach2/count

marks = 0
if avg_time_approach1/avg_time_approach2 >= 10 and wrong == 0:
    marks = 1

print("\n\nAverage Speedup for >= 1000 points: {}\n* Section 2: {}/1".format(avg_time_approach1/avg_time_approach2, marks))