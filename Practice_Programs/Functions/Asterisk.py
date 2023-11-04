def display_square(size, Character):
    for count in range(size):
        print(Character*size)

Character = input("Please enter a single character: ")
size = int(input("Please enter a positive number: "))
display_square(size, Character) 
