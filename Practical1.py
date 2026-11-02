
from collections import deque

def water_jug(capacity1, capacity2, target):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        current_path = path + [(x, y)]

        if x == target or y == target:
            return current_path

        next_states = []

        # Fill Jug 1
        next_states.append(((capacity1, y), "Fill Jug 1"))

        # Fill Jug 2
        next_states.append(((x, capacity2), "Fill Jug 2"))

        # Empty Jug 1
        next_states.append(((0, y), "Empty Jug 1"))

        # Empty Jug 2
        next_states.append(((x, 0), "Empty Jug 2"))

        # Pour Jug 1 -> Jug 2
        amount = min(x, capacity2 - y)
        next_states.append(
            ((x - amount, y + amount), "Pour Jug 1 -> Jug 2")
        )

        # Pour Jug 2 -> Jug 1
        amount = min(y, capacity1 - x)
        next_states.append(
            ((x + amount, y - amount), "Pour Jug 2 -> Jug 1")
        )

        for state, action in next_states:
            if state not in visited:
                queue.append((state, current_path + [action]))

    return None


capacity1 = 4
capacity2 = 3
target = 2

solution = water_jug(capacity1, capacity2, target)

if solution:
    print("Water Jug Solution:")
    for i, item in enumerate(solution):
        print(item)
else:
    print("No solution exists.")
