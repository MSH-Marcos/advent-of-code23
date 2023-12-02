
colour_limit = {
    " red": "|12",
    " green": "|13",
    " blue": "|14"   
}

game = 1    
result = 0

# Game 14: 9 green, 4 red; 6 blue, 1 red, 7 green; 3 blue, 5 green

with open('input.txt') as f:
    for line in f:
        line_to_search = line[line.find(":") + 2:]
        for colour, number in colour_limit.items():
            line_to_search = line_to_search.replace(colour, number)
        line_to_search = line_to_search.replace(", ", "|")
        line_to_search = line_to_search.replace("; ", "|")
        line_to_search = line_to_search[:-1]
        list_to_compare = line_to_search.split("|")

        for i in range(0, len(list_to_compare), 2):
            if int(list_to_compare[i]) > int(list_to_compare[i + 1]):
                game += 1
                break
        else:
            result += game
            game += 1
    
    print(result)
