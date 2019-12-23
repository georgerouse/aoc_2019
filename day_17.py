from intcode import int_code

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return('({x}, {y})'.format(x=self.x, y=self.y))

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def get_new_direction(robot_facing, robot_loc, canvas):
    new_facing = None
    try:
        if robot_facing == NORTH and canvas[robot_loc.y][robot_loc.x+1] == '#':
            new_facing = EAST
            turn_instruction = 'R'
    except:
        pass
    try:
        if robot_facing == NORTH and canvas[robot_loc.y][robot_loc.x-1] == '#':
            new_facing = WEST
            turn_instruction = 'L'
    except:
        pass
    try:
        if robot_facing == SOUTH and canvas[robot_loc.y][robot_loc.x+1] == '#':
            new_facing = EAST
            turn_instruction = 'L'
    except:
        pass
    try:
        if robot_facing == SOUTH and canvas[robot_loc.y][robot_loc.x-1] == '#':
            new_facing = WEST
            turn_instruction = 'R'
    except:
        pass
    try:
        if robot_facing == WEST and canvas[robot_loc.y-1][robot_loc.x] == '#':
            new_facing = NORTH
            turn_instruction = 'R'
    except:
        pass
    try:
        if robot_facing == WEST and canvas[robot_loc.y+1][robot_loc.x] == '#':
            new_facing = SOUTH
            turn_instruction = 'L'
    except:
        pass
    try:
        if robot_facing == EAST and canvas[robot_loc.y-1][robot_loc.x] == '#':
            new_facing = NORTH
            turn_instruction = 'L'
    except:
        pass
    try:
        if robot_facing == EAST and canvas[robot_loc.y+1][robot_loc.x] == '#':
            new_facing = SOUTH
            turn_instruction = 'R'
    except:
        pass

    if new_facing is None:
        return new_facing, ''
    else:
        return new_facing, turn_instruction

def get_distance_and_loc(robot_facing, robot_loc, canvas):
    distance_count = 0
    hit_end = False
    if robot_facing in [NORTH, SOUTH]:
        robot_facing = {NORTH:SOUTH, SOUTH:NORTH}.get(robot_facing)
    new_loc = robot_loc + robot_facing
    while not hit_end:
        try:  # Hack to handle the fact that there are paths at the canvas edge
            if canvas[new_loc.y][new_loc.x] in ['#', 'O']:
                distance_count += 1
                new_loc = new_loc + robot_facing
            else:
                new_loc = new_loc - robot_facing
                hit_end = True
        except:
            new_loc = new_loc - robot_facing
            hit_end = True
    return distance_count, new_loc

NORTH = Point(0, 1)
SOUTH = Point(0, -1)
WEST = Point(-1, 0)
EAST = Point(1, 0)

if __name__ == '__main__':
    # Get the input data
    with open('input/day_17.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]

    # Part 1:
    # Build up canvas
    canvas = []
    runner = int_code(input_list, 0, [])
    row_list = []
    done = False
    while not done:
        result = next(runner)
        if result == 35:
            row_list.append('#')
        elif result == 46:
            row_list.append('.')
        elif result == 10:
            if '#' not in row_list:
                done = True
            canvas.append(row_list)
            row_list = []
        elif result == 94:
            row_list.append('^')
    #print_canvas(canvas)

    # Calculate the intersections
    canvas_height = len(canvas)
    canvas_width = len(canvas[0])
    intersections = []
    robot_loc = None
    for i in range(canvas_height):
        for j in range(canvas_width):
            try:
                if canvas[i+1][j] == '#' and canvas[i-1][j] == '#' and canvas[i][j+1] == '#' and canvas[i][j-1] == '#' and canvas[i][j] == '#':
                    intersections.append((i, j))
                    canvas[i][j] = 'O'
                if canvas[i][j] == '^':
                    robot_loc = Point(j, i)
            except:
                pass
    print("Sum of the alignment parameters:", sum([abs(x[0]*x[1]) for x in intersections]))

    # Part 2:
    logging = False
    robot_facing = NORTH
    instruction_list = []
    new_direction = 0
    while new_direction is not None:
        if logging:
            print(f"robot_facing before: {robot_facing}")
        new_direction, turn_instruction = get_new_direction(robot_facing, robot_loc, canvas)
        if logging:
            print(f"new_direction:    {new_direction}")
        if logging:
            print(f"turn_instruction: {turn_instruction}")
        if new_direction:
            instruction_list.append(turn_instruction)
            robot_facing = new_direction
            if logging:
                print(f"robot_facing after: {robot_facing}")
            distance_to_travel, new_loc = get_distance_and_loc(robot_facing, robot_loc, canvas)
            instruction_list.append(str(distance_to_travel))
            robot_loc = new_loc
            if logging:
                print(f"robot_loc:        {robot_loc}")
        if logging:
            print("instruction_list: " + str(instruction_list))

    '''
    instruction_list:

    'L', '12', 'R', '4', 'R', '4', -- A

    'R', '12', 'R', '4', 'L', '12', -- B
    'R', '12', 'R', '4', 'L', '12', -- B

    'R', '12', 'R', '4', 'L', '6', 'L', '8', 'L', '8', -- C
    'R', '12', 'R', '4', 'L', '6', 'L', '8', 'L', '8', -- C

    'L', '12', 'R', '4', 'R', '4', -- A
    'L', '12', 'R', '4', 'R', '4', -- A

    'R', '12', 'R', '4', 'L', '12',   -- B
    'R', '12', 'R', '4', 'L', '12',   -- B

    'R', '12', 'R', '4', 'L', '6', 'L', '8', 'L', '8' -- C
    '''
    main_movement_routine = ['A', 'B', 'B', 'C', 'C', 'A', 'A', 'B', 'B', 'C']
    main_movement_routine = [x for x in ','.join(main_movement_routine)]
    a_movement = ['L', ',', '1', '2', ',', 'R', ',', '4', ',', 'R', ',', '4']
    b_movement = ['R', ',', '1', '2', ',', 'R', ',', '4', ',', 'L', ',', '1', '2']
    c_movement = ['R', ',', '1', '2', ',', 'R', ',', '4', ',', 'L', ',', '6', ',', 'L', ',', '8', ',', 'L', ',', '8']

    full_inputs = main_movement_routine + [10] + \
                  a_movement + [10] + \
                  b_movement + [10] + \
                  c_movement + [10] + \
                  ['n'] + [10]

    full_ascii_inputs = [ord(x) if type(x) == str else x for x in full_inputs]

    # Get the input data
    with open('input/day_17.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]
    input_list[0] = 2
    runner = int_code(input_list, 0, full_ascii_inputs)
    outputs = []
    logging = False
    while True:
       try:
           value = next(runner)
           outputs.append(value)
       except:
           break
    if logging:
        print(''.join([chr(x) for x in outputs]))

    print("Dust collected: ", outputs[-1])  # 923017
