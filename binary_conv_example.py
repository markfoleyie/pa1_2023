# The Problem

# We are going to do some conversions, from integer to binary and then from binary back to integer. It will give us a
# chance to play with if-elif-else and while statements, as well as a little string slicing.

# Your Task
# You prompt for an integer, convert the integer to a binary number string (there is no type for actual binary numbers
# so we just represent it as a string). We then take the string and turn it back into a regular integer. Things to remember
# If the integer is 0, then we are done since conversion back and forth of 0 is still 0. The program simply prints a note
# saying it is 0 and quits.

incoming_int_as_string = input("Enter an integer to convert: ")
if incoming_int_as_string.isnumeric():
    incoming_int = int(incoming_int_as_string)
else:
    print(f"{incoming_int_as_string} is not a number, quitting...")
    quit(1)

# If the integer is negative, then we probably don’t know how to do it, so the program prints a message saying it is
# negative and quits.

if incoming_int < 0:
    print(f"Value {incoming_int} cannot be processed, so I'm quitting...")
    quit(1)
else:
    print(f"{incoming_int} is a valid number, proceeding to conversion...")

# Otherwise, we do the conversion of the integer to a binary string (a string of 1’s and 0’s) and then convert that same
# string back to an integer to make sure we did it right.

# Hints

binary_string = ''

while incoming_int > 0:                    # keep dividing by 2 until nothing left
    remainder = incoming_int % 2           # '%' is 'modulus' i.e. it calculates the remainder from division
    incoming_int = incoming_int // 2       # '//' is 'integer' division, i.e. yields a whole number only.
    binary_string = str(remainder) + binary_string     # Fill in what has to happen next (make a string of remainder and add it to
                                           # the fromt of 'binary_string')

print(f"Converted {incoming_int_as_string} to {binary_string}")

# End of first part

# How do we get a binary string from an integer? First, we note that dividing an integer by 2 is essentially a shift of
# the bits that represent the number 1 to the right. For example:
# 10 in binary is ‘1010’. That’s the answer we should get after we do all the following.
#
# 10/2 is 5, which in binary is ‘101’ (shift ‘1010’ to the right, drop the last value which gets shifted off and
# disappears, leaves ‘101’)
#
# 5/2 is 2, which in binary is ‘10’
#
# 2/1 is 1, which in binary is ‘1’
#
# When we do this shift, we want to remember the bit that “falls off” as we shift to the right. The remainder function
# tells us what that number is. Thus:
#
# 10 in binary is ‘1010’, remember that’s our answer.
#
# 10 % 2 is ‘0’, 10/ 2 is 5, which in binary is ‘101’. Remember the ‘0’, work with the new dividend value of 5
#
# 5 % 2 is ‘1’, 5/ 2 is 2, which in binary is ‘10’. Concatenate the ‘1’ remainder to the previous ‘0’ to make ’10’.
# Work with the new dividend value 2
#
# 2 % 2 is ‘0’, 2/2 is 1, which in binary is ‘1’. Concatenate the ‘0’ remainder to the previous ‘10’ to make ‘010’.
# Work with the new dividend value of 1.
#
# 1 % 2 is ‘1’, 1/2 is 0, and we are done dividing. Concatenate the ‘1’ remainder with the previous ‘010’ to make ‘1010’
#
#
# GETTING AN INTEGER FROM A BINARY STRING...
#
# How do we get an integer from a binary string? First, we know it is a string, so the elements are ‘1’ and ‘0’.
# Every time we grab a 1 or a 0 (a bit), we are adding a power of two to the overall integer value. Which power of 2?
# If you grab bits from the right, they are increasing orders of powers of 2. The far right position of the string, or,
# better said, the last bit in the string (how do you get the last bit??) is 2**0. The next bit 2**1. The next bit 2**2.
# And so on. If the bit is a ‘1’, then we add that power of 2 to the overall sum; if it is 0 we do nothing.
#
# For example. start with ‘1010’
# last bit is ‘0’ and 2**0 * 0 is 0. Sum is 0
# next bit is ‘1’ and 2**1 * 1 is 2. Sum is 2
# next bit is ‘0’ and 2**2 * 0 is 0. Sum is 2
# next bit (first bit) is ‘1’ and 2**3 * 1 is 8. Sum is 10
binary_string = input('Give me a binary string: ')
for character in binary_string:
    if character not in ('1', '0'):
        print(f"Invalid input. {binary_string} is not a binary string")
        quit(1)

temporary_binary_string = binary_string    # we use temporary_binary_string in the calculation as we will be chopping
                                           # off pieces of it, one digit at a time
answer = 0                                 # answer is computed by summing up binary digits by successive powers of 2
power = 0

while len(temporary_binary_string) > 0:
    bit = int(temporary_binary_string[-1])
    answer = answer + (bit * (2 ** power))
    temporary_binary_string = temporary_binary_string[:-1]
    power += 1

print(f"I converted binary {binary_string} to {answer}")

# To convert to other base e.g. hex (base 16) create string with valid ssymbols
base_string = "0123456789abcdef"
# change base to a variable (16) -> it's 2 at the moment