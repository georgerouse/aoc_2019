from collections.abc import Iterator

def int_code(program_list, p_id, list_of_inputs, i=0, logging=False):
    if not isinstance(list_of_inputs, Iterator):
        list_of_inputs = iter(list_of_inputs)
    relative_base = 0
    program_list.extend([0] * 10000)  # Add memory

    while i < len(program_list):
        op_code = program_list[i]
        mode_1 = int(op_code / 100) % 10
        mode_2 = int(op_code / 1000) % 10
        mode_3 = int(op_code / 10000) % 10
        op_code = op_code % 100

        if op_code == 99:
            raise StopIteration()

        if mode_1 == 0:
            value_1 = program_list[i+1]
        elif mode_1 == 1:
            value_1 = i+1
        elif mode_1 == 2:
            value_1 = program_list[i+1] + relative_base

        if mode_2 == 1:
            value_2 = i+2
        elif mode_2 == 0:
            value_2 = program_list[i+2]
        elif mode_2 == 2:
            value_2 = program_list[i+2] + relative_base

        try:
            if mode_3 == 1:
                value_3 = i+3
            elif mode_3 == 0:
                value_3 = program_list[i+3]
            elif mode_3 == 2:
                value_3 = program_list[i+3] + relative_base
        except Exception:
            pass

        if op_code == 1:
            program_list[value_3] = program_list[value_1] + program_list[value_2]
            i += 4

        elif op_code == 2:
            program_list[value_3] = program_list[value_1] * program_list[value_2]
            i += 4

        elif op_code == 3:
            program_list[value_1] = next(list_of_inputs)
            i += 2

        elif op_code == 4:
            if logging:
                print(program_list[value_1])
            yield program_list[value_1]
            i += 2

        elif op_code == 5:
            if program_list[value_1] != 0:
                i = program_list[value_2]
            else:
                i += 3

        elif op_code == 6:
            if program_list[value_1] == 0:
                i = program_list[value_2]
            else:
                i += 3

        elif op_code == 7:
            program_list[value_3] = 1 if program_list[value_1] < program_list[value_2] else 0
            i += 4

        elif op_code == 8:
            program_list[value_3] = 1 if program_list[value_1] == program_list[value_2] else 0
            i += 4

        elif op_code == 9:
            relative_base += program_list[value_1]
            i += 2

        else:
            print("INVALID OP CODE: " + str(op_code))
