import random
Die1 = random.randint(1,10)
Die2 = random.randint(1,10)
print("you rolled a",Die1, "and a",Die2)
if Die1 > Die2:
    print("This was the largest number:",Die1)
else:
    print("This was the largest number:",Die2)