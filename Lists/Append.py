import random
L = []
while True:
    lower_upper_alphabet = ("A", "B", "C")
    random_letter = random.choice(lower_upper_alphabet)
    L.append(random_letter)
    if len(L) > 100:
        break
    User_Input = str(input("Please pick a letter to remove from A, B or C: ")).upper()
    if len(User_Input) > 1:
        print("Please only pick one letter to remove from A, B or C: ")
    if not User_Input.isalpha():
         print("Please only pick one letter to remove from A, B or C: ")
    else:
        for item in L:
            if(item==User_Input):
                L.remove(User_Input)
        print(L)
        
                
    
    