def update_velocities(moon_dict):
    for current_moon_name, current_value in moon_dict.items():
        for moon_name, other_value in moon_dict.items():
            if current_moon_name == moon_name:
                break
            else:
                for direction in ["x", "y", "z"]:
                    if current_value["pos"][direction] > other_value["pos"][direction]:
                        current_value["vel"][direction] -= 1
                        other_value["vel"][direction] += 1
                    elif current_value["pos"][direction] < other_value["pos"][direction]:
                        current_value["vel"][direction] += 1
                        other_value["vel"][direction] -= 1
    return moon_dict


def apply_velocity(moon_dict):
    for moon_name, dict_value in moon_dict.items():
        for direction in ["x", "y", "z"]:
            moon_dict[moon_name]["pos"][direction] = moon_dict[moon_name]["pos"][direction] + moon_dict[moon_name]["vel"][direction]
    return moon_dict


def print_moon_dict(moon_dict):
    for moon_name, value in moon_dict.items():
        print(moon_name.ljust(10, ' '), "pos:",
            "x=", str(value["pos"]["x"]).rjust(4, ' ') + ',',
            "y=", str(value["pos"]["y"]).rjust(4, ' ') + ',',
            "z=", str(value["pos"]["z"]).rjust(4, ' ') + ',',
            "vel:",
            "x=", str(value["vel"]["x"]).rjust(4, ' ') + ',',
            "y=", str(value["vel"]["y"]).rjust(4, ' ') + ',',
            "z=", str(value["vel"]["z"]).rjust(4, ' '))
    print("\n")


def calculate_and_print_total_energy(moon_dict):
    energey_dict = {}
    for moon_name, value in moon_dict.items():
        pot_energy = sum([abs(x) for x in value['pos'].values()])
        kin_energy = sum([abs(x) for x in value['vel'].values()])
        energey_dict[moon_name] = pot_energy * kin_energy

    total_energy = sum(energey_dict.values())
    print("Total energy in the system: " + str(total_energy))


def least_common_multiple(x, y):
    a, b = x, y
    while a:
        a, b = b % a, a
    return x // b * y


if __name__ == '__main__':
    # Get the input data
    with open('input/day_12.txt') as f:
        file_data = f.read()

    # Process input data
    input_list = [x.replace('<','').replace('>','') for x in file_data.split('\n')]
    input_list = [x.replace('x=','').replace('y=','').replace('z=','') for x in input_list]
    input_list = [x.split(',') for x in input_list]
    moon_dict = {}
    moon_names = ['Io', 'Europa', 'Ganymede', 'Callisto']
    for i, item in enumerate(input_list):
        values = {"x": int(item[0]), "y": int(item[1]), "z": int(item[2])}
        moon_dict[moon_names[i]] = {"pos": values, "vel": {"x": 0, "y": 0, "z": 0}}

    # Part 1:
    print_part_1 = False
    if print_part_1:
        print("After 0 steps:")
        print_moon_dict(moon_dict)
    counter = 1
    while counter <= 1000:
        moon_dict = update_velocities(moon_dict)
        moon_dict = apply_velocity(moon_dict)
        if print_part_1:
            print(f"After {counter} steps:")
            print_moon_dict(moon_dict)
        counter += 1
    calculate_and_print_total_energy(moon_dict)

    # Process input data
    input_list = [x.replace('<','').replace('>','') for x in file_data.split('\n')]
    input_list = [x.replace('x=','').replace('y=','').replace('z=','') for x in input_list]
    input_list = [x.split(',') for x in input_list]
    moon_dict = {}
    moon_names = ['Io', 'Europa', 'Ganymede', 'Callisto']
    for i, item in enumerate(input_list):
        values = {"x": int(item[0]), "y": int(item[1]), "z": int(item[2])}
        moon_dict[moon_names[i]] = {"pos": values, "vel": {"x": 0, "y": 0, "z": 0}}

    # Part 2:
    x_set = set()
    y_set = set()
    z_set = set()
    found = False
    # Insert initial position
    x_list = []
    y_list = []
    z_list = []
    for moon_name, value in moon_dict.items():
        x_tuple = (moon_dict[moon_name]["pos"]["x"], moon_dict[moon_name]["vel"]["x"])
        x_list.append(x_tuple)
        y_tuple = (moon_dict[moon_name]["pos"]["y"], moon_dict[moon_name]["vel"]["y"])
        y_list.append(y_tuple)
        z_tuple = (moon_dict[moon_name]["pos"]["z"], moon_dict[moon_name]["vel"]["z"])
        z_list.append(z_tuple)
    x_set.add(tuple(x_list))
    y_set.add(tuple(y_list))
    z_set.add(tuple(z_list))

    while not found:
        moon_dict = update_velocities(moon_dict)
        moon_dict = apply_velocity(moon_dict)
        # Record positions
        x_list = []
        y_list = []
        z_list = []
        for moon_name, value in moon_dict.items():
            x_tuple = (moon_dict[moon_name]["pos"]["x"], moon_dict[moon_name]["vel"]["x"])
            x_list.append(x_tuple)
            y_tuple = (moon_dict[moon_name]["pos"]["y"], moon_dict[moon_name]["vel"]["y"])
            y_list.append(y_tuple)
            z_tuple = (moon_dict[moon_name]["pos"]["z"], moon_dict[moon_name]["vel"]["z"])
            z_list.append(z_tuple)

        if tuple(x_list) in x_set and tuple(y_list) in y_set and tuple(z_list) in z_set:
            found = True
        else:
            x_set.add(tuple(x_list))
            y_set.add(tuple(y_list))
            z_set.add(tuple(z_list))

    result = least_common_multiple(len(x_set), least_common_multiple(len(y_set), len(z_set)))
    print("Number of steps: " + str(result))
