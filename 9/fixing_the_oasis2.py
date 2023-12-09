

# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45



with open('input.txt', 'r') as f:
    result = 0

    lines = f.read().splitlines()

    for line in lines:
        number_tree = []
        number_serie = line.split()
        number_serie = [int(n) for n in number_serie]

        number_tree.append(number_serie)

        iter = 0

        while True:
            temp_number_list = []
            for i in range(len(number_tree[- 1]) - 1):
                temp_number_list.append(number_tree[- 1][i + 1] - number_tree[- 1][i])
            
            number_tree.append(temp_number_list)

            if all(el == 0 for el in temp_number_list):
                break
            iter += 1
        temp_res = 0

        for i in range(len(number_tree) - 1, 0, -1):
            temp_res = number_tree[i - 1][0] - temp_res
        result += temp_res

print(result)