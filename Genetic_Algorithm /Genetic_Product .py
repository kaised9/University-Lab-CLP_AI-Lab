import random
import math

pop_size = 100
mutation_rate = 0.2
max_Gen = 500

T = int(input("T = "))
k = int(input("K = "))

def fitness(individual):
    return abs(T - math.prod(individual))

def individual():
    return [random.randint(0, 9) for _ in range(k)]

def crossover(p1, p2):
    point = random.randint(1, k - 1)
    return p1[:point] + p2[point:]

def mutation(indivi):
    if random.random() < mutation_rate:
        index = random.randint(0, k - 1)
        indivi[index] = random.randint(0, 9)
    return indivi

def Gen_Algo():
    pop = [individual() for _ in range(pop_size)]

    for generation in range(max_Gen):
        pop.sort(key=lambda x: fitness(x))

        if fitness(pop[0]) == 0:
            print(pop[0])
            return pop[0]

        next_gen = pop[:20]

        while len(next_gen) < pop_size:
            p1 = random.choice(pop[:50])
            p2 = random.choice(pop[:50])
            child = crossover(p1, p2)
            child = mutation(child)
            next_gen.append(child)

        pop = next_gen

    print("Solution Not Found !!!")
    return None

sol= Gen_Algo()
