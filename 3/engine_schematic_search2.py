import re
from functools import reduce

# 467..114..
# ...*......
# ..35*.633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# sacar indices de caracteres especiales
# sacar indices y numeros enteros de los numeros

result = 0

with open('input.txt') as f:
    index_numbers_last_row = []
    special_character_index_last_row = {}

    for line in f:
        index_numbers = []
        special_character_indexes = {}
        index_numbers_temp_list = []
        digit_string = ""

        for i, char in enumerate(line):
            if char == "*":
                special_character_indexes[i] = []
            
            if char.isdigit():
                digit_string += char
                index_numbers_temp_list.append(i)
                index_numbers_temp_list.append(i + 1)
                index_numbers_temp_list.append(i - 1)
            elif digit_string:
                index_numbers.append((index_numbers_temp_list, int(digit_string)))
                digit_string = ""
                index_numbers_temp_list = []


        for i, numbers in special_character_index_last_row.items():
            for indexes_with_number, number in index_numbers:
                if i in indexes_with_number:
                    numbers.append(number)
                    continue

        for i, numbers in special_character_indexes.items():
            for indexes_with_number, number in index_numbers:
                if i in indexes_with_number:
                    numbers.append(number)
                    continue

            for indexes_with_number, number in index_numbers_last_row:
                if i in indexes_with_number:
                    numbers.append(number)
                    continue

        for i, numbers in special_character_index_last_row.items():
            if len(numbers) > 1:
                result += reduce(lambda x, y: x * y, numbers)

        special_character_index_last_row = special_character_indexes   
        index_numbers_last_row = index_numbers

    print(result)
