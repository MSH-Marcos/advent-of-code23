import re

# Time:      71530
# Distance:  940200

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))

    result = 0
    even = 0
        
    start_low = (time // 2)
    start_up = (time // 2) + (time % 2)

    if start_low == start_up:
        even = 1
    match = True

    while match:
        if start_low * start_up > distance:
            result += 1
            start_low -= 1
            start_up += 1
        else:
            match = False
    
    print(result * 2 - even)

