# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[playername]")
define m = Character("Me")
define e = Character("Elise")
define z = Character("Zack")



# The game starts here.
# SCRIPT NI KYLE !
label start:

    # Take player name
    python:
        p = renpy.input("What is your name?", length=32)
        p = p.strip()

        if not p:
            p = "Shy Guy"

    # Start of the story    
    "Hello there [p]"
       
    # Show a black screen with text on top of it
    scene black 

    centered "Case 1: \n\n\nKarl's Desperation"
    
    centered "\“On the 7th of April Year 2019, a new law called {b}Republic Act 11313{/b} or also known as {b}Safe Spaces Act{/b} has 
    been approved by the president.\"" 

    centered "\"This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions……\”"

    #
    scene bg clubroom

    e "Hey, how many times you gonna read that again? [p]"

    m "Well, this is a reminder for myself..Hmm??!!"

    "{i}Your phone starts ringing...{/i}"

    z "[p!u]!!!!"
    
    z "The client’s accusation is real! I also already recorded the scene for the evidence!"
    
    z "Go to the backside of the gym!!! Hurry!!! Before he do something bad to the client!!!"

    m "I see, good work Major Zack."

    z "Ohh really thanks hahahahah!.......wait…..Please! Just hurry up General!!!"

    m "Don’t worry, we will arrive in the scene in no time."

    m "Lieutenant Elise! Get ready, we've got a mission to complete."

    e "Okay! Give me a minute. Also! Don’t call me Lieutenant! Geez"
    
    m "Whatever you say, anyway let’s make haste Lieutenant Elise!"

    e "........"

label backsidegym:
    
    scene bg backsidegym
    



    return
