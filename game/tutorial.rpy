label tutorial_start:
    # Ask user some questions aboutn VN, Safe Spaces, etc.

    play music "audio/Shenanigans!.ogg" fadein 2.0
    define n = Character('Natasha')
    
    scene bg beautiful park 
    with fade



    show natasha talk with dissolve

    "Hello! Welcome to our visual novel game...."

    n "My name is Natasha and I will be your guide before you start playing!"

    python:
        player = renpy.input("What is your first name?", length=32)
        player = player.strip()

        if not p:
            p = "Shy Guy"

    show natasha closed eyes_
    with dissolve

    n "Hello [player]!"

    show natasha talk
    with dissolve

    n "This visual novel game was created with the idea of educating people about {color=#22ff00}Safe Spaces Act{/color} in an entertaining fashion!"

    n "Now before you start playing, I will first ask some questions."

    n "Have you ever played a visual novel game before?" 

    hide natasha talk with dissolve

    menu:
        n "Have you ever played a visual novel game before?" 

        "Yes, I've played some before.":

            show natasha closed eyes_
            with dissolve

            n "Great! I see that you are a man/woman of culture as well!"

        "No, not yet.":

            show natasha closed eyes_
            with dissolve

            n "Great! Let's explore together the world of visual novels!"

            n "It's like an interactive book that you can read on a computer or a console."

            n "You can make choices that lead to different events and endings in the story."

            menu:

                "Tell me more.":

                    show natasha talk
                    with dissolve

                    n "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

                "So where does the \"visual\" part come in?":
                    n "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    n "Now that you have some knowledge on visual novels..."

    show natasha talk with dissolve

    n "Do you know anything about the law called \"Safe Spaces Act\"?"

    hide natasha talk with dissolve

    menu:
        n "Do you know anything about the law called \"Safe Spaces Act\"?"

        "I have no idea.":

            show natasha closed eyes_
            with dissolve

            n "That is absolutely fine! Together, we will learn about the Safe Spaces Act through this visual novel."
            n "Learning this law will definitely help you in some way!"

        "I've heard about it before.":

            show natasha closed eyes_
            with dissolve
            
            n "That is magnificent! The extra knowledge that you'll learn here will definitely help you!"

    # Talk about HBB points
    show natasha closed eyes_ with dissolve

    n "I'm gonna say one last thing before I send you off, let me talk about {color=#40ff00}HBB points{/color}."

    n "If you look at the top right corner, there is a indicator of your current points."

    show screen displayHBBPoints 

    show natasha talk 

    with dissolve

    n "What is {color=#40ff00}HBB points{/color}? In this game, there will be decisions and questions wherein you need to select the {color=#40ff00}best answer{/color}."

    n "The game comprises of 3 main stories. However there is a twist."

    n "To unlock the {color=#40ff00}special ending{/color} in each of the main stories, you must reach a certain number of points."

    n "Selecting the {color=#40ff00}most correct{/color} decision will grant you the most points."

    show natasha closed eyes_ with dissolve

    n "I'll give an example! This time, I will include a {color=#f00}timer{/color}."

    n "When the {color=#f00}timer{/color} runs out, it will randomly select a choice. So you should think carefully, okaaaaay? "

    show natasha talk with dissolve

    n "Now here's the scenario. You see me passing in an alleyway. Then some random old men started harassing me."

    show natasha cry with dissolve

    n "I feel so scared because of what they did."

    pause 2.0

    hide natasha cry with dissolve

    $ timeout_label = "natashaChoice3"
    $ timeout = 15

    menu whatToDo:
        "What would you do?"

        "Record it and post in social media.":
            jump natashaChoice1
            

        "Shout at the old men.":
            jump natashaChoice2
            

        "Talk to them calmly and call the police if they don't stop.":
            jump natashaChoice3
            


label natashaChoice1:

    "I will record it and post in social media."

    show natasha closed eyes_ with dissolve

    n "Honestly this is not a bad answer. But are you just gonna let me get harrassed?"

    n "This can be a traumatic experience for me."

    
    play sound "audio/addPoints.mp3"
    $ points += 2
    show screen displayHBBPoints
    n "For this answer, I will reward you {color=#22ff00}2 HBB points{/color}."
    
    

    $ timeout_label = None

    menu:
        "Would you like to try selecting a different choice?"
    
        "Yes":

            with fade

            $ points = 0

            $ timeout_label = "natashaChoice3"

            jump whatToDo
        
        "No":
            jump endTutorial


    

label natashaChoice2:
    "Shout at the old men."

    show natasha closed eyes_ with dissolve

    n "Not the answer I was expecting."

    n "They might beat you up, you know?"

    play sound "audio/addPoints.mp3"
    $ points += 1
    show screen displayHBBPoints

    n "For this answer, I will reward you {color=#22ff00}1 HBB point{/color}."

    

    $ timeout_label = None

    menu:
        "Would you like to try selecting a different choice?"
    
        "Yes":

            with fade

            $ points = 0

            $ timeout_label = "natashaChoice3"

            jump whatToDo
        
        "No":
            jump endTutorial

label natashaChoice3:
    "Talk to them calmly and call the police if they don't stop."

    show natasha closed eyes_ with dissolve

    n "I think this is the best answer."

    show natasha talk with dissolve

   
    play sound "audio/addPoints.mp3"
    if points < 3:
        $ points = 3
    else:
        $ points += 3
    
    show screen displayHBBPoints
    n "For this answer, I will reward you {color=#22ff00}3 HBB points{/color}."

    

    n "You saved me from them and prevented them from doing anything!!"

    show natasha blush with dissolve

    n "I might fall for you, you know?"

    show natasha closed eyes_ with dissolve

    n "Just kidding!!! Hahaha~"

    show natasha talk with dissolve

    label endTutorial:

        n "Since this is only a tutorial..."

        n "The next time when you don't choose the best answer, you will {color=#f00}lose points!{/color}"

        show natasha closed eyes_ with dissolve

        n "Remember that okaaaaaaaaay?"

        n "Okay let's now move on to the game!"

        stop music fadeout 3.0
        pause 2.0
        jump yui_start_case_1



    