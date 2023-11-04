# Anas Jamil (668659)
# 2020-11-11
# A popular word game involves trying to “build” words from the letters provided in a larger word. Program that asks the user toenter a word, then allows the user to build other words using the supplied letters.

List = []
Main_List = []
print ("Welcome to Word Builder by Anas Jamil")
User_Word = str(input("Please enter a word you would like build from: ")).upper()      
def split(User_Word): 
    return [char for char in User_Word]  
User_Word_Split = (split(User_Word))
print ("You may use these letters to build your word")
print(User_Word_Split)
def Word_Builder():
    while True:
        count = 0
        User_Word_Choice = str(input("Please build a word from the letters above: ")).upper()
        User_Word_Choice2 = (split(User_Word_Choice))
        Length_1 = len(User_Word_Choice)
        Main_Length = len(User_Word)
        List.append(User_Word)
        Main_List.append(User_Word_Choice)
        if Main_Length >= Length_1:
            continue
            count = count + 1
            if count < 3:
                break
                        
            

Word_Builder()        
