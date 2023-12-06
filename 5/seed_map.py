from collections import OrderedDict

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

seeds = []
conversion_map = OrderedDict()
actual_mapper = ""
lowest_location = 999999999999999999999999999999999999999

with open('input.txt', 'r') as f:
    content = f.read()
    clean_content = content.replace("\n\n", "\n")
    lines = clean_content.splitlines()

    seeds = [int(numb) for numb in lines.pop(0).split()[1:]] 
    for line in lines:
        if ":" in line:
            actual_mapper = line.split()[0].split("-")[-1]
            conversion_map[actual_mapper] = []
        else:
            conversion_map[actual_mapper].append([int(numb) for numb in line.split()])
    
    for seed in seeds:
        location = seed
        for mapper_lists in conversion_map.values():
            for mapper in mapper_lists:
                if mapper[1] <= location <= (mapper[1] + mapper[2] - 1):
                    location = mapper[0] + location - mapper[1]
                    break
        if location < lowest_location:
            lowest_location = location

print(lowest_location)