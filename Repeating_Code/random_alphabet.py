import random
Alphabet = str(input("Would you like a random letter? Yes or No?: "))
if Alphabet == ("Yes") and ("yes"):
    count = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("A random letter is",count)

