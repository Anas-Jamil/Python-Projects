#Anas Jamil
#2023-10-08

import random

def Rank_Of_Card():
    Total_Card_Rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    Total_Card_Value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    combined_cards = list(zip(Total_Card_Rank, Total_Card_Value))
    Card_Rank = random.choice(combined_cards)
    return Card_Rank

def Suit_Of_Card():
    Total_Suits = ["Spades", "Hearts", "Club", "Diamond"]
    Rank_Of_Suit = random.choice(Total_Suits)
    return Rank_Of_Suit

def Colour_Of_Card():
    Rank_Of_Suit = Suit_Of_Card()
    if Rank_Of_Suit in ["Spades", "Club"]:
        Colour_Card = "Black"
    else:
        Colour_Card = "Red"
    return Colour_Card

def Main_Program():
    while True:
        User_Input = input("Type 'Yes' to start the game: ").strip().lower()
        if User_Input == 'yes':
            player_select()
        else:
            print("Please enter 'Yes' to draw a card.")
            continue

        restart = input("Would you like to play again? (Y/N): ").strip().lower()
        if restart != 'y':
            break

def player_select():
    player_one = input("Player one, please type your name: ")
    player_two = input("Player two, please type your name: ")

    Player_One_Draw = Rank_Of_Card()
    Player_Two_Draw = Rank_Of_Card()

    print(f"Player One ({player_one}) drew a {Player_One_Draw[0]} ({Colour_Of_Card()})")
    print(f"Player Two ({player_two}) drew a {Player_Two_Draw[0]} ({Colour_Of_Card()})")

    if Player_One_Draw[1] > Player_Two_Draw[1]:
        print(f"{player_one} wins")
    elif Player_One_Draw[1] < Player_Two_Draw[1]:
        print(f"{player_two} wins")
    else:
        print("It's a tie!")

Main_Program()
