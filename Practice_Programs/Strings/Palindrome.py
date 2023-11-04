def isPalindrome(User_Input):
    return User_Input == User_Input[::-1]

User_Input = input("Please enter a word: ")
Check_Pal = isPalindrome(User_Input)
 
if Check_Pal:
    print("Yes")
else:
    print("No")