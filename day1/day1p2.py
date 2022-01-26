from itertools import combinations

with open("input") as f:
    lines = f.readlines()
    numbers = [int(line.strip()) for line in lines]
    for num1, num2, num3 in list(combinations(numbers,3)):
        total = num1 + num2 + num3
        if total == 2020:
            print(num1 * num2 * num3)
