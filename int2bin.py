'''
Simple program to convert integers to binary and vice versa

Mark Foley October 2013
'''

# print('Int to binary')

# Integer to binary
int_str = input('Give me an int: ')
my_int = int(int_str)

bin_str = ''
while my_int > 0:
    my_remainder = my_int % 2
    my_int = my_int // 2
    bin_str = str(my_remainder) + bin_str

print('The binary of', int_str, 'is', bin_str)

#
# First part ends here
#

# Binary to Integer
print('\nBinary to int')
bin_str = input('Give me a binary string: ')

temp = bin_str
new_int = 0
power = 0
while len(temp) > 0:
    bit = int(temp[-1])
    new_int = new_int + bit * 2 ** power
    temp = temp[:-1]
    power += 1

print(bin_str, 'to integer is', new_int)

## Alternative algorithm (as raised in class 3-oct)
new_answer = 0
for e in bin_str[:-1]:
    new_answer += new_answer + (int(e) * 2)
new_answer += int(bin_str[-1])

print(f"Alternative algorithm: {bin_str} to int is {new_answer}")
