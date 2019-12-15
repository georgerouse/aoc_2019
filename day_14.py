from collections import defaultdict
import math

class ChemicalReaction:
    def __init__(self, inputs=None, output=None):
        if inputs is None:
            self.inputs = []
        self.output = output


class Chemical:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


def calculate_required_ore(name, needed, producing):
    reaction = reaction_dict[name]
    output_chemical = reaction.output
    count = math.ceil(max(0, needed[output_chemical.name] - producing[output_chemical.name]) / output_chemical.amount)
    producing[output_chemical.name] += count * output_chemical.amount
    for input_chemical in reaction.inputs:
        needed[input_chemical.name] += count * input_chemical.amount

    for input_chemical in reaction.inputs:
        if input_chemical.name != "ORE":
            calculate_required_ore(input_chemical.name, needed, producing)


if __name__ == '__main__':
    # Get the input data
    with open('input/day_14.txt') as f:
        file_data = f.readlines()

    # Format input data into a list of reactions
    reaction_dict = {}
    for line in file_data:
        reaction = ChemicalReaction()
        inputs, output = line.split("=>")
        output_number, output_name = output.strip().split(" ")
        reaction.output = Chemical(output_name, int(output_number))
        for input_chemical in inputs.split(","):
            input_chemical = input_chemical.strip()
            input_number, input_name = input_chemical.split(" ")
            reaction.inputs.append(Chemical(input_name, int(input_number)))
        reaction_dict[output_name] = reaction

    # Part 1:
    needed = defaultdict(int)
    needed["FUEL"] = 1
    producing = defaultdict(int)
    calculate_required_ore("FUEL", needed, producing)
    print("Minimum amount of ORE:  " + str(needed["ORE"]))

    # Part 2:
    fuel_to_produce = 0
    fuel_increment = 1
    getting_closer = False
    calculating = True

    while calculating:
        needed.clear()
        producing.clear()
        needed["FUEL"] = fuel_to_produce

        calculate_required_ore("FUEL", needed, producing)

        if needed["ORE"] > 1000000000000:
            getting_closer = True
            fuel_increment = max(1, fuel_increment // 2)
            fuel_to_produce -= fuel_increment

        elif not getting_closer:
            fuel_increment *= 2
            fuel_to_produce += fuel_increment

        else:
            if fuel_increment == 1:
                calculating = False
            else:
                fuel_to_produce += fuel_increment

    print("Maximum amount of FUEL: " + str(fuel_to_produce))
