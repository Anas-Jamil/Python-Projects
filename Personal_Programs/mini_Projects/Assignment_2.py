# Anas Jamil (668659)
# 2020-10-23
# Dice rolling game, whoever rolls the highes at the end of the game wins. Whoever reacher 50 first wins
import time
import sys
import random
Introduction = input("Welcome to a dice rolling game! Press enter to continue")
if Introduction == (""):
    #Loads game with effect
    text = "Loading..."
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.3)
    print("\nWelcome to the Dice Rolling Game") 
    while True:
#Roll loop starts here
        User_Input = input("Player one will go first! Press enter when ready")
        if User_Input == (""):
            Roll = random.randint(1,6)
            Player = 1
            Total_Player_One = 0
            text = "Rolling Die"
            for char in text:
                sys.stdout.write(char)
                time.sleep(0.2)
            print("\nPlayer", Player, "rolled a", Roll,)
            Total_Player_One = Roll + Total_Player_One
#Would Have used define statment here but did not want to waste time since it was not part of requiremnet.
#Code repeats here.Define statment would have been more effiecent.Not enough time.
            User_Input2 = input("Now player two will roll!, Press enter to continue")
            if User_Input2 == (""):
                Roll1 = random.randint(1,6)
                Player2 = 2
                Total_Player_Two = 0
                text = "Rolling Die"
                for char in text:
                    sys.stdout.write(char)
                    time.sleep(0.2)
                print("\nPlayer", Player2, "rolled a", Roll1,)
                Total_Player_Two = Roll1 + Total_Player_Two
                if Total_Player_One or Total_Player_Two > 5:
                    if Total_Player_One > Total_Player_Two:
                        print("Player One Wins!")
                    elif Total_Player_One < Total_Player_Two:
                        print("Player Two Wins!")
                    break
                    
        
    

  <div class="Heading_1">
    <h2>My Projects</h2>
    <div class="My_Projects">
        <script src="https://gist.github.com/Anas-Jamil/1d2be29ef633b9e01eb357ff764284e2.js"></script>
            <div class="Pro_1">
                <h1>Portfolio Website HTML/CSS</h1>
                <p>Welcome to my custom-built portfolio! This website is a reflection of my passion for web development and my desire to showcase my skills and past projects to anyone interested in my work. It serves as a testament to my experience in both front-end and back-end design, with the seamless integration of HTML, CSS, and JavaScript. This portfolio isn't just a collection of code and designs; it's a canvas that tells the story of my journey in the world of web development. It's a testament to my commitment to continuous improvement and my dedication to creating memorable online experiences <br></p>
                <h3>Showcasing My Skills</h3>
                <p>My website demonstrates not only my technical skills but also my creativity. The design, layout, and interactivity are carefully crafted to provide a user-friendly and visually appealing experience.</p>
            </div>
    </div>
</div>


.My_Projects {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    position: absolute;
    bottom: -220vh;
    background-color: rgb(156, 151, 151);
    width: 100%;
    height: 90%;
    text-align: center;
    font-family: 'Source Code Pro', monospace;
    color: hsl(0, 0%, 22%);
    box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
}
.Pro_1 {
    width: 50%; /* Adjust the width as needed */
    max-width: 600px; /* Limit the max width */
}
.Heading_1 h2 {
    position: absolute;
    font-size: 60px;
    top: 225%;
    z-index: auto;
}