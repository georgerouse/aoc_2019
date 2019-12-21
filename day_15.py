import networkx as nx
import matplotlib.pyplot as plt
import random
from intcode import int_code
from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length < other.length

    def __hash__(self):
        return hash(tuple((self.x, self.y)))

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def neighbours(self):
        return [self + p for p in robot_directions]

robot_directions = [
    Point(0, 1),   # north
    Point(0, -1),  # south
    Point(-1, 0),  # west
    Point(1, 0),   # east
]

if __name__ == '__main__':
    # Get the input data
    with open('input/day_15.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]

    global_inputs = [0]
    maze_area = {}
    oxygen = None
    runner = int_code(input_list, 0, global_inputs)
    oxygen_found = False
    paths = []
    print('Looking for oxygen...')
    try:
        curr = Point(0, 0)
        for j in range(1000000):
            print(j)
            facing = random.choice(range(4))
            while maze_area.get(curr + robot_directions[facing], 1) == 0:
                facing = random.choice(range(4))

            global_inputs[0] = facing + 1
            result = next(runner)

            if result == 0:
                maze_area[curr + robot_directions[facing]] = 0

            elif result == 1:
                source_pos = (curr.x, curr.y)
                curr += robot_directions[facing]
                target_pos = (curr.x, curr.y)
                maze_area[curr] = 1
                if (source_pos, target_pos) not in paths:
                    paths.append((source_pos, target_pos))

            elif result == 2:
                source_pos = (curr.x, curr.y)
                curr += robot_directions[facing]
                target_pos = (curr.x, curr.y)
                if (source_pos, target_pos) not in paths:
                    paths.append((source_pos, target_pos))
                oxygen = curr
                maze_area[curr] = 2
                oxygen_found = True

            # Added the below to make Part 1 quicker but gave me a partially mapped maze
            # if oxygen_found:
            #    break

    except StopIteration:
        pass

    assert 2 in maze_area.values()  # Check we've found it

    # Use networkx to find shortest path
    graph = nx.Graph()

    # Add nodes
    oxygen_node_id = None
    start_node_id = None
    for i, coords in enumerate(maze_area.items()):
        if coords[1] in [1, 2]:
            graph.add_node(i, pos=(coords[0].x, coords[0].y))
        if (coords[0].x, coords[0].y) == (oxygen.x, oxygen.y):
            oxygen_node_id = i
        if (coords[0].x, coords[0].y) == (0, 0):
            start_node_id = i

    pos = nx.get_node_attributes(graph, 'pos')

    # Add edges/paths
    for source, target in paths:
        for key, value in pos.items():
            if value == source:
                source_id = key
            if value == target:
                target_id = key
        graph.add_edge(source_id, target_id)

    # Section for printing to help debug...
    labels = {k: str(v) for k, v in pos.items()}
    nx.draw(graph, pos, node_size=10, font_size=7)
    nx.draw_networkx_labels(graph, pos, labels, font_size=5)
    plt.show()

    shortest_path = nx.shortest_path(graph, start_node_id, oxygen_node_id)
    print('Optimal movement to oxygen:', len(shortest_path) - 1)

    # Part 2:
    minutes = 0
    done = {(oxygen.x, oxygen.y)}
    oxygen_tracker = [(oxygen.x, oxygen.y)]
    while oxygen_tracker:
        void = []
        for coords in oxygen_tracker:
            for adjescent in [x[0] for x in paths if x[1] == coords]:
                if adjescent in done:
                    continue
                done.add(adjescent)
                void.append(adjescent)
        oxygen_tracker = void
        minutes += 1
    print('Minutes to fill with oxygen:', str(minutes - 1))
    
