with open("day2\input.txt", "r") as f:
    data = f.read().splitlines()

def check_movement(value_string):
    values = list(map(int, value_string.split()))
    
    initial_increase = values[0] < values[1]

    for i in range(len(values) - 1):

        current_increase = values[i] < values[i+1]
        
        if initial_increase != current_increase or (diff:=abs(values[i] - values[i+1])) > 3 or diff == 0:
            if check_boundry(values, i) or check_boundry(values, 0) or check_boundry(values, -1) or check_boundry(values, i+1):
                return True
            return False
    return True


def check_boundry(values, idx):
    values_copy = values.copy()
    
    del values_copy[idx]
    
    initial_increase = values_copy[0] < values_copy[1]

    for i in range(len(values_copy) - 1):
        current_increase = values_copy[i] < values_copy[i+1]
        
        if initial_increase != current_increase or (diff:=abs(values_copy[i] - values_copy[i+1])) > 3 or diff == 0:
            return False
    return True

import time
start = time.time()
print(sum(1 for line in data if check_movement(line)))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")