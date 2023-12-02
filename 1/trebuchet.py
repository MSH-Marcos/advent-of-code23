
result = 0
with open('input.txt') as f:
    for line in f:
        numbers = [letter for letter in line if letter.isdigit()]
        if len(numbers)> 1:
            result += int(f"{numbers[0]}{numbers[-1]}")
        else:
            result += int(f"{numbers[0]}{numbers[0]}")
print(result)
