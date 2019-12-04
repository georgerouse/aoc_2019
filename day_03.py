import os

if __name__ == '__main__':
    # Get the input data
    with open('input/day_03.txt') as f:
        file_data = f.read()
        data = file_data.split('\n')
        data = [x.split(',') for x in data]

    # Initialise (assuming only 2 wires)
    direction_map = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    wire_1 = data[0]
    wire_2 = data[1]
    wire_1_map = {}
    wire_2_map = {}

    for wire, wire_map in [(wire_1, wire_1_map),(wire_2, wire_2_map)]:
        x = 0
        y = 0
        count = 0
        for step in wire:
            for i in range(int(step[1:])):
                offset = direction_map[step[0]]
                x += offset[0]
                y += offset[1]
                count += 1
                wire_map[(x, y)] = count

    wire_cross = wire_1_map.keys() & wire_2_map.keys()
    closest = min([y for y in wire_cross], key=lambda x: abs(x[0]) + abs(x[1]))
    man_distance = abs(closest[0]) + abs(closest[1])
    print("Manhattan distance:   ", man_distance)

    # Part 2:
    least_steps = min(wire_cross, key=lambda x: wire_1_map[x] + wire_2_map[x])
    steps = wire_1_map[least_steps] + wire_2_map[least_steps]
    print("Fewest combined steps:",steps)
