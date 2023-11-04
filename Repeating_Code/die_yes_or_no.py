import random
while True:
    Die_One = random.randint(1,6)
    Die_Two = random.randint(1,6)
    print("you rolled a", Die_One, "and a", Die_Two)
    answer = None
    while answer != "yes" and answer != "no":
        answer = str(input("Would you like to roll again? yes or no? "))
        if answer == "yes":
            if answer == "no":
                print("Bye!")
        break    
                     
    
        
       
    