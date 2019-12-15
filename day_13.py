from collections.abc import Iterator

def get_diagnostic_code(input_list, list_of_inputs, logging=False):
    if not isinstance(list_of_inputs, Iterator):
        list_of_inputs = iter(list_of_inputs)
    input_list.extend([0] * 10000)
    i = 0
    relative_base = 0

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
            input_list[value_1] = next(list_of_inputs)
            i += 2
        elif op_code == 4:
            value = input_list[value_1]
            if logging:
                print(value)
            yield value
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

def initalise_game_board(game_runner, board_size):
    global board, score
    for _ in range(board_size + 1):
        x = next(game_runner)
        y = next(game_runner)
        value = next(game_runner)
        if (x, y) == (-1, 0):
            score = value
        else:
            game_board[x, y] = value


def move_joystick():
    global game_board
    ball = [k for k, v in game_board.items() if v == 4][0][0]
    paddle = [k for k, v in game_board.items() if v == 3][0][0]
    if paddle < ball:
        return 1
    elif paddle > ball:
        return -1
    return 0


def update_board(game_runner):
    global score
    value = None
    while value != 4:
        try:
            x = next(game_runner)
        except StopIteration:
            break
        y = next(game_runner)
        value = next(game_runner)
        if (x, y) == (-1, 0):
            score = value
        else:
            game_board[x, y] = value


if __name__ == '__main__':
    # 0 empty tile
    # 1 wall tile
    BLOCK_TILES = 2
    # 3 horizontal paddle tile
    # 4 ball tile

    # Get the input data
    with open('input/day_13.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]

    # Part 1:
    global game_board
    game_board = {}
    game_runner = get_diagnostic_code(input_list, [])
    for x in game_runner:
        y = next(game_runner)
        value = next(game_runner)
        game_board[x, y] = value
    print('Number of block tiles:', list(game_board.values()).count(BLOCK_TILES))

    # Part 2:
    board_size = len(game_board)
    inputs = []
    game_runner = get_diagnostic_code([2] + input_list[1:], inputs)
    initalise_game_board(game_runner, board_size)
    while True:
        if list(game_board.values()).count(2) == 0:
            break
        inputs.append(move_joystick())
        update_board(game_runner)

    print('Final score:' + str(score))
