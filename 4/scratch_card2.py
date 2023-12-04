import re


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

pattern = r'Card\s*\d+:\s*'
result = 0
precalculated_cards = {}


def calculate_card(card_number: int, lines: list) -> int:
    if res_calc := precalculated_cards.get(card_number):
        return res_calc
    else:
        card_result = 1
        numbers_found = 0

        winning_numbers, checking_numbers = lines[card_number].split(" | ")
        
        winning_numbers = winning_numbers.split(" ")
        checking_numbers = checking_numbers.split(" ")

        for winning_number in winning_numbers:
            if winning_number in checking_numbers:
                numbers_found += 1
        
        if numbers_found:
            for i in range(1, numbers_found + 1):
                card_result += calculate_card(card_number + i, lines)

        precalculated_cards[card_number] = card_result
        
    return card_result



with open('input.txt', 'r') as f:
    content = f.read()
    clean_content = re.sub(pattern, '', content)
    clean_content = clean_content.replace("  ", " ")
    lines = clean_content.splitlines()

    for i, line in enumerate(lines):
        result += calculate_card(card_number=i, lines=lines)
    
print(result)
