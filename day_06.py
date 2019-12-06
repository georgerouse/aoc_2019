# req: pip install anytree==2.7.2
from anytree import Node, RenderTree, AsciiStyle, LevelOrderIter
from anytree import search, walker

def build_tree(input_list, root):
    while input_list:
        print("Items left to process: " + str(len(input_list)))
        for i, item in enumerate(input_list):
            parent = item.split(')')[0]
            child = item.split(')')[1] # is in orbit around

            if parent == 'COM':
                new_node = Node(child, parent=root)
                input_list.pop(i)

            else:
                results = search.findall(root, filter_=lambda node: node.name in (parent))
                if len(results) == 1:
                    new_node = Node(child, parent=results[0])
                    input_list.pop(i)
    return root


def get_orbits(tree):
    orbits = 0
    for node in LevelOrderIter(tree):
        orbits += node.depth
    return orbits


if __name__ == '__main__':
    # Get the input data
    with open('input/day_06.txt') as f:
        file_data = f.read()
    input_list = [x for x in file_data.split('\n')]

    # Build the tree
    root = Node("COM")
    tree = build_tree(input_list, root)

    # print(RenderTree(tree, style=AsciiStyle()).by_attr())
    # Part 1:
    print("Total number of direct and indirect orbits: " + str(get_orbits(tree)))

    # Part 2:
    w = walker.Walker()
    you = search.findall(root, filter_=lambda node: node.name in ('YOU'))
    you_orbit = you[0].parent
    santa = search.findall(root, filter_=lambda node: node.name in ('SAN'))
    santa_orbit = santa[0].parent
    upwards, common, downwards = w.walk(you_orbit, santa_orbit)
    print("Minimum number of orbital transfers: " + str(len(upwards) + len(downwards)))
