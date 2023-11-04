# Anas Jamil (668659)
# 2020-10-01
# Is number a perfect square
import math
num = int(input("Please enter an integer: "))
sqroot = math.sqrt(num)
if int(sqroot + 0.5) ** 2 == num:
    print("Your number,", num, "is a perfect square!")
else:
    print("Your number,", num, "is not a perfect square!")