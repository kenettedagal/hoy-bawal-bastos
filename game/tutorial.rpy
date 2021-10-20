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

    n "This visual novel game was created with the idea of educating people about Safe Spaces Act in an entertaining fashion!"

    n "Now before you start playing, I will first ask some questions."

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

    show natasha talk with dissolve

    n "What is {color=#40ff00}HBB points{/color}? In this game, there will be decisions and questions wherein you need to select the right one."

    n "The game comprises of 5 main stories. However there is a twist."

    n "To unlock a special route in the main stories, you must achieve a certain number of points."

    n "Selecting the {color=#f00}most correct{/color} decision will grant you the most points."

    show natasha closed eyes_ with dissolve

    n "I'll give an example!"

    show natasha talk with dissolve

    n "You see me passing in an alleyway. Then some random old men started catcalling on me."

    show natasha cry with dissolve

    n "I feel so scared because of what they did."

    pause 1.0
    menu whatToDo:
        "What would you do?"

        "Take out my phone and record.":
            n "Honestly this is not a bad answer. But are you just gonna let me get harrassed?"

            n "This can be a traumatic experience for me."

            n "For this answer, I will reward you 2 HBB points."

            show natasha closed eyes_ with dissolve

            n "Try it again."

            jump whatToDo

        "Shout at the old men.":
            n "Not the answer I was expecting."

            n "They might beat you up, you know?"

            n "For this answer, I will reward you 1 HBB point."

            show natasha closed eyes_ with dissolve

            n "Try it again."

            jump whatToDo

        "Talk to them calmly and call the police if they don't stop.":
            show natasha closed eyes_ with dissolve
            n "I think this is the best answer."

            show natasha talk with dissolve

            n "For this answer, I will reward you 3 HBB points."

            n "You saved me from them and prevented them from doing anything."

            show natasha blush with dissolve

            n "I might fall for you, you know?"

            show natasha closed eyes_ with dissolve

            n "Just kidding!!!"


    stop music fadeout 3.0
    pause 2.0
    jump yui_start_case_1
    