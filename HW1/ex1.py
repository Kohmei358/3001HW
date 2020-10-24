def robot_move(moves):
    x = 0
    y = 0

    for dir, dist in moves:
        if dir == 'N':
            y += dist
        elif dir == 'E':
            x += dist
        elif dir == 'S':
            y -= dist
        elif dir == 'W':
            x -= dist
        else:
            raise Exception("Valid Directions: (N,E,S,W) - Your input: " + str(dir))

    return x, y

# --- Test cases ---
# print(robot_move([])) => Assert (0, 0)
# print(robot_move([('N', 5), ('S', 3)])) => Assert (0, 2)
# print(robot_move([('Z', -10)])) => Assert Invalid Direciton Error
