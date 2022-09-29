"""
This is a program to calculate the area and circumference of a circle.

Mark F.
Sept 2020
"""

# Calculate the area and circumference of a circle
# 1. Prompt for the radius
# 2. Apply formulae
# 3. Print results

import math

radius_str = input("Input radius: ")

radius_float = float(radius_str)

circumference = 2 * math.pi * radius_float
area = math.pi * (radius_float ** 2)

print(f"When radius is {radius_float}, circumference is {circumference} and area is {area}.")
