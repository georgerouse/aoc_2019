def print_eris(bug_list):
    for row in bug_list:
        print(''.join(row))
    print('\n')

def lifecycle_bugs(input_list):
    grid_size = len(input_list[0])
    output_list = []
    for y in range(grid_size):
        row_list = []
        for x in range(grid_size):
            if input_list[y][x] == '#':
                bug_count = 0
                for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    try:
                        if y + y_offset >= 0 and x + x_offset >= 0:
                            if input_list[y+y_offset][x+x_offset] == '#':
                                bug_count += 1
                    except:
                        pass
                if bug_count == 1:
                    row_list.append('#')
                else:
                    row_list.append('.')
            elif input_list[y][x] == '.':
                bug_count = 0
                for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    try:
                        if y + y_offset >= 0 and x + x_offset >= 0:
                            if input_list[y + y_offset][x + x_offset] == '#':
                                bug_count += 1
                    except:
                        pass
                if (bug_count == 1) or (bug_count == 2):
                    row_list.append('#')
                else:
                    row_list.append('.')
            else:
                print("BROKEN")
        output_list.append(row_list)
    return output_list

def calc_biodiversity_rating(new_bug_layout):
    grid_size = len(new_bug_layout[0])
    powers = []
    x = 1
    i = 1
    while i <= (grid_size * grid_size):
        powers.append(x)
        x *= 2
        i += 1

    flat_list = [item for sublist in new_bug_layout for item in sublist]
    indexes = [i for i, x in enumerate(flat_list) if x == "#"]
    result = 0
    for index in indexes:
        result += powers[index]
    return result

if __name__ == '__main__':
    # Get the input data
    with open('input/day_24.txt') as f:
        input = f.read()
    bug_layout = [[y for y in x.strip()] for x in input.split('\n')]
    i = 0
    layout_list = []
    dupe = False
    while not dupe:
        new_bug_layout = lifecycle_bugs(bug_layout)
        bug_layout = new_bug_layout
        if new_bug_layout not in layout_list:
            layout_list.append(new_bug_layout)
        else:
            dupe = True
        i += 1
    print_eris(new_bug_layout)
    biodiversity_rating = calc_biodiversity_rating(new_bug_layout)
    print("Biodiversity rating:", biodiversity_rating)
    
