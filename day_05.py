def get_diagnostic_code(input_list, input_value):
    i = 0
    returned_value = None
    while True:
        op_code = input_list[i]
        mode_1 = int(op_code / 100) % 10
        mode_2 = int(op_code / 1000) % 10
        mode_3 = int(op_code / 10000) % 10
        op_code = op_code % 100

        value_1 = i+1 if mode_1 == 1 else input_list[i+1]
        value_2 = i+2 if mode_2 == 1 else input_list[i+2]
        value_3 = i+3 if mode_3 == 1 else input_list[i+3]

        if op_code == 99:
            break

        elif op_code == 1:
            input_list[value_3] = input_list[value_1] + input_list[value_2]
            i += 4

        elif op_code == 2:
            input_list[value_3] = input_list[value_1] * input_list[value_2]
            i += 4

        elif op_code == 3:
            input_list[value_1] = input_value
            i += 2

        elif op_code == 4:
            returned_value = input_list[value_1]
            print("op_code 4: " + str(returned_value))
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

        else:
            print("INVALID OP CODE: " + str(op_code))
            break
    return returned_value

if __name__ == '__main__':
    # Get the input data
    with open('input/day_05.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]
    second_list = input_list.copy()

    result = get_diagnostic_code(input_list, 1)
    print("Diagnostic code, part 1: " + str(result))

    result = get_diagnostic_code(second_list, 5)
    print("Diagnostic code, part 2: " + str(result))
