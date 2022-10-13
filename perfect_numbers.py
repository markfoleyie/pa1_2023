# classify a range of numbers with respect to perfect, abundant or deficient
# unless otherwise stated, variables are assumed to be of type int. Rule 4

top_num_str = input("What is the upper number for the range:")
if not top_num_str.isnumeric():
    print(f"{top_num_str} is not a valid integer. Quitting...")
    quit(1)

top_num = int(top_num_str)
number = 2

if number > top_num:
    print(f"{top_num} needs to less than or equal to {number}. Quitting...")
    quit(1)

while number <= top_num:
    # sum up the divisors
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1
    # classify the number based on its divisor sum
    if number == sum_of_divisors:
        print(f"{number} is perfect")
    elif number < sum_of_divisors:
        print(f"{number} is abundant")
    else:
        print(f"{number} is deficient")
    number += 1
