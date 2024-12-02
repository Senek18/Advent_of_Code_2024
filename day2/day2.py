with open("day2\input.txt", "r") as f:
    data = f.read().splitlines()

def check_movement(value_string):
    values = list(map(int, value_string.split()))
    
    initial_increase = values[0] < values[1]
    
    for i in range(len(values) - 1):
        current_increase = values[i] < values[i+1]
        
        if initial_increase != current_increase or (diff:=abs(values[i] - values[i+1])) > 3 or diff == 0:
            return False
    
    return True

print(sum(1 for line in data if check_movement(line)))