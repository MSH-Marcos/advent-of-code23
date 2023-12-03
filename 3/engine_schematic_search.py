import re

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

set_to_exclude = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"}

result = 0

with open('input.txt') as f:
    index_numbers_last_row = []
    special_character_index_last_row = []

    for line in f:
        index_numbers = []
        special_character_indexes = []
        index_numbers_temp_list = []
        digit_string = ""

        for i, char in enumerate(line):
            if char not in set_to_exclude:
                special_character_indexes.append(i - 1)
                special_character_indexes.append(i)
                special_character_indexes.append(i + 1)
            
            if char.isdigit():
                digit_string += char
                index_numbers_temp_list.append(i)
            elif digit_string:
                index_numbers.append([index_numbers_temp_list, int(digit_string), False])
                digit_string = ""
                index_numbers_temp_list = []

        sum_indexes = special_character_indexes + special_character_index_last_row
        numbers_to_check = index_numbers + index_numbers_last_row

        for i, values in enumerate(numbers_to_check):
            for ind in values[0]:
                if ind in sum_indexes and not values[2]:
                    result += values[1]
                    numbers_to_check[i][2] = True

        index_numbers_last_row = index_numbers
        special_character_index_last_row = special_character_indexes   

    print(result)
