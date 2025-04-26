def print_pattern(number):
    for index in range(1, number + 1):
        print(str(index) * (number - 1) + str(index + 1))
number = 5
print_pattern(number)