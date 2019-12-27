from itertools import cycle, islice, chain, repeat

def keep_last_digit(number):
    return int(str(number)[-1])


def calc_list(input_list):
    base_pattern = [0, 1, 0, -1]
    return_list = []
    for i in range(1, len(input_list)+1):
        pattern = list(chain.from_iterable(repeat(x, i) for x in base_pattern))
        pattern = list(islice(cycle(pattern), len(input_list)+1))
        pattern = pattern[1:]
        multiplied_list = [a * b for a, b in zip(input_list, pattern)]
        value = sum(multiplied_list)
        value = keep_last_digit(value)
        return_list.append(value)
    return return_list


if __name__ == '__main__':
    logging = False
    # Get the input data
    with open('input/day_16.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data]

    # Part 1:
    phase_num = 0
    while phase_num < 100:
        input_list = calc_list(input_list)
        phase_num += 1
        if logging:
            print(phase_num, ':', ''.join([str(x) for x in input_list]))
    print("Part 1 answer:", ''.join([str(x) for x in input_list])[0:8])
