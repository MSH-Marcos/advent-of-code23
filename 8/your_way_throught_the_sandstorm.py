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
    to_search = "AAA"

    while searching:
        if iter == len(instructions):
            iter = 0
        to_search = map_dict[to_search][instructions[iter]]
        iter += 1
        result += 1

        if to_search == end:
            searching = False

print(result)