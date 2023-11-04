import string

def MainMenu():
    print("Welcome to the Cryptographic Techniques Program Tool!\nPlease Enter Your Selection:")
    while True:
        try:
            Selection = int(input(" 1. Encrypt\n 2. Decrypt\n 3. Exit\n "))
            while Selection > 3 or Selection < 1:
                Selection = int(input("Your Selection Has to be either 1, 2, or 3: "))
            break
        except ValueError:
            print("Please Enter an Integer Only! ")
    return Selection

def KeySelection():
    while True:
        try:
            Key = int(input("Please Enter any Integer Key Value: "))
            Key %= 63
            break
        except ValueError:
            print("Please Enter an Integer Only: ")
    return Key

def Cipher(UserIn, Key):
    codes = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    moved = codes[Key:] + codes[:Key]
    trans = str.maketrans(codes, moved)
    caeser = UserIn.translate(trans)
    print("Your Encrypted/Decrypted Message is:", caeser)

def ModeSelect():
    Selection = MainMenu()
    if Selection == 1:
        print("Encryption Mode Selected!\n")
        Key = KeySelection()
        UserIn = input("Please Enter a Text to Encrypt: ")
        Cipher(UserIn, Key)
    elif Selection == 2:
        print("Decryption Mode Selected\nPlease Ensure Key is Correct")
        Key = 63 - KeySelection()
        UserIn = input("Please Enter a Text to Decrypt: ")
        Cipher(UserIn, Key)
    elif Selection == 3:
        print("GoodBye")
        exit()
    
    while True:
        print("Would you Like to Encrypt/Decrypt Again Y/N? ")
        restart = input(": ").strip().lower()
        if restart == 'y':
            ModeSelect()
        elif restart == 'n':
            exit()

ModeSelect()
