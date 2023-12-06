from itertools import combinations_with_replacement
from functools import reduce

# Time:      7  15   30
# Distance:  9  40  200

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    input = zip([int(n) for n in lines[0].split()[1:]], [int(n) for n in lines[1].split()[1:]])

    results = []
    for time, disntance in input:
        numbers = list(range(1, time + 1))
        combinations = [
            combi for combi in combinations_with_replacement(numbers, 2)
            if combi[0] * combi[1] >= disntance + 1 and sum(combi) == time
        ]
        res = len(combinations) * 2
        for r in combinations:
            if r[0] == r[1]:
                res -= 1
        results.append(res)
    
    print(reduce(lambda x, y: x * y, results))
    