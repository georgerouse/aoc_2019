from collections import Counter

def print_image(flat_list, image_size):
    for i in range(0, len(flat_list), image_size[0]):
        line_string = ''
        layer = flat_list[i:i + image_size[0]]
        for item in layer:
            if item == '1':
                line_string += u"\u2588"
            else:
                line_string += " "
        print(line_string)

if __name__ == '__main__':
    # Get the input data
    with open('input/day_08.txt') as f:
        file_data = f.read()
    input_list = [x for x in file_data]

    # Part 1:
    image_size = (25, 6)
    layer_size = image_size[0] * image_size[1]
    result = {}
    layer_count = 0
    min_0_layer = None
    layer_list = []
    for i in range(0, len(input_list), layer_size):
        layer = input_list[i:i + layer_size]
        layer_list.append(layer)
        result[layer_count] = Counter(layer)
        if min_0_layer is None:
            min_0_layer = layer_count
        else:
            if result[layer_count]['0'] < result[min_0_layer]['0']:
                min_0_layer = layer_count
        layer_count += 1

    result = result[min_0_layer]['1'] * result[min_0_layer]['2']
    print("Digits multiplied: " + str(result))

    # Part 2:
    flat_list = [None] * layer_size
    for list_num in range(0, len(layer_list[0])):
        for layer_num in range(0, len(layer_list)):
            if layer_list[layer_num][list_num] == '1':
                if flat_list[list_num] is None:
                    flat_list[list_num] = '1'
                else:
                    break
            elif layer_list[layer_num][list_num] == '0':
                if flat_list[list_num] is None:
                    flat_list[list_num] = '0'
                else:
                    break
            else:
                pass
    print("Message:")
    print_image(flat_list, image_size)
