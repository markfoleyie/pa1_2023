# If one inch of rain falls on an acre of land, how many gallons of water have accumulated on that acre?
#
# 1 acre = 43,560 square feet
# 1 cubic foot = 7.48051945 gallons
#
# Find the volume in cubic feet of water of 1 inch over 1 acre
# 1 inch = 1/12 foot
# volume = depth * area = (1/12)*43560 cubic feet
#
# Convert cubic feet to gallons
# gallons = volume * 7.48051945

inches_str = input("Enter rainfall in inches: ")
inches_float = float(inches_str)
volume = (inches_float / 12) * 43560
gallons = volume * 7.48051945

print(f"{inches_float} in. rain on 1 acre is {gallons} gallons.")