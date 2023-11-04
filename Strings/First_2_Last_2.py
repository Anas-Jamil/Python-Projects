Example = input("Please enter a word: ")
Ans = Example[0:2] + Example[-2:]
Len_Ans = len(Ans)
if Len_Ans < 4:
    print("Bye")
else:
    print(Ans)
    