# Anas Jamil (668659)
# 2020-09-30
# Calculate the are and circumference of a circle, given its radius.
import math
Radius = float(input("Please enter the radius here: "))
Area = math.pi * Radius**2
Circumference = 2 * math.pi * Radius
print("The area is", round(Area, 4), "square units.")
print("the circumference is", round(Circumference, 4), "units.")