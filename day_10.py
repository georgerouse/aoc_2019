import math

def get_distance(asteroid_1, asteroid_2):
    return math.sqrt((asteroid_1[0] - asteroid_2[0]) ** 2 + (asteroid_1[1] - asteroid_2[1]) ** 2)

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
        angle += abs(math.degrees(math.atan(x_diff/y_diff)))
    elif asteroid_1[0] > asteroid_2[0] and asteroid_1[1] < asteroid_2[1]:
        angle += 180
        angle += abs(math.degrees(math.atan(x_diff/y_diff)))
    elif asteroid_1[0] > asteroid_2[0] and asteroid_1[1] > asteroid_2[1]:
        angle += 270
        angle += abs(math.degrees(math.atan(y_diff/x_diff)))
    else:
        angle += abs(math.degrees(math.atan(y_diff/x_diff)))
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

    # Part 2:
    monitoring_station = (20, 20)
    result = {}

    for other_asteroid in asteroids:
        if monitoring_station == other_asteroid:
            pass
        else:
            angle = get_angle(monitoring_station, other_asteroid)
            if angle not in result.keys():
                result[angle] = [other_asteroid]
            else:
                dict_asteroids = result[angle]
                dict_asteroids.append(other_asteroid)
                result[angle] = dict_asteroids

    counter = 0
    angle_list = sorted(list(result.keys()))
    for angle in angle_list:
        ast_list = result[angle]
        ast_list.sort(key=lambda a: get_distance(monitoring_station, a), reverse=True)
        exploded_ast = ast_list.pop()
        counter += 1
        if counter == 200:
            print("200th: "+ str(exploded_ast))
            break
    print("Part 2 answer: " + str((exploded_ast[0]*100) + exploded_ast[1]))
    
