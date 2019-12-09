def get_diagnostic_code(input_list, i, list_of_inputs, logging=False):
    returned_value = None
    relative_base = 0
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

        elif op_code == 9:
            relative_base += input_list[value_1]
            i += 2

        else:
            print("INVALID OP CODE: " + str(op_code))
            break
    return returned_value

if __name__ == '__main__':
    # Get the input data
    with open('input/day_09.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]

    # Part 1:
    result = get_diagnostic_code(input_list, 0, [1], False)
    print("Result: " + str(result))

    # Part 2:
    result = get_diagnostic_code(input_list, 0, [2], False)
    print("Coordinates: " + str(result))
    
