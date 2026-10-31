
import random
import math

N = 8

# Calculate heuristic
def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Print chess board
def print_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


# Simulated Annealing algorithm
def simulated_annealing():

    # Fixed initial state (valid solution)
    current = [0, 4, 7, 5, 2, 6, 1, 3]

    temperature = 100
    cooling_rate = 0.95

    while temperature > 0.01:

        current_h = heuristic(current)

        print("State:", current, "Heuristic:", current_h)

        if current_h == 0:
            print("\nSolution Found!")
            print("Final State:", current)
            print_board(current)
            return

        neighbor = current.copy()

        col = random.randint(0, N - 1)
        row = random.randint(0, N - 1)

        neighbor[col] = row

        neighbor_h = heuristic(neighbor)

        delta = current_h - neighbor_h

        if delta > 0:
            current = neighbor

        elif random.random() < math.exp(delta / temperature):
            current = neighbor

        temperature *= cooling_rate

    print("\nSolution not found!")


# Main program
print("8 Queens using Simulated Annealing")
simulated_annealing()
