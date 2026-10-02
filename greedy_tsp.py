#Travelling Salesman problem

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

def greedy_tsp(start=0):
    n = len(cities)
    visited = [False] * n
    tour = [start]
    visited[start] = True

    current = start # start value 0
    print("current:" + str(current))

    for _ in range(n - 1):
        next_city = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i]:
                #visted:[True, True, True, False, False]
                # print("cities[current]:"+ str(cities[current]) + "citites[i]:"+str(cities[i]))
                # A---->B(A,B)---->C(B,C)----->E(C-E)--->D(E,D)
                d = distance(cities[current], cities[i]) # d value is calculated from two cities
                # print("distance(d):"+ str(d)) i=0=>A, i=1=>B, i=2=>C, i=3=>D, i=4=>E
                # print("min_dist:"+ str(min_dist) ) # current state = 2, i =3,4
                # Compare(C,D) and compare(C,E)
                
                if d < min_dist: # min_dist = infinit
                   
                    min_dist = d

                    next_city = i # i=1, i=2
                    print(f"minimum_distance: {min_dist}")

        tour.append(next_city)
        visited[next_city] = True
        current = next_city
        print("Tour:"+ str(tour) + ", visted:" + str(visited) + ", current:"+str(current))

    return tour

# Run
tour = greedy_tsp()
print("Tour:", tour)



print(range(5))
for i in range(5):
    print(i)

#EXCLUSIVE
