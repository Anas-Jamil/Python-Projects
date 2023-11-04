#Write a program that reads a positive integer from the user, then generates that many random integers between 1 and 20. If the majority of the random numbers are even, display a message. If the majority are odd, display a second. If there is a tie, display a third.
import random
def integer_check():
    while True:
        try:
            Integer = int(input("Please enter a positive integer: "))
            while Integer < 0:
                Integer = int(input("Invalid, Try again with positive integer: "))
            break
        except ValueError:
            print("Please input an integer only!")
    return Integer,
integer_check()
def Random_Generation():
        List_Randoms = (random.randint(0, 21))
        return List_Randoms,
Random_Generation()
def Check_For_Even(number):
    if(number % 2) == 0:
        return True
    return False
Check_For_Even
def Starting():
    Integer = interger_check()
    Number_Of_Evens = 0
    Number_Of_Odds = 0
    for count in range(integer):
        List_Randoms, = Random_Generation()
        if (Check_For_Even(List_Randoms)):
            Number_Of_Evens += 1
        else:
            Number_Of_Odds = Number_Of_Odds + 1
Starting()
def End_Results(If_Evens, If_Odds):
    if Number_Of_Evens > Number_Of_Odds:
        print("There were more even numbers!")
        if Number_Of_Odds > Number_Of_Evens:
            print("There were more odd numbers!")
            if Number_Of_Odds == Number_Of_Evens:
                print("It was a tie!")

            
                        
    