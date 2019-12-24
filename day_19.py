from intcode import int_code

if __name__ == '__main__':
    logging = False
    # Get the input data
    with open('input/day_19.txt') as f:
        file_data = f.read()
    program_list = [int(x) for x in file_data.split(',')]
    orig_list = program_list.copy()

    # Part 1:
    grid_size = 50
    canvas = []
    logging = False
    count = 0
    for y in range(grid_size):
        row = []
        for x in range(grid_size):
            program_list = orig_list.copy()
            input_list = [x, y]
            runner = int_code(program_list, 0, input_list)
            value = next(runner)
            row.append(value)
            if value == 1:
                count += 1
        canvas.append(row)
    if logging:
        for row in canvas:
            print(''.join([str(x) for x in row]))
    print("Number of points affected:", count)

    # Part 2:
    x = 0
    for y in range(100, 100000):
        in_beam = False
        while not in_beam:
            input_list = [x, y]
            program_list = orig_list.copy()
            runner = int_code(program_list, 0, input_list)
            value = next(runner)
            if value == 1:
                in_beam = True
            else:
                x += 1
        if logging:
            print("x:",x)
        input_list = [x + 99, y - 99]
        program_list = orig_list.copy()
        runner = int_code(program_list, 0, input_list)
        value = next(runner)
        if value == 1:
            return_value = (10000 * x) + (y-99)
            break
    print("Coordinate code:", return_value)
    
