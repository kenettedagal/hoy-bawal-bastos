label tutorial_start:
    # Ask user some questions aboutn VN, Safe Spaces, etc.

    define n = Character('Natasha')
    
    "Hello! Welcome to our visual novel game...."

    n "My name is Natasha and I will be your guide before you start playing!"

    python:
        player = renpy.input("What is your first name?", length=32)
        player = player.strip()

        if not p:
            p = "Shy Guy"

    n "Hello [player]!"

    n "This visual novel game was created with the idea of educating people about Safe Spaces Act in an entertaining fashion!"

    n "Now before you start playing, I will first ask some questions."

    menu:
        n "Have you ever played a visual novel game before?"

        "Yes, I've played some before.":
            n "Great! I see that you are a man/woman of culture as well!"

        "No, not yet."
            n "Great! Let's explore together the world of visual novels!"

            n "It's like an interactive book that you can read on a computer or a console."

            n "You can make choices that lead to different events and endings in the story."

            "Tell me more.":
                n "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

            "So where does the \"visual\" part come in?":
                n "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    n "Now that you have a some knowledge on visual novels..."

    menu:
        n "Do you know anything about the law called \"Safe Spaces Act\"?"

        "I have no idea.":
            n "That is absolutely fine! Together, we will learn about the Safe Spaces Act through this visual novel."
            n "Learning this law will definitely help you in some way!"

        "I've heard about it before.":
            n "That is magnificent! The extra knowledge that you'll learn here will definitely help you!"


        


    return