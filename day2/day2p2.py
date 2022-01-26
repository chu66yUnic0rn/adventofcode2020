with open("input") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        policy, password = line.strip("\n").split(": ")
        count_range, letter = policy.split(" ")
        index_option1 = int(count_range.split("-")[0])-1
        index_option2 = int(count_range.split("-")[1])-1
        if (password[index_option1] == letter) ^ (password[index_option2] == letter):
            count += 1
    print(count)

