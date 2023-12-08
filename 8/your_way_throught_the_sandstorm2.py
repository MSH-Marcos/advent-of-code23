import math
from collections import defaultdict

# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)


with open('input.txt', 'r') as f:
    result = 0
    end = "ZZZ"

    content = f.read()
    content = content.replace(",", "")
    content = content.replace("(", "")
    content = content.replace(")", "")

    lines = content.splitlines()

    instructions = lines.pop(0)
    instructions = [0 if char == "L" else 1 for char in instructions]

    lines.pop(0)

    map_dict = {}

    for line in lines:
        line_to_search = line.split(" = ")
        tuple_to_add = line_to_search[1].split()

        map_dict[line_to_search[0]] = (tuple_to_add[0], tuple_to_add[1])
    
    searching = True
    iter = 0
    to_search_list = [el for el in map_dict.keys() if el.endswith('A')]
    results_dict = defaultdict(list)
    count = {}
    while searching:
        if iter == len(instructions):
            iter = 0
        for i, path in enumerate(to_search_list):
            to_search_list[i] = map_dict[path][instructions[iter]]
        iter += 1
        result += 1

        for j, path_to_check in enumerate(reversed(to_search_list)):
            if path_to_check.endswith('Z'):
                if not results_dict.get(j):
                    results_dict[j] = result
                else:
                    results_dict[j] = result - results_dict[j]
                    count[j] = True

        if len(count) == len(to_search_list):
            searching = False

    result = math.lcm(*results_dict.values())
    
print(result)