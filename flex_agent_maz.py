
maze = [
    [0, 0, 1, 0, 'G'],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0]
]

start = (0, 0)

def is_goal(cell):
    return cell == 'G'

def get_possible_actions(pos, maze):
    actions = []
    x, y = pos

    directions = {
        "right": (x, y + 1),
        "left": (x, y - 1),
        "down": (x + 1, y),
        "up": (x - 1, y)
    }

    for action, (nx, ny) in directions.items():
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == 0 or maze[nx][ny] == 'G':
                actions.append(action)

    return actions

def move(pos, action):
    x, y = pos

    moves = {
        "right": (x, y + 1),
        "left": (x, y - 1),
        "down": (x + 1, y),
        "up": (x - 1, y)
    }

    return moves.get(action, pos)

def reflex_agent(maze, start):
    pos = start
    visited = set()
    path = [pos]

    print("Agent Movement Path:")

    while True:
        x, y = pos
        cell = maze[x][y]

        if is_goal(cell):
            print(" Goal reached!")
            break

        visited.add(pos)

        actions = get_possible_actions(pos, maze)

        actions = [a for a in actions if move(pos, a) not in visited]

        if not actions:
            print(" Agent stuck (no valid moves)")
            break

        for priority in ["right", "down", "left", "up"]:
            if priority in actions:
                next_action = priority
                break
        else:
            next_action = actions[0]

        pos = move(pos, next_action)
        path.append(pos)

        print(f"Moved {next_action} → {pos}")

    print("\nFinal Path:", path)


if __name__ == "__main__":
    reflex_agent(maze, start)