import random
#implementing the GA algorithm to solve Max problem

#Pre-defined Genetic Algorithm Parameters
POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 10
MUTATION_RATE = 0.1
GENERATION = 10


#generating initial population

def generate_initial_population(population_size,chromosome_length):
    return [[random.randint(0,1) for _ in range(chromosome_length)] for _ in range(population_size)]


#Calculate the individual fitness
def calculate_fitness(individual):
    return sum(individual)

#selecting parents for mating

def selection(population,parent_num):
    selected_parents=[]

    for _ in range(parent_num):
       tournament = random.sample(population, 3)
       if len(selected_parents) > 0 :
           while selected_parents[0] in tournament:
               tournament = random.sample(population, 3)

       selected_parents.append(max(tournament,key=calculate_fitness))

    return selected_parents[0],selected_parents[1]

#crossover to create offsprings
def crossover(parent1,parent2):
    #lets get random crossover points
    crossover_point = random.randint(1,len(parent1)-1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1,offspring2

#Mutation for diversity
def mutation(individual,mutation_rate):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(int(not gene))
        else:
            mutated_individual.append(gene)
    return mutated_individual

# Main Genetic Algorithm

population = generate_initial_population(POPULATION_SIZE,CHROMOSOME_LENGTH)
for generation in range(GENERATION):
    fitness_score = [calculate_fitness(individual) for individual in population]
    print(f"Generation {generation} : Best Fitness : {max(fitness_score)}")
    #selecting parents
    parent1,parent2 = selection(population,2)
    offspring1,offspring2 = crossover(parent1,parent2)
    offspring1 = mutation(offspring1,MUTATION_RATE)
    offspring2 = mutation(offspring2,MUTATION_RATE)
    population.extend([offspring1,offspring2])

    #now the fittest individual will survive
    population = sorted(population,key=calculate_fitness,reverse=True)[:CHROMOSOME_LENGTH]

## calculate the fitness for each individual

print("Next generation : ",max([calculate_fitness(individual) for individual in population]))
for individual in population:
    print(f"{individual} : fitness {calculate_fitness(individual)}")
#selecting parents
#
# parent1,parent2 = selection(population,2)
# offspring1,offspring2 = crossover(parent1,parent2)
#
# print(f"Parent1 : {parent1}\nParent2 : {parent2}")
# print(f"offspring1 : {offspring1}\noffspring2 : {offspring2}")