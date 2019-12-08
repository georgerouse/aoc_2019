from itertools import permutations
from copy import copy


def get_diagnostic_code(input_list, i, list_of_inputs, logging=False):
    returned_value = None
    while True:
        op_code = input_list[i]
        mode_1 = int(op_code / 100) % 10
        mode_2 = int(op_code / 1000) % 10
        mode_3 = int(op_code / 10000) % 10
        op_code = op_code % 100

        if op_code == 99:
            break

        value_1 = i+1 if mode_1 == 1 else input_list[i+1]
        value_2 = i+2 if mode_2 == 1 else input_list[i+2]
        try:
            value_3 = i+3 if mode_3 == 1 else input_list[i+3]
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

        elif op_code == 4:
            returned_value = input_list[value_1]
            if logging:
                print("op_code 4: " + str(returned_value))
            i += 2
            break

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

        else:
            print("INVALID OP CODE: " + str(op_code))
            break
    return input_list, i, list_of_inputs, returned_value


if __name__ == '__main__':
    # Get the input data
    with open('input/day_07.txt') as f:
        file_data = f.read()
    original_list = [int(x) for x in file_data.split(',')]

    # Part 1:
    result = 0
    for permu in permutations([0, 1, 2, 3, 4]):
        initial_amp = 0
        for phase_setting in permu:
            input_list = original_list.copy()
            initial_amp = get_diagnostic_code(input_list, 0, [phase_setting, initial_amp])[-1]
        result = max(result, initial_amp)
    print("Highest signal: " + str(result))

    # Part 2:
    result = 0
    for permu in permutations([5, 6, 7, 8, 9]):
        regs = []
        inps = []
        for x in range(5):
            regs.append(copy(original_list))
            inps.append([permu[x]])
        zero_list = [0, 0, 0, 0, 0]
        initial_amp = 0
        while initial_amp is not None:
            for x in range(5):
                inps[x].append(initial_amp)
                regs[x], zero_list[x], inps[x], initial_amp = get_diagnostic_code(regs[x], zero_list[x], inps[x])
            if initial_amp is None:
                last_amp = last_amp
            else:
                last_amp = initial_amp
        result = max(result, last_amp)
    print("Highest signal: " + str(result))
