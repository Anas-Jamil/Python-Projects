while True:
    s = input("Please insert a numerical value for a: ")
    try:
        a = float(s)
        break
    except ValueError:
        print ("Please enter a numeric value.")
print ("Well done.")