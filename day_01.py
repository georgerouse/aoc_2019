def fuel_required(mass):
    return int((mass/3.0) - 2)

if __name__ == '__main__':
    # Get the input data
    with open('input/day_01.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split('\n')]

    # Calculate fuel v1
    print("Sum of the fuel requirements:", sum([fuel_required(x) for x in input_list]))

    # Calculate fuel v2
    fuel_list = []
    for input in input_list:
        while input > 0:
            input = fuel_required(input)
            if input > 0:
                fuel_list.append(input)
    print("Sum of the total fuel requirements:", sum(fuel_list))
