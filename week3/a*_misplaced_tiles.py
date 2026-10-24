import heapq

def misplaced_tiles(state, goal):
    h = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            h += 1
    return h

def get_moves(state):
    neighbors = []
    zero_idx = state.index(0)
    r, c = zero_idx // 3, zero_idx % 3
    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

    for move, (dr, dc) in moves.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr * 3 + nc
            temp = list(state)
            temp[zero_idx], temp[new_idx] = temp[new_idx], temp[zero_idx]
            neighbors.append((tuple(temp), move))
    return neighbors

def solve_misplaced(start, goal):
    h_start = misplaced_tiles(start, goal)
    queue = [(h_start, 0, start, [])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        for next_state, move in get_moves(state):
            if next_state not in visited:
                next_g = g + 1
                next_h = misplaced_tiles(next_state, goal)
                next_f = next_g + next_h
                heapq.heappush(queue, (next_f, next_g, next_state, path + [(move, next_state)]))
    return None

def print_board_with_metrics(state, g, h):
    f = g + h
    for i in range(0, 9, 3):
        row_str = " ".join(map(str, state[i:i+3])).replace("0", "_")
        print(f"  {row_str}")
    print(f"  g={g}, h={h}, f={f}\n")

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
solution = solve_misplaced(start, goal)

print("Initial State (Using Misplaced Tiles):")
print_board_with_metrics(start, 0, misplaced_tiles(start, goal))

if solution:
    for step, (move, state) in enumerate(solution, 1):
        print(f"Step {step}: Move {move}")
        g = step
        h = misplaced_tiles(state, goal)
        print_board_with_metrics(state, g, h)
else:
    print("No solution found.")
