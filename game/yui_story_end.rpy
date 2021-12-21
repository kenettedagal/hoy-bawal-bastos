#Check if special route unlocked

label yui_end:

    scene bg beautiful park 
    show natasha talk
    with fade
    
    $ play_music (tutorial)
    # if perfect points + Yui route

    # n "Congratulations! You unlocked the secret ending route!"

    # n "Congratulations! You achieved the good ending route!"
 
    # # if not perfect points

    # n "Based on my calculations, you have not achieved the amount of points to unlock it."

    # n "Do you wanna try again or proceed to next story?"

    if badEndingGame:


        n "Hellooooooo!"

        n "I'm really sad to say that you reached the \"Bad End\" route."

        python:

            if achievementList[10] == False:
                    
                achievement.grant("Bad End")
                renpy.notify("Achievement Unlocked: Bad End")
                renpy.play("audio/sfx/achievement.ogg",channel="sound")
                achievementList[10] = True

        n "It's okay! It's not over yet. You can try again or proceed to the next story."

        n "If you try again, I will give you hint to reach the good ending. Sounds good?"

        n "What do you want to do?"

        menu:
            n "What do you want to do?"

            "Try it again.":

                n "Great choice! Now here is the hint."

                n "You have to take the train, save the girl and help her."

                n "Once you reach the amount of points required, you will unlock the secret ending! Goodluck!"

                jump yui_start_case_1

            "Proceed to next story.":

                n "It's fine. You can try this story again once you feel like doing it."

                jump Act_2_School

    elif goodEnding:
        
        n "Congratulations! You achieved the good ending route!"

        python:

            if achievementList[11] == False:
                    
                achievement.grant("Good End")
                renpy.notify("Achievement Unlocked: Good End")
                renpy.play("audio/sfx/achievement.ogg",channel="sound")
                achievementList[11] = True

        n "Was it a fun ride? Ahahaha~"

        n "Let me see if you achieved the points to unlock the secret ending..."

        if hbbpoints >= 20:

            $ timeout_label = None

            play sound "audio/sfx/addPoints.mp3"

            n "Congratulations! You unlocked the secret ending route!"

            python:

                if achievementList[12] == False:
                        
                    achievement.grant("Special End")
                    renpy.notify("Achievement Unlocked: Special End")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    achievementList[12] = True

            n "Do you want to play the secret ending? Or proceed to the next story?"

            n "You can go back and play the secret ending whenever you want."

            menu: 
                "What do you want to do?"

                "Take me to the secret ending!":
                    ""

                "Proceed to next story!":
                    ""
                    jump Act_2_School

        else:
            n "Unfortunately you did not qualify for the Special Ending..."

            n "Do you want to try again or proceed to the next story?"

            n "If you try again, I will give you hint to reach the secret ending. Sounds good?"

            n "What do you want to do?"

            menu:

                "Try it again.":
                    n "Great choice! Now here is the hint."

                    n "You have to atleast achieve a score of 20 points and help the girls."

                    n "Once you reach the amount of points required, you will unlock the secret ending! Goodluck!"

                    jump yui_start_case_1

                "Return to Main Menu":
                    n "It's fine. You can try this story again once you feel like doing it."

                    jump splashscreen


    # elif friendEnding:
    #     n "Congratulations! You achieved the good ending route!"

    #     n "There is still a secret ending route which you can unlock. Do you want to try again or proceed to the next story.?"

    #     n "If you try again, I will give you hint to reach the secret ending. Sounds good?"

    #     menu:
    #         n "What do you want to do?"

    #         "Try it again.":
    #             n "Great choice! Now here is the hint."

    #             n "You have to take the train, save the girl and help her."

    #             n "Once you reach the amount of points required, you will unlock the secret ending! Goodluck [player]!"

    #         "Proceed to next story.":
    #             n "It's fine. You can try this story again once you feel like doing it."
        




    