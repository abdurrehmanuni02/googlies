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


def gen_population(population_size):
    return [random_tour() for _ in range(population_size)]


def evaluate_population(population):
    return [tour_distance(tour) for tour in population]


def selection(population, num_parents):
    ranked_population = sorted(population, key=tour_distance)
    return ranked_population[:num_parents]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2


def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        i1, i2 = random.sample(range(len(tour)), 2)
        tour[i1], tour[i2] = tour[i2], tour[i1]
    return tour


def genetic_algorithm(population_size, num_generations, num_parents, mutation_rate):
    population = gen_population(population_size)
    for generation in range(num_generations):
        parents = selection(population, num_parents)
        offspring = []
        for i in range(0, num_parents, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            offspring.extend([child1, child2])
        population = offspring
    temp_best_solution = min(population, key=tour_distance)
    temp_best_distance = tour_distance(temp_best_solution)
    return temp_best_solution, temp_best_distance


if __name__ == "__main__":
    population_size = 50
    num_generations = 100
    num_parents = 10
    mutation_rate = 0.1

    print(evaluate_population(gen_population(20)))
    best_solution, best_distance = genetic_algorithm(population_size, num_generations, num_parents, mutation_rate)
    print("Best Solution:", best_solution)
    print("Best Distance:", best_distance)
