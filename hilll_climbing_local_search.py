import random
import math

cities = [
    (0, 0),
    (1, 5),
    (5, 2),
    (6, 6),
    (8, 3)
]

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def total_distance(tour):
    dist = 0
    print("distance function: " + str(tour))
    for i in range(len(tour)-1):
        dist += distance(cities[tour[i]], cities[tour[i+1]])
    dist += distance(cities[tour[-1]], cities[tour[0]])
    return dist

def hill_climbing():
    n = len(cities)
    current = list(range(n))
    random.shuffle(current)
    
    improved = True
    while improved:
        improved = False
        for i in range(n):
            for j in range(i+1, n):
                new = current[:]
                print("new: " + str(new))
                new[i], new[j] = new[j], new[i]

                if total_distance(new) < total_distance(current):
                    current = new
                    improved = True
                    print("current:  " + str(current))
                #For tracing the distance
                print("total_distance(new): "+ str(total_distance(new)) + "total_distance(current)): " + str(total_distance(current)))

    return current, total_distance(current)
# Run
tour, dist = hill_climbing()
print("Tour:", tour)
print("Distance:", dist)