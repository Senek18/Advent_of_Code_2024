with open("day5/input.txt", "r") as f:
    data = f.read().split("\n\n")
    rules = data[0].splitlines()
    updates = data[1].splitlines()

rules_dict = {}

for rule in rules:
    l, r = map(int, rule.split("|"))
    rules_dict[l] = rules_dict.get(l, []) + [r]

correct = []
for update in updates:
    key_list = list(map(int, update.split(",")))
    number_of_elements = len(key_list)
    wrong_list = False
    for idx, key in enumerate(key_list):
        if wrong_list:
            break

        try:
            rule = rules_dict[key]
        except KeyError:
            if idx != number_of_elements - 1:
                wrong_list = True
                break
            continue

        for i in range(idx+1, number_of_elements):
            if key_list[i] not in rule:
                wrong_list = True
                break
    else:
        correct.append(key_list)

count = 0
for update in correct:
    count += update[int(len(update)/2)]

print(count)