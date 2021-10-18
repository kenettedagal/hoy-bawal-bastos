image kitchen = im.Scale("images/bg kitchen.webp", 1920, 1080)

label yui_start_case_1:
    define mm = Character('Mom')
   

    scene black
    #Play iphone alarm tone

    pause 2.0
    play sound "audio/iphone.ogg" 

    scene bg room morning with fade
    

    "{i}7:00 AM....{/i}"
    
    "Ugh...."

    "Shut up Siri."

    "......"

    menu:

        "Snooze alarm for 5 minutes":

            scene black
            "Zzzzzz...."

            pause 2.0
            play sound "audio/iphone.ogg"

            scene bg room morning with dissolve

            "{i}7:27 AM....{/i}"

            play music "audio/Time for Rest.ogg" fadein 0.3 volume 0.2

            m "NO WAY!!! I ALMOST SLEPT FOR ANOTHER 30 MINUTES!"

            jump breakfastWithMom
        
        "Get up and fix the bed":
            
            play music "audio/Time for Rest.ogg" fadein 0.3 volume 0.2  
            
            scene bg room morning with dissolve

            "Another day, another dollar..."

            jump breakfastWithMom


label breakfastWithMom:

    mm "Mark! Are you awake?"

    play sound "audio/doorknock.mp3"
    "....."
    play sound "audio/doorknock.mp3"

    "{i}Yawns{/i}"

    m "Yes mom... Please stop knocking on the door."

    mm "It's your first day at school..."

    mm "I told you to sleep early last night. Did you play games all night again?"

    m "Ehehe......"

    scene kitchen with fade

    mm "Go now and eat breakfast with me. Your father left early for work."

    m "What did you cook for breakfast [mm]?"

    mm "I made your favorite foods! A scrambled egg, tocino and some bacon."

    menu: 

        mm "What do you wanna eat?"

        "Scrambled eggs.":
            m "Nothing beats [mm]'s scrambled eggs."

        "Tocino":
            m "The sweet taste of tocino means a very good morning."

        "Bacon":
            m "Crispy and juicy bacon. The best breakfast food invented."

        "Ofcourse, all of it!":
            m "All of these dishes in one plate..."
            m "I hope my stomach won't hurt when I'm outside. Haha...."
            
    m "Thank you for the food!"

    "...."

    menu:
        "I should first look at some news before leaving..."

        "Grab the newspaper.":
            jump law

        "Open the TV.":
            jump law

label law:
    
    scene black

    centered "\“On the 17th of April Year 2019, a new law called {color=#f00}{b}Republic Act No. 11313{/b}{/color} 
    or also known as {color=#f00}{b}Safe Spaces Act{/b}{/color} has been approved by the President.\"" 

    centered "This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions……"

label goingToSchool:



    return