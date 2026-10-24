import random

NUM_ROOMS = 10
rooms = [random.choice(['dirty', 'clean', 'obstacle']) for _ in range(NUM_ROOMS)]

if 'dirty' not in rooms:
    rooms[random.randint(0, NUM_ROOMS - 1)] = 'dirty'
if 'obstacle' not in rooms:
    rooms[random.randint(0, NUM_ROOMS - 1)] = 'obstacle'

vacuum_position = random.randint(0, NUM_ROOMS - 1)

while rooms[vacuum_position] == 'obstacle':
    vacuum_position = random.randint(0, NUM_ROOMS - 1)

print(f"Initial rooms: {rooms}")
print(f"Vacuum cleaner starts at room index: {vacuum_position}")

def clean_rooms(rooms, initial_position):
    cleaned_rooms = list(rooms)
    
    print("\n--- Cleaning Process ---")
    
    for i in range(initial_position, NUM_ROOMS):
        if cleaned_rooms[i] == 'obstacle':
            print(f"Vacuum at room {i}: Encountered an obstacle. Stopping rightward movement.")
            break
        elif cleaned_rooms[i] == 'dirty':
            print(f"Vacuum at room {i}: Cleaning dirty room.")
            cleaned_rooms[i] = 'clean'
        else:
            print(f"Vacuum at room {i}: Room is already clean.")

    for i in range(initial_position - 1, -1, -1):
        if cleaned_rooms[i] == 'obstacle':
            print(f"Vacuum at room {i}: Encountered an obstacle. Stopping leftward movement.")
            break
        elif cleaned_rooms[i] == 'dirty':
            print(f"Vacuum at room {i}: Cleaning dirty room.")
            cleaned_rooms[i] = 'clean'
        else:
            print(f"Vacuum at room {i}: Room is already clean.")

    print("--- Cleaning Complete ---")
    return cleaned_rooms

final_rooms = clean_rooms(rooms, vacuum_position)
print(f"\nInitial state of rooms: {rooms}")
print(f"Final state of rooms:   {final_rooms}")

if all(room == 'clean' for room in final_rooms if room != 'obstacle'):
    print("All accessible rooms are clean!")
else:
    print("Some rooms might still be dirty")
