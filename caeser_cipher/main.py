#Anas Jamil, Huzaifa Farhan 
#100864684, #100741975
#Natural Foundations, Assingment One
#September 28 2023

import string                   #importing the string modulus for this code


def MainMenu():                                                                                                    # Function to display the main menu and get user selection
    print("Welcome to the Cryptographic Techniques Program Tool!\nPlease Enter Your Selection:")            #print the following string
    while True:                                                                                         #while infinite loop
        try:                                                                                            #test this first
            Selection = int(input(" 1. Encrypt\n 2. Decrypt\n 3. Exit\n "))                             #get input from user by selecting one of the three
            while Selection > 3 or Selection < 1:                                               #this is to make sure the input is either 1,2,3 or there would be errors
                Selection = int(input("Your Selction Has to be either 1, 2 or 3: "))        #this is to make sure the input is either 1,2,3 or there would be errors
            break
        except ValueError:
            print("Please Enter an Integer Only! ")                                         #to make sure that only integers are entered and not other characters
    return Selection


def KeySelection():                                                            # Function to get an integer key from the user
    while True:
        try:
            Key = int(input("Please Enter any Integer Key Value: "))                    #taking input for any integer number
            Key %= 63                                                                           #return input modulus of 63
            break
        except ValueError:
            print("Please Enter Integer Only: ")                                     #to make sure that only integers are entered and not other characters
    return Key


def Cipher(UserIn, Key):                                                                    # Function to perform encryption or decryption
    codes = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '               # used to declare all the characters and integers for encrypting
    moved = codes[Key:] + codes[:Key]                                                       # uses key from user and shifts that many characters right (ex. key = 4, 4 units right), then appends all characters that were behind the key, to the front.
    trans = str.maketrans(codes, moved)                                                     # creates a transistion to convert the 'codes' to the shifted codes ("moved")
    caeser = UserIn.translate(trans)                                                        # Translates to string, which uses the translation made in the last argument
    print("Your Encrypted/Decrypted Message is:", caeser)                                   # prints encryption or decryption


def ModeSelect():                                                           # Function to select between modes
    Selection = MainMenu()
    if Selection == 1:
        print("Encryption Mode Selected!\n")                                        #print the following string
        Key = KeySelection()
        UserIn = input("Please Enter a Text to Encrypt: ")
        Cipher(UserIn, Key)
    elif Selection == 2:
        print("Decryption Mode Selected\nPlease Ensure Key is Correct")                             #print the following string
        Key = 63 - KeySelection() 
        UserIn = input("Please Enter a Text to Decrypt: ")
        Cipher(UserIn, Key)
    elif Selection == 3:
        print("GoodBye")
        exit()
    
    while True:
        print ("Would you Like to Encrypt/Decrypt Again Y/N? ")                             #print the following string
        restart = input(": ").strip().lower()
        if restart == 'y':                                                      #if input for restart is y then go to the start of the code
            ModeSelect()
        elif restart == 'n':                                                        #else if input for restart is n then end the code
            exit()


ModeSelect()

    







    

