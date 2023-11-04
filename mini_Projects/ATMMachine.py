# Anas Jamil (668659)
# 2020-10-16
# ATM Machine Coding Project
def Creating_PIN():
    while True:
        try:
            Pin = int(input("Please Create Your PIN number: "))
            while Pin > 9999 or Pin < 1000:
                Pin = int(input("Your Pin Has To Be Four Digits, Try Again: "))
            break
        except ValueError:
            print("Please input an integer only!")
    return Pin,

def Welcome_Page():
    Pin, = Creating_PIN()
    print("Welcome To Scotia Bank ATM")
    Enter_Pin = int(input("Please Enter Your PIN number: "))
    if Enter_Pin == Pin:
        print("Welcome To Scotia Bank ATM\nPlease pick what you would like!")
        print
    else:
        Incorrect_PIN_Reset()

def Incorrect_PIN_Reset():
    count = 3
    while count > 0:
        int(input("Invalid try again, " + str(count) + " " + "tries left : "))
        count = count - 1
    if count < 1:
        print("You Have Been LOCKED Out!")
        Enter_To_Continue = input("Press enter to continue and make a new PIN")
        if Enter_To_Continue == (""):
            Welcome_Page()

Welcome_Page()

