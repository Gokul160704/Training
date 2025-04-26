def is_disarium(num):
    num_str = str(num)
    total = 0
    for index in range(len(num_str)):
        total += int(num_str[index]) ** (index + 1)
    return total == num

num = 135
print(f"{num} is a Disarium number: {is_disarium(num)}")

def first_n_disarium(num):
    disarium_numbers = []
    index = 1
    while len(disarium_numbers) < num:
        if is_disarium(index):
            disarium_numbers.append(index)
        index += 1
    return disarium_numbers
num = 10
print(f"First n Disarium numbers as n = {num}: {first_n_disarium(num)}")

def disarium_in_range(start, end):
    return [num for num in range(start, end + 1) if is_disarium(num)]

start, end = 1, 100
print(f"Disarium numbers between {start} and {end}: {disarium_in_range(start, end)}")




