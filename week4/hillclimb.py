def heuristic(state):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(state):
    for row in range(4):
        for col in range(4):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print()


def hill_climbing(initial_state):
    current = initial_state

    while True:
        current_h = heuristic(current)

        print("Current State:", current)
        print("Heuristic:", current_h)
        print_board(current)

        if current_h == 0:
            print("Solution Found!")
            return current

        best_state = current
        best_h = current_h

        # Generate neighboring states
        for col in range(4):
            for row in range(4):
                if row != current[col]:
                    neighbor = current.copy()
                    neighbor[col] = row

                    h = heuristic(neighbor)

                    if h < best_h:
                        best_h = h
                        best_state = neighbor

        # Stop if no better neighbor exists
        if best_state == current:
            print("Local Minimum Reached! No solution found.")
            return None

        current = best_state


# Initial state
initial_state = [1, 3, 0, 2]

print("4 Queens using Hill Climbing Search")
hill_climbing(initial_state)
