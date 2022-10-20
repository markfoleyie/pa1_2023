'''
This program takes an integer as input and converts it to its equivalent
in any base from 2 (binary) to 16 (hexadecimal). We impose a limit of 16 
because we don't have a convenient symbol set defined for digits beyond 15.
Hex 15 is 'f'.   

Note that even though the program is longer than the class example, most of the extra effort went on 
error trapping. 

Note also that I have partitioned the work using functions to handle the conversions and the validation 
of the base. As this validation function us invoked by both conversion functions, this is a sensible approach.

Written by Mark Foley, October 2012 amended October 2013, October 2022.
'''

BASE_DIGITS = '0123456789abcdef'
# Symbols for ANY base up to 16 (hex)

def int_to_base(my_int, my_base):
    ''' This function takes in an integer and a base and converts the integer to the base.
    The result is returned as a string.
    The method is to repeatedly divide the integer by the base and store the remainder.
    Example: 8 to base 2 (binary)
    1. -- 8/2 = 4, remainder 0
    2. -- 4/2 = 2, remainder 0
    3. -- 2/2 = 1, remainder 0
    4. -- 1/2 = 0, remainder 1
    5. Reading from the bottom up, answer is 1000
    '''
    print(f"Converting {my_int} to {my_base}")

    base_str = ''
    # Answer is initially blank
    my_quotient = my_int
    # We store the quotient in my_quotient

    while my_quotient > 0:
        # my_quotient reduces with each trip around the while loop until it equals 0
        base_digit = str(BASE_DIGITS[my_quotient % my_base])
        # base_digit is the remainder converted to string
        base_str = base_digit + base_str
        # base_str is prior answer added to base_digit because the answer reads in reverse
        my_quotient //= my_base
        # quotient is reduced for next trip through while loop

    print(f"The base {my_base} of {my_int} is {base_str}")
    return base_str


def base_to_int(base_str, my_base):
    '''
    This function takes a value in string format and converts it to base 10 (decimal).
    The characters in the string must be in '0123456789abcdef'.
    The method is least significant digit * base^0 + next digit * base^1 ... and so on
    Example: 3f (base 16) = [f (15) * 16^0 = 15] + [3 * 16^1 = 48] = 63
    '''

    print(f"Converting {base_str} to decimal")

    tmpbase_str = base_str
    # tmpbase_str holds the string to convert less the least significant digit after each loop
    answer = 0
    # Answer starts at 0, is added to with each trip through the while loop
    power = 0
    # Power starts at 0, increases by one for each trip through the while loop

    while len(tmpbase_str) > 0:
        # Go through string - a digit is lost each time, loop ends when there are none left
        for pos in range(len(BASE_DIGITS)):
            # Look up each element in 'base_digits'
            if BASE_DIGITS[pos] == tmpbase_str[-1]:
                # Get the integer equivalent of the current character ...
                int_equivalent = int(pos)
                # ... in tmpbase_str working from the end
                break
                # Once you've found it you can stop looking

        answer = answer + int_equivalent * my_base ** power
        # Add integer you found * the base to the power of <depends on how many trips through loop>
        tmpbase_str = tmpbase_str[:-1]
        # String has last digit chopped off
        power += 1
        # power increases by 1

    print(f"{base_str} base {my_base} to integer is {answer}")
    return answer


def is_valid_base(my_base):
    '''
    Returns True if base is valid
    '''
    if not my_base.isdigit():
        print("Bad input, You must enter a valid integer")
        return False
    if int(my_base) not in range(2, 17):
        print("bad input, You must enter a number between 2 & 16")
        return False
    return True

# The program starts here.
#
# We set up a while loop that only exits when you enter '0'. 
# On each loop we get the inputs for our integer and the base. 
# Make sure that both are in valid ranges - int must be a valid number and base 
# must be between 2 & 16

optionStr = ""
while optionStr != "0":
    print("\nInteger to Base Converter")
    print("-------------------------")
    print("Choose an option")
    print("Enter 1 Convert from decimal to base x")
    print("Enter 2 Convert from base x to decimal")
    print("Enter 0 to exit the program")

    optionStr = input("Enter your choice now: ")
    if (len(optionStr) != 1) or (optionStr not in "012"):
        print("Error: You must enter a valid choice")

    #
    # This section handles Int to Base x
    #
    elif optionStr == "1":  # Int to Base selected ...
        int_str = input('Give me an integer to convert: ')

        if not int_str.isdigit():  # Invalid integer?
            print("Bad input, You must enter a valid integer")
            break

        my_int = int(int_str)  # We now have a valid integer to convert

        base_str = input('Give me a base: ')

        if not is_valid_base(base_str):  # Invalid base?
            break

        my_base = int(base_str)  # We now have a valid base

        # The next line is the main event here. This passes your valid source integer and base to the function
        # that actually does the work of converting to the target base
        my_answer = int_to_base(my_int, my_base)

        print("Answer is ", my_answer)

    #
    # This section handles Base x to Int
    #
    elif optionStr == "2":
        base_str = input('Give me a string to convert: ')
        for char in base_str:
            if char not in BASE_DIGITS:
                print("Bad string:", char)
                break  # ... out of 'if'
            break  # ... out of 'for' loop

        base = input('Give me a base: ')

        if not is_valid_base(base):  # Invalid base?
            break

        my_base = int(base)  # We now have a valid base

        # The next line is the main event here. This passes your valid source string and base to the function
        # that actually does the work of converting the string representation of the source number to the target base
        my_answer = base_to_int(base_str, my_base)
        print("Answer is ", my_answer)

    #
    # This section causes you to exit
    #
    elif optionStr == "0":
        print("\nExiting ... Goodbye!")

    #
    # Catches any other weird condition. Should never be reached, it's just here for completeness.
    #
    else:
        print("\Bad option")
