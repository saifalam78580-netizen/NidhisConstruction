# NidhisConstruction - Python 3

n = int(input().strip())

commands = []

for _ in range(n):
    a, b, direction = input().split()
    commands.append((int(a), int(b), direction.lower()))

# Sort by existing cube number, then by new cube number
commands.sort(key=lambda x: (x[0], x[1]))

# Direction movement
move = {
    "top": (0, 1),
    "up": (0, 1),
    "down": (0, -1),
    "left": (-1, 0),
    "right": (1, 0)
}

# cube -> (x, y)
pos = {}

# position -> cube
grid = {}

# Process commands
for existing, new_cube, direction in commands:

    # Existing cube must already have a position
    if existing not in pos:
        # The first cube can be placed at (0, 0)
        if not pos:
            pos[existing] = (0, 0)
            grid[(0, 0)] = existing
        else:
            continue

    x, y = pos[existing]
    dx, dy = move[direction]

    nx = x + dx
    ny = y + dy

    # If another cube already exists here, remove it
    if (nx, ny) in grid:
        old_cube = grid[(nx, ny)]
        if old_cube in pos:
            del pos[old_cube]

    # Place new cube
    pos[new_cube] = (nx, ny)
    grid[(nx, ny)] = new_cube


# Target cube
target = int(input().strip())

# If target doesn't exist
if target not in pos:
    print("-1 -1 -1 -1")
else:
    x, y = pos[target]

    # Up, Down, Left, Right
    directions = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0)
    ]

    answer = []

    for dx, dy in directions:
        neighbour = grid.get((x + dx, y + dy), -1)
        answer.append(neighbour)

    print(*answer)