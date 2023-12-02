
colour = {
    "red": "|red|",
    "green": "|green|",
    "blue": "|blue|"   
}

with open('input.txt', 'r') as f:
    content = f.read()
    content = content.replace(", ", "")
    content = content.replace("; ", "")
    content = content.replace(" ", "")
    for colour, number in colour.items():
        content = content.replace(colour, number)

    lines = content.splitlines()

    result = 0

    for line in lines:
        max_colour = {
            "blue": 0,
            "red": 0,
            "green": 0
        }

        line_to_search = line[line.find(":") + 1:]
        
        list_to_check = line_to_search.split("|")
        list_to_check = list_to_check[:-1]

        for i in range(0, len(list_to_check), 2):
            if max_colour[list_to_check[i + 1]] < int(list_to_check[i]):
                max_colour[list_to_check[i + 1]] = int(list_to_check[i])
        
        result += max_colour["blue"] * max_colour["green"] * max_colour["red"]
    
    print(result)