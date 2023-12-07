# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

values_dict = {
    "5": 70000000000,
    "4": 60000000000,
    "32": 50000000000,
    "23": 50000000000,
    "3": 40000000000,
    "22": 30000000000,
    "2": 20000000000,
    "": 10000000000
}

char_equivalence = {
    "A": "14", 
    "K": "13", 
    "Q": "12", 
    "J": "11",
    "T": "10", 
    "9": "9", 
    "8": "8",
    "7": "7", 
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2"
}

postion_equivalence = {
    0: "00000000",
    1: "000000",
    2: "0000",
    3: "00",
    4: ""
}

def calculate_hand_score(hand: str) -> int:
    result = 0
    value_of_hand = ""
    for char in set(hand):
        number_of_repeats = hand.count(char)
        if number_of_repeats != 1:
            value_of_hand += str(number_of_repeats)

    result = values_dict[value_of_hand]

    for i, char in enumerate(hand):
        result += int(f"{char_equivalence[char]}{postion_equivalence[i]}")
    

    return result



rankings = []


with open('input.txt') as f:
    result = 0

    for line in f:
        hand = line.split()
        hand.append(calculate_hand_score(hand[0]))
        rankings.append(hand)
    
    rankings.sort(key=lambda x: x[2])

    for i, hand in enumerate(rankings):
        result += (i + 1) * int(hand[1])

    print(result)
