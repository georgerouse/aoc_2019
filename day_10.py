import math

def get_angle(asteroid_1, asteroid_2):
    angle = 0
    x_diff = asteroid_1[0] - asteroid_2[0]
    y_diff = asteroid_1[1] - asteroid_2[1]
    if asteroid_1[0] == asteroid_2[0]:
        if asteroid_2[1] > asteroid_1[1]:
            return 180
        else:
            return 0
    elif asteroid_1[1] == asteroid_2[1]:
        if asteroid_2[0] > asteroid_1[0]:
            return 90
        else:
            return 270

    elif asteroid_1[0] < asteroid_2[0] and asteroid_1[1] < asteroid_2[1]:
        angle += 90
    elif asteroid_1[0] > asteroid_2[0] and asteroid_1[1] < asteroid_2[1]:
        angle += 180
    elif asteroid_1[0] > asteroid_2[0] and asteroid_1[1] > asteroid_2[1]:
        angle += 270
    angle += abs(math.degrees(math.atan(x_diff/y_diff)))
    return angle


if __name__ == '__main__':
    # Get the input data
    with open('input/day_10.txt') as f:
        file_data = f.read()

    lines = [x for x in file_data.split('\n')]
    # Build a grid of tuple coordinates
    asteroids = []
    for y, line in enumerate(lines):
        grid_line = []
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    # Part 1:
    result = {}
    for asteroid in asteroids:
        angle_list = []
        for other_asteroid in asteroids:
            if asteroid == other_asteroid:
                pass
            else:
                angle = get_angle(asteroid, other_asteroid)
                if angle not in angle_list:
                    angle_list.append(angle)
        result[asteroid] = len(angle_list)

    print("Location: " + str(max(result, key=result.get)))
    print("Asteroids detected: " + str(result[max(result, key=result.get)]))
