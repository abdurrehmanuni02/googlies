import random


def fitness(chromosome):
    conflicts = 0
    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            if chromosome[i] == chromosome[j] or abs(i - j) == abs(chromosome[i] - chromosome[j]):
                conflicts += 1
    return 28 - conflicts


def generate_chromosome():
    return random.sample(range(8), 8)


def crossover(parent1, parent2):
    offspring = [-1] * 8
    for i in range(8):
        if random.random() < 0.5:
            offspring[i] = parent1[i]
    for i in range(8):
        if parent2[i] not in offspring:
            offspring[offspring.index(-1)] = parent2[i]
    return offspring


def mutate(chromosome):
    idx1, idx2 = random.sample(range(8), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome


def select_parents(population):
    parent1 = max(random.sample(population, k=5), key=fitness)
    parent2 = max(random.sample(population, k=5), key=fitness)
    return parent1, parent2


def genetic_algorithm(population_size, generations):
    population = [generate_chromosome() for _ in range(population_size)]
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            new_population.extend([offspring1, offspring2])
        population = new_population
    return max(population, key=fitness), fitness(max(population, key=fitness))


if __name__ == "__main__":
    population_size = 100
    generations = 1000
    best_solution, best_fitness = genetic_algorithm(population_size, generations)
    print("Best Solution:", best_solution)
    print("Fitness Score:", best_fitness)
