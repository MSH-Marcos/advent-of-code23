
from collections import OrderedDict

def count_numbers(line: str):
    numbers = [letter for letter in line if letter.isdigit()]
    if len(numbers)> 1:
        return int(f"{numbers[0]}{numbers[-1]}")
    else:
        return int(f"{numbers[0]}{numbers[0]}")
    
result = 0

numbers = OrderedDict({
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
})


with open('input.txt', 'r') as f:
    content = f.read()
    for number_name, number in numbers.items():
        content = content.replace(number_name, number)
    
    lines = content.splitlines()

    for line in lines:
        result += count_numbers(line)

print(result)