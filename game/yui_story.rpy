image kitchen = im.Scale("images/bg kitchen.webp", 1920, 1080)
image outside = im.Scale("images/bg outside.webp", 1920, 1080)

define kk = Character('Kurt')

label yui_start_case_1:
    define mm = Character('Mom')
   

    scene black
    centered "Story #1\n\n\nYui's Melancholy"
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
    pause 1.0
    "....."
    play sound "audio/doorknock.mp3"
    pause 2.0

    "{i}Yawns...{/i}"

    m "Yes mom... Please stop knocking on the door."

    show mom worried at left with dissolve

    mm "It's your first day at school honey..."

    mm "I told you to sleep early last night. Did you play games all night again?"

    m "Ehehe......"

    scene kitchen with fade
    show mom happy at left with dissolve

    mm "Go now and eat breakfast with me. Your father left early for work."

    m "What did you cook for breakfast [mm]?"

    show mom happy closed at left with dissolve
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
            
    m "Thank you for the food, Mom!"

    show mom happy at left with dissolve
    
    mm "No worries! It's gonna be a big day for you honey."

    "...."

    menu:
        "I should first look at some news before leaving..."

        "Grab the newspaper.":
            play sound "audio/newspaper.wav"
            pause 0.5
            jump law

        "Open the TV.":
            play sound "audio/tv.wav"
            pause 0.5
            jump law


label law:
    
    scene black

    centered "\“On the 17th of April Year 2019, a new law called {color=#f00}{b}Republic Act No. 11313{/b}{/color} 
    or also known as {color=#f00}{b}Safe Spaces Act{/b}{/color} has been approved by the President.\"" 

    centered "This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions……"

label goingToSchool:

    scene outside with fade
    "Well, that was a great law. Hopefully I can teach someone about it."

    "Hmmm. As expected, there will be a class introduction soon. How should I introduce myself?"

    "Ehem....."

    "\"How y'all doin' everyone! The greatest future lawyer is in this class. The name's Mark!\""

    "How's that? Hmmm..."

    "No... that's... way too embarassing."

    "How about..."

    "\"Pleased to meet you everyone. Please call me Mark. I love anime and manga.\""

    "...."

    "Yeah that'll work. Short and simple."
    
    "They don't need to know that I am dreaming to be a lawyer someday."

    "{i}8:15 AM...{/i}"

    "Oh!!! I didn't notice the time at all."

    "Should I take a jeep or train today?"

    menu:
        
        # Meet Yui
        "Take the train.":
            jump meetWithYui

        # Meet Kurt
        "Ride a jeep.":
            jump meetWithKurt


label meetWithKurt:
    scene bg jeep n with fade
    
    "Mark!"

    "Mark!!!"

    "Uhmm someone is calling me?"

    "From where?"

    "???" "Dude! Are you deaf?"

    "Bam!!" with vpunch

    "Ouch that hurts..."

    m "Oh.. it is you Kurt!"

    show kurt happy with dissolve

    m "Why'd you hit me in the back of my head?"

    kk "Dude you almost rode the jeep without me."

    m "Sorry I didn't notice you at all."

    kk "Well its fine. Atleast I'm going to school with you."

    "This is Kurt. My weird friend. Our friendship started weird. This guy randomly talked to me when I was eating alone in cafeteria."

    "But I don't hate it at all."

    kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"

    m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

    kk "You poor little thing."

    m "Well, don't even talk like you have one."

    kk "Hahaha~ Don't worry about me. I'm more worried about your future."

    m "I'm not a child for you to worry about."

    jump schoolCeremony


label meetWithYui:
    scene bg train with fade

    "Eh, it is surprisingly quiet today..."

    "Even though its the first day of class?"

    "Well, I shouldn't be complaining about this."

    "I kinda like this atmosphere."

    "Hopefully, this day goes successful."

    
    

label schoolCeremony:

return
