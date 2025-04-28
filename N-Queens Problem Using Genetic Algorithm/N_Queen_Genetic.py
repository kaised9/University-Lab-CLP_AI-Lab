import random
def create_random_board(size):
    return [random.randint(1, size) for _ in range(size)]

def calculate_fitness(board):
    horizontal_collisions = sum([board.count(queen) - 1 for queen in board]) / 2
    diagonal_collisions = 0

    n = len(board)
    left_diagonal = [0] * (2 * n)
    right_diagonal = [0] * (2 * n)

    for i in range(n):
        left_diagonal[i + board[i] - 1] += 1
        right_diagonal[len(board) - i + board[i] - 2] += 1

    for i in range(2 * n - 1):
        if left_diagonal[i] > 1:
            diagonal_collisions += (left_diagonal[i] - 1) / (n - abs(i - n + 1))
        if right_diagonal[i] > 1:
            diagonal_collisions += (right_diagonal[i] - 1) / (n - abs(i - n + 1))

    return int(max_fitness - (horizontal_collisions + diagonal_collisions))

def calculate_probability(board):
    return calculate_fitness(board) / max_fitness

def select_random_parent(population, probabilities):
    population_with_prob = list(zip(population, probabilities))
    total = sum(prob for board, prob in population_with_prob)
    r = random.uniform(0, total)
    running_sum = 0
    for board, prob in population_with_prob:
        running_sum += prob
        if running_sum >= r:
            return board
    return population[0]


def crossover(parent1, parent2):
    n = len(parent1)
    cut_point = random.randint(0, n - 1)
    return parent1[:cut_point] + parent2[cut_point:]

def mutate(child):
    n = len(child)
    idx = random.randint(0, n - 1)
    new_value = random.randint(1, n)
    child[idx] = new_value
    return child

def print_board_details(board):
    print("Board: {}, Fitness: {}".format(str(board), calculate_fitness(board)))

def solve_n_queens():
    global max_fitness
    size = int(input("Enter The Number Of Queens : ")) 
    max_fitness = (size * (size - 1)) / 2 
  
    population = [create_random_board(size) for _ in range(100)]
    generation = 1

    while True:
        fitness_values = [calculate_fitness(board) for board in population]
        if max_fitness in fitness_values:
            break

        print("\n-----Generation {}-----".format(generation))
        probabilities = [calculate_probability(board) for board in population]

        new_population = []
        for _ in range(len(population)):
            parent1 = select_random_parent(population, probabilities)
            parent2 = select_random_parent(population, probabilities)

            child = crossover(parent1, parent2)

            if random.random() < 0.03:  
                child = mutate(child)

            print_board_details(child)
            new_population.append(child)

            if calculate_fitness(child) == max_fitness:
                break

        population = new_population
        best_fitness = max(calculate_fitness(board) for board in population)
        print("\nBest Fitness in Generation {}: {}".format(generation, best_fitness))

        generation += 1

    print("\nSolved in Generation {}!".format(generation - 1))

    for board in population:
        if calculate_fitness(board) == max_fitness:
            print("\nOne of the solutions:")
            print_board_details(board)
            final_board = board
            break
        
    chessboard = [["x" for _ in range(size)] for _ in range(size)]
    for col in range(size):
        row = size - final_board[col]
        chessboard[row][col] = "Q"

    print("\nFinal Chess Board Are :")
    for row in chessboard:
        print(" ".join(row))

if __name__ == "__main__":
    solve_n_queens()
