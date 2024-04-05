import random
import math

cities = {'A': (0, 0), 'B': (1, 3), 'C': (2, 5), 'D': (5, 3), 'E': (6, 0)}

#function to generate initial tour

def initial_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    return tour

#function to calculate th Eculindean distance between cities
def distance(city1,city2):
    x1,y1 = city1
    x2,y2 = city2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#function to calculate the totlal distance of the tour

def tour_distance(tour):
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += distance(cities[tour[i]],cities[tour[i+1]])
    #distance of returning to the starting city
    total_distance += distance(cities[tour[-1]],cities[tour[0]])

    return  total_distance

#stimulated annealing function to get the best path

def simulated_annealing(tour,initial_temp,cooling_rate,stopping_temperature):
    current_tour = tour
    current_distance = tour_distance(current_tour)
    best_tour = current_tour
    best_distance = current_distance
    temp = initial_temp
    while temp > stopping_temperature:
        #generate a neighbouring toure by randomly swapping 2 cities
        neighbour_tour = current_tour[:]
        indx1,indx2 = random.sample(range(len(neighbour_tour)),2)
        neighbour_tour[indx1],neighbour_tour[indx2] = neighbour_tour[indx2],neighbour_tour[indx1]

        neighbour_distance = tour_distance(neighbour_tour)
        delta_enerygy = neighbour_distance - current_distance
        if delta_enerygy < 0 or random.random() < math.exp((delta_enerygy)/temp):
            current_tour = neighbour_tour
            current_distance = neighbour_distance
        if current_distance < best_distance :
            best_distance = current_distance
            best_tour = current_tour

        # cooling down temperate
        temp *=cooling_rate

    return best_tour,best_distance


#Main

tour = initial_tour()
initial_temperature = 100
stopping_temperature = 0.1
cooling_rate = 0.95

best_tour,best_distance = simulated_annealing(tour,initial_temperature,cooling_rate,stopping_temperature)

print(f"Best Tour : {best_tour} \nBest Distance : {best_distance}")


