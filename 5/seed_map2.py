from collections import OrderedDict
import copy

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
seed_ranges = []

def get_tuple_intersection(reference_tuple: tuple, check_tuple: tuple, reference_number: int):
    # out
    if check_tuple[0] > reference_tuple[1] or check_tuple[1] < reference_tuple[0]:
        return None, None
    # in
    elif check_tuple[0] >= reference_tuple[0] and check_tuple[1] <= reference_tuple[1]:
        return None, (reference_number - reference_tuple[0] + check_tuple[0], reference_number - reference_tuple[0] + check_tuple[1])
    # partial in in 
    elif reference_tuple[0] > check_tuple[0] and reference_tuple[1] < check_tuple[1]:
        return [(check_tuple[0], reference_tuple[0] - 1), (reference_tuple[1] + 1, check_tuple[1])], (reference_number, reference_number - reference_tuple[0] + reference_tuple[1] ) 
    # partial in upper
    elif check_tuple[0] >= reference_tuple[0]:
       return [(reference_tuple[1] + 1, check_tuple[1])] , (reference_number - reference_tuple[0] + check_tuple[0], reference_number - reference_tuple[0] + reference_tuple[1])
    # partial in lower
    elif check_tuple[1] <= reference_tuple[1]:
        return [(check_tuple[0], reference_tuple[0] - 1)], (reference_number, reference_number - reference_tuple[0] + check_tuple[1] )
    else:
        print('')

with open('input.txt', 'r') as f:
    content = f.read()
    clean_content = content.replace("\n\n", "\n")
    lines = clean_content.splitlines()
    first_line = lines.pop(0).split()[1:]
    for i in range(0, len(first_line), 2):
        seed_ranges.append((int(first_line[i]), int(first_line[i]) + int(first_line[i + 1]) - 1))

    for line in lines:
        if ":" in line:
            actual_mapper = line.split()[0].split("-")[-1]
            conversion_map[actual_mapper] = []
        else:
            map_numbers = [int(numb) for numb in line.split()]
            map_numbers[2] = map_numbers[1] + map_numbers[2] - 1
            conversion_map[actual_mapper].append(map_numbers)
    
    for v in conversion_map.values():
        v.sort(key=lambda x: x[1])

    for seeds in seed_ranges:
        seeds_to_transform = [seeds]
        for mapper_lists in conversion_map.values():
            pending = 0
            repeat = True
            new_segments = []
            new_seeds_to_transform = copy.deepcopy(seeds_to_transform)
            seeds_to_transform = []
            mapper_len = len(mapper_lists)
            while repeat:
                if not new_seeds_to_transform or pending < 0:
                    if pending < 0:
                        repeat = False
                    pending -= 1
                for check_seeds in reversed(new_seeds_to_transform):
                    mapper_len_count = 0
                    for mapper in mapper_lists:
                        discarted_tuples, matched_tuples = get_tuple_intersection(reference_tuple=(mapper[1], mapper[2]), check_tuple=check_seeds, reference_number=mapper[0])
                        if not discarted_tuples and not matched_tuples:
                            mapper_len_count += 1
                            continue
                        if matched_tuples:
                            seeds_to_transform.append(matched_tuples)
                        if discarted_tuples:
                            pending += len(discarted_tuples)
                            new_segments += discarted_tuples
                        new_seeds_to_transform.remove(check_seeds)
                        break
                    if new_segments:
                        new_seeds_to_transform += new_segments
                        new_segments = []
                    elif mapper_len_count == mapper_len:
                        pending -= 1
            if new_seeds_to_transform:
                seeds_to_transform += new_seeds_to_transform

        min_iter = min(tuple_to_check_min[0] for tuple_to_check_min in seeds_to_transform)

        if min_iter < lowest_location:
            lowest_location = min_iter

print(lowest_location)
