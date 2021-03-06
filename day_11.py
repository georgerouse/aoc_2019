UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def print_image(result):
    x_values = [x for (x, y) in result]
    min_x = min(x_values)
    y_values = [y for (x, y) in result]
    min_y = min(y_values)
    canvas_height = max(y_values) - min(y_values)
    canvas_width = max(x_values) - min(x_values)

    # Initialise blank canvas
    row = [None for x in range(canvas_width+1)]
    canvas = [row.copy() for x in range(canvas_height+1)]

    # Paint the canvas
    for (x, y), v in result.items():
        if v == 0:
            canvas[y][x] = u"\u2588"
        else:
            canvas[y][x] = " "

    # Fill None values as "black"
    for row_list in canvas:
        for i, item in enumerate(row_list):
            if item is None:
                row_list[i] = u"\u2588"
        print(''.join(row_list))


def update_robot_position(x_y, direction):
    x = x_y[0]
    y = x_y[1]
    if direction == UP:
        return (x, y-1, direction)
    elif direction == DOWN:
        return (x, y+1, direction)
    elif direction == RIGHT:
        return (x+1, y, direction)
    elif direction == LEFT:
        return (x-1, y, direction)


def get_diagnostic_code(input_list, i, list_of_inputs, logging=False):
    robot_position = (0, 0, UP)
    paint_map = {(0, 0): 0}
    returned_value = None
    relative_base = 0
    instruction_sent = True
    input_list.extend([0] * 2000)  # Add "memory"

    while True:
        op_code = input_list[i]
        mode_1 = int(op_code / 100) % 10
        mode_2 = int(op_code / 1000) % 10
        mode_3 = int(op_code / 10000) % 10
        op_code = op_code % 100

        if op_code == 99:
            break

        if mode_1 == 1:
            value_1 = i+1
        elif mode_1 == 0:
            value_1 = input_list[i+1]
        elif mode_1 == 2:
            value_1 = input_list[i+1] + relative_base

        if mode_2 == 1:
            value_2 = i+2
        elif mode_2 == 0:
            value_2 = input_list[i+2]
        elif mode_2 == 2:
            value_2 = input_list[i+2] + relative_base

        try:
            if mode_3 == 1:
                value_3 = i+3
            elif mode_3 == 0:
                value_3 = input_list[i+3]
            elif mode_3 == 2:
                value_3 = input_list[i+3] + relative_base
        except Exception:
            pass

        if op_code == 1:
            input_list[value_3] = input_list[value_1] + input_list[value_2]
            i += 4

        elif op_code == 2:
            input_list[value_3] = input_list[value_1] * input_list[value_2]
            i += 4

        elif op_code == 3:
            input_list[value_1] = list_of_inputs.pop(0)
            i += 2
            instruction_sent = True

        elif op_code == 4:
            if instruction_sent:
                paint_map[(robot_position[0], robot_position[1])] = input_list[value_1]
                instruction_sent = False
            else:
                new_direction = (robot_position[2] + (1 if input_list[value_1] == 1 else -1)) % 4
                robot_position = update_robot_position(robot_position, new_direction)
                colour = paint_map.get((robot_position[0], robot_position[1]), 0)
                list_of_inputs.append(colour)
            i += 2

        elif op_code == 5:
            if input_list[value_1]:
                i = input_list[value_2]
            else:
                i += 3

        elif op_code == 6:
            if input_list[value_1] == 0:
                i = input_list[value_2]
            else:
                i += 3

        elif op_code == 7:
            if input_list[value_1] < input_list[value_2]:
                input_list[value_3] = 1
            else:
                input_list[value_3] = 0
            i += 4

        elif op_code == 8:
            if input_list[value_1] == input_list[value_2]:
                input_list[value_3] = 1
            else:
                input_list[value_3] = 0
            i += 4

        elif op_code == 9:
            relative_base += input_list[value_1]
            i += 2

        else:
            print("INVALID OP CODE: " + str(op_code))
            break
    return paint_map


if __name__ == '__main__':
    # Get the input data
    with open('input/day_11.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]
    input_list_2 = input_list.copy()

    # Part 1:
    result = get_diagnostic_code(input_list, 0, [0], False)
    print("Painted panels: " + str(len(result)))

    # Part 2:
    result = get_diagnostic_code(input_list_2, 0, [1], False)
    print("Part 2:")
    print_image(result)
