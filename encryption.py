'''
In this lab we will create a program that can encrypt and decrypt strings 
using a simple algorithm.

The algorithm we will use is the following:
* To encrypt a string, we reverse it and add 1 to the ASCII code for each 
character. For example, if we take the word:
    python
    When we encrypt the word it becomes:
    opiuzq
Notice that the p in python has become q in the encrypted string and we 
have switched the order.

To decrypt a string we do the opposite. We reverse the order again, but 
this time subtracting 1 from the ASCII code for each character in the 
string.

Your output should look something like:

Enter plaintext: some random text

Encrypting  some random text
s  ->  t
o  ->  p
m  ->  n
e  ->  f
   ->  !
r  ->  s
a  ->  b
n  ->  o
d  ->  e
o  ->  p
m  ->  n
   ->  !
t  ->  u
e  ->  f
x  ->  y
t  ->  u

Encrypted string is  uyfu!npeobs!fnpt

Enter cyphertext: uyfu!npeobs!fnpt

Decrypting  uyfu!npeobs!fnpt
u  ->  t
y  ->  x
f  ->  e
u  ->  t
!  ->   
n  ->  m
p  ->  o
e  ->  d
o  ->  n
b  ->  a
s  ->  r
!  ->   
f  ->  e
n  ->  m
p  ->  o
t  ->  s

Decrypted string is  some random text


 Here are some encrypted strings for you to decrypt:
 /ztbF!tj!hojnnbshpsq!/hojnnbshpsq!fwpM!J
 /sfuvqnpd!b!op!ovs!pu!tofqqbi!utvk!ubiu!hojwmpt.nfmcpsq!op!zbttf!ob!tj!nbshpsq!B
 ubfsh!tj!opiuzQ
 fujsx!pu!fwbi!uoeje!vpz!fojm!fiu!tj!fupsx!sfwf!vpz!fepd!gp!fojm!utfc!fiU
 
 
 Mark Foley October 2013.
'''


def convert_string(original_string, option_flag):
    '''
    General function to encrypt or decrypt text. Note that the only
    difference between encryption and decryption in this program is the
    shifting of the	ASCII value of a character, either up or down (* 1 or
    * -1). optionFlag can be shift key or shift key * -1 which determines whether we are
    encrypting or decrypting. The program sets positive or negative as appropriate.
    '''
    new_string = ''
    for any_char in original_string:
        new_string += chr(ord(any_char) + option_flag)
        print(any_char, ' -> ', chr(ord(any_char) + option_flag))

    return new_string[::-1]


# The program starts here.
#
# We set up a while loop that only exits when you enter '0'. 
# On each loop we get the text to be converted. The only difference
# between encryption and decryption in this program is the conversion of 
# the ASCII value of a character, either up or down (+ or -).

option_str = ""
while option_str != "0":
    print("\nEncrypt/Decrypt Text")
    print("----------------------")
    print("Choose an option")
    print("Enter 1 to Encrypt")
    print("Enter 2 to Decrypt")
    print("Enter 0 to exit the program")

    option_str = input("Enter your choice now: ")
    if (len(option_str) != 1) or (option_str not in "012"):
        print("Error: You must enter a valid choice")

    #
    # This section handles Encryption
    #
    elif option_str == "1":

        try:
            inStr = input('Enter plaintext: ')
            shift_key = int(input("Enter shift key: "))
            print("Result is ", convert_string(inStr, shift_key))
        except Exception as e:
            print(str(e))
            continue


    #
    # This section handles Decryption
    #
    elif option_str == "2":
        try:
            inStr = input('Enter cyphertext: ')
            shift_key = int(input("Enter shift key: "))
            print("Result is ", convert_string(inStr, (shift_key * -1)))
        except Exception as e:
            print(str(e))
            continue

    #
    # This section causes you to exit
    #
    elif option_str == "0":
        print("\nExiting ... Goodbye!")
        break

    #
    # Catches any other weird condition. Should never be reached, it's
    # just here for completeness.
    #
    else:
        print("\nBad option")
