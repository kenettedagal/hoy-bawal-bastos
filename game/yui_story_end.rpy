#Check if special route unlocked

label yui_end:

    scene endScreen
    show natasha talk
    with fade
    
    # if perfect points + Yui route

    n "Congratulations! You unlocked the secret ending route!"

    n "Congratulations! You achieved the good ending route!"
 
    # if not perfect points

    n "Based on my calculations, you have not achieved the amount of points to unlock it."

    n "Do you wanna try again or proceed to next story?"

    if badEndingGame:
        n "Hellooooooo! [player]"

        n "I'm really sad to say that you reached the \"Bad End\" route."

        n "It's okay! It's not over yet. You can try again or proceed to the next story."

        n "If you try again, I will give you hint to reach the secret ending. Sounds good?"

        n "What do you want to do?"

        menu:
            n "What do you want to do?"

            "Try it again.":
                n "Great choice! Now here is the hint."

                n "You have to take the train, save the girl and help her."

                n "Once you reach the amount of points required, you will unlock the secret ending! Goodluck [player]!"

            "Proceed to next story.":
                n "It's fine. You can try this story again once you feel like doing it."

    elif friendEnding:
        n "Congratulations! You achieved the good ending route!"

        n "There is still a secret ending route which you can unlock. Do you want to try again or proceed to the next story.?"

        n "If you try again, I will give you hint to reach the secret ending. Sounds good?"

        menu:
            n "What do you want to do?"

            "Try it again.":
                n "Great choice! Now here is the hint."

                n "You have to take the train, save the girl and help her."

                n "Once you reach the amount of points required, you will unlock the secret ending! Goodluck [player]!"

            "Proceed to next story.":
                n "It's fine. You can try this story again once you feel like doing it."
        




    