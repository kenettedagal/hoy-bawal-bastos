# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[playername]")
define e = Character("Elise")
define z = Character("Zack")



# The game starts here.

label start:

    # Take player name
    python:
        p = renpy.input("What is your name?", length=32)
        p = p.strip()

        if not p:
            p = "Pat Smith"

    # Start of the story    
    "Hello there [p]"
       
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom_01_day
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show placeholder 
    
    "\“On April 17,2019 a law called Republic Act 11313 or also known as Safe Space Act has 
    been approved by the president. This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions……\”"







    return
