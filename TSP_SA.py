import math
import random

cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 5),
    'D': (5, 3),
    'E': (6, 0)
}


def dis(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def random_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    return tour


def tour_distance(tour):
    td = 0
    for i in range(len(tour) - 1):
        td += dis(tour[i], tour[i + 1])
    td += dis(tour[-1], tour[0])
    return td


def gen_neighbours(tour):
    neighbours = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            temp_tour = tour.copy()
            temp_tour[i], temp_tour[j] = temp_tour[j], temp_tour[i]
            neighbours.append(temp_tour)
    return neighbours


def acceptance_probability(delta, temperature):
    if delta < 0:
        return 1
    return math.exp(-delta / temperature)


def simulated_annealing(tour, temp, cooling_rate):
    current_tour = tour
    current_distance = tour_distance(current_tour)
    temp_best_tour, temp_best_distance = current_tour, current_distance
    while temp > 0.1:
        current_neighbours = gen_neighbours(current_tour)
        selected_neighbour = random.choice(current_neighbours)
        selected_distance = tour_distance(selected_neighbour)
        delta = selected_distance - current_distance
        if acceptance_probability(delta, temp) > random.random():
            current_tour = selected_neighbour
            current_distance = selected_distance
            if current_distance < temp_best_distance:
                temp_best_tour = current_tour
                temp_best_distance = current_distance

        temp *= cooling_rate
    return temp_best_tour, temp_best_distance


if __name__ == "__main__":
    cooling_rate = 0.99
    initial_temp = 100
    initial_tour = random_tour()
    best_tour, best_distance = simulated_annealing(initial_tour, initial_temp, cooling_rate)
    print("Best Tour:", best_tour)
    print("Best Distance:", best_distance)
