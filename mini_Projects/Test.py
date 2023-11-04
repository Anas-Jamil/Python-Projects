while True:
    try:
        User_Input = float(input("Hey would you like to draw a card Yes or No: "))
        while User_Input != "Yes" or "yes" or "No" or "no":
            User_Input = float(input("Please enter Yes or No only! "))
        break
    except ValueError:
        print("Please input an integer only!")
