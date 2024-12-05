
with open("day5/input.txt", "r") as f:
    data = f.read().split("\n\n")
    rules = data[0].splitlines()
    updates = data[1].splitlines()

rules_dict = {}

for rule in rules:
    l, r = map(int, rule.split("|"))
    rules_dict[l] = rules_dict.get(l, []) + [r]

incorrect = []
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
                incorrect.append(key_list)
                break
            continue

        for i in range(idx+1, number_of_elements):
            if key_list[i] not in rule:
                wrong_list = True
                incorrect.append(key_list)
                break
    else:
        correct.append(key_list)

new_order = []
for pages in incorrect:
    number_of_elements = len(pages)
    i = 0
    while True:
        try:
            rule = rules_dict[pages[i]]
        except KeyError:
            move_element = pages[i]
            del pages[i]
            pages.append(move_element)
            continue
        next_idx = False
        for j in range(i+1, number_of_elements):
            if pages[j] not in rule:
                move_element = pages[i]
                del pages[i]
                pages.append(move_element)
                next_idx = True
                break

        if next_idx:
            continue

        i+=1
        if i > (j:=int(number_of_elements/2)):
            new_order.append(pages[j])
            break

print(sum(new_order))