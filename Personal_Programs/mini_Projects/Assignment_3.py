# Anas Jamil (668659)
# 2020-10-29
# Draw a playing card with the Rank, Colour and Suit. Ask user if it would like to roll.
import random
def Rank_Of_Card():

    import random
    Total_Card_Rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    Card_Rank = random.choice(Total_Card_Rank)
    return Card_Rank,

def Suit_Of_Card():

    Total_Suits = ["Spades", "Hearts", "Club", "Diamond"]
    Rank_Of_Suit = random.choice(Total_Suits)
    return Rank_Of_Suit,

def Colour_Of_Card():
 
    Rank_Of_Suit, = Suit_Of_Card()
    if Rank_Of_Suit == "Spades" or "Clubs":
        Colour_Card = "Black"
    else:
        Colour_Card = "Red"
    
    return Colour_Card,
         
def Main_Program():

    Card_Rank, = Rank_Of_Card()
    Rank_Of_Suit, = Suit_Of_Card()
    Colour_Card, = Colour_Of_Card()
    User_Input = input("Type Yes to draw a card: ").upper().strip()
    if User_Input.isdigit:
        if User_Input != "YES":
            print("Bye")
    if User_Input == "YES":
        Rank_Of_Card()
        Suit_Of_Card()
        Colour_Of_Card()
        print ("You got a", Colour_Card, Card_Rank, "of", Rank_Of_Suit)

                
Main_Program()
                    
                    
                    
                    
            
            
    


    

        