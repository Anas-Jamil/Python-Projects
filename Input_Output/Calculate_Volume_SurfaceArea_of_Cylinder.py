# Anas Jamil
# 2020-10-15
# Calculate the volume and surface area of a cylinder
import math
Radius = float(input("Please enter the radius: "))
Height = float(input("Please enter the height: "))
Volume = round((math.pi * Radius**2)*Height,4)
Surface_Area = round(2 * math.pi*Radius * (Radius+Height),4)
print("The volume was:",Volume)
print("The surface area was:",Surface_Area)