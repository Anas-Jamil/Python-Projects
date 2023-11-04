def NumOfSevens(integer):
    sevens=0
    while (integer > 0):
        if (integer % 10 == 7):
            sevens=sevens+1
        integer = integer // 10
    return sevens
import random
for val in range(20):
    integer=random.randint(1,1000000)
    sevens=NumOfSevens(integer)
    print(integer, sevens)