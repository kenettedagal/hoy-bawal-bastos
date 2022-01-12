label yui_start_case_1:
    image kitchen = im.Scale("images/bg kitchen.webp", 1920, 1080)
    image outside = im.Scale("images/bg outside.webp", 1920, 1080)
    image aerial = im.Scale("images/school aerial.webp", 1920, 1080)
    image hallway = im.Scale("images/hallways.webp", 1920, 1080)
    image pools = im.Scale("images/pool.webp", 1920, 1080)
    image classroom lunch1 = im.Scale("images/classroom lunch.webp", 1920,1080)  
    image classroom2 = im.Scale("images/classroom_2.webp",1920,1080)
    image classroom morning = im.Scale("images/classroom_morning.webp",1920,1080)
    image walk = im.Scale("images/walk1.webp", 1920, 1080)
    image school gate = im.Scale("images/school gate1.webp", 1920, 1080)

    define kk = Character('Kurtney',color='#51ceff',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    define y = Character('Yui',color='#f9b3ff',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    define t = Character('Teacher Clarisse',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    define b = Character('Butch',color='#badb27',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    define o = Character('Officer Greg', color='#30ff45',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    define mc = Character("Mark",ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    define m = Character("Mark",color='#00ffea',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")

    default notebookOpen = False
    default hbbpoints = 0
    default yuiStoryProgress = 0
    default notebookIndex = 0
    define mm = Character('Mom',color='#00ff2a',ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
    default badEndingGame = False
    default kurtneyHelp = False
    default persistent.achievementList = [False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False, False]
    default persistent.unlockroom = False
    default persistent.unlockTrain = False
    default persistent.unlockJeep = False
    default persistent.unlockHallway = False
    default persistent.unlockTrain2 = False
    default persistent.unlockWalk = False
    default persistent.unlockCafeteria = False
    default persistent.unlockClass = False
    default persistent.unlockYui = False
    default persistent.unlockKurtney = False
    default kurtneySpecial = False
    default yuiSpecial = False

    init python:
        
        def subtractPoints():
            global hbbpoints
            if hbbpoints >= 1:
                hbbpoints -= 1
                play_sound(subPoints)
                "Your points are deducted by 1 HBB Point"

    #Disclaimer & Company Logo
    $ quick_menu = False
    stop music
    $_dismiss_pause = False
    scene black with fade
    with Pause(1)

    scene disclaimer with dissolve
    with Pause(7)

    scene black with fade
    with Pause(1)

    show logo_company with dissolve
    with Pause(4)

    scene black with fade
    with Pause(1)

    #START OF YUI STORY
    stop music
    hide screen displayHBBPoints
    scene school gate with fade
    play music "audio/music/Piano6.ogg"
    show screen titleYui with dissolve
    pause 0.5
    
    #Play iphone alarm tone
    pause 2.0
    hide screen titleYui with dissolve
    pause 0.5
    stop music
    
    $ quick_menu = True
    
    $ preferences.set_volume("sfx", 1.0)
    $ play_sound (phone) 

    scene bg room2 with fade


    "{i}7:00 AM....{/i}"
    $ preferences.set_volume("voice", 0.50)
    voice "bm0.ogg"
    "Ugh...."
    
    $ preferences.set_volume("sfx", 0.30)
    python:

        if persistent.achievementList[0] == False:
        
            achievement.grant("A New Leaf")
            renpy.notify("Achievement Unlocked: A New Leaf")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[0] = True

    $ persistent.unlockroom = True

    pause 1.9
    voice "bm1.ogg"
    "Shut up Siri."

    "......"
    $ timeout_label = "snooze"
    $ timeout = 10

    $ preferences.set_volume("music", 0.20)
    $ preferences.set_volume("voice", 0.30)
    menu:

        "Snooze alarm for 5 minutes":
            jump snooze
            
        
        "Get up and fix the bed":
            
            $ play_music (rest, fadein=0.3) 
            
            scene bg room2 with dissolve

            voice "bm2.ogg"
            "Another day, another dollar..."

            jump breakfastWithMom


label snooze:
    scene black
    $ preferences.set_volume("voice", 0.40)
    voice "bm3.ogg"
    "Just a few more minutes...."

    "Zzzzzz...."

    pause 2.0
    $ preferences.set_volume("sfx", 1.0)
    $ play_sound (phone)
    
    scene bg room2 with dissolve

    "{i}7:27 AM....{/i}"

    $ play_music (rest, fadein=0.3) 

    voice "m1.ogg"
    $ preferences.set_volume("voice", 0.50)
    m "NO WAY!!! I ALMOST SLEPT FOR ANOTHER 30 MINUTES!"
    $ preferences.set_volume("sfx", 0.50)
    jump breakfastWithMom


label breakfastWithMom:

    scene black 
    show mark
    with fade
    pause 2.0 
    window hide
    $ preferences.set_volume("voice", 0.35)
    hide mark with dissolve
    voice "bm4.ogg"
    centered "My name is {color=#00ffea}Markkuss{/color}. I know it is a weird name so I told my friends and family to just call me {color=#00ffea}Mark.{/color}"

    voice "bm5.ogg"
    centered "Today marks the day of me being a Second-Year highschool student."

    voice "bm6.ogg"
    centered "I am your average highschool boy if you wanna know."

    voice "bm7.ogg"
    centered "I barely pass my subjects but I'm also quite decent at sports."

    voice "bm8.ogg"
    centered "Gotta brag when you gotta brag. Hahaha~"

    voice "bm9.ogg"
    centered "Becoming an Attorney is my dream."

    voice "bm10.ogg"
    centered "You know why?"

    voice "bm11.ogg"
    centered "Cause I have played lots of detective games!"

    voice "bm12.ogg"
    centered "Hahaha I know its nonsense but still..."

    voice "bm13.ogg"
    centered "Anyways! My hobbies are sleeping and watching anime."

    $ preferences.set_volume("voice", 0.45)
    voice "bm14.ogg"
    centered "Wait is this even called hobbies? It's more of a \"I've got nothing else to do in life.\""

    voice "bm15.ogg"
    centered "Well...."

    voice "bm16.ogg"
    centered "Nothing eventful has happened yet in my life."

    voice "bm17.ogg"
    centered "I haven't even experienced the so called \"romance of highschool.\""

    voice "bm18.ogg"
    centered "I wonder if it starts now? Hahaha~"

    scene bg room2 with fade

    "....."
    $ preferences.set_volume("voice", 0.40)
    voice "mm1.ogg"
    mm "Mark! Are you awake?"
    $ preferences.set_volume("sfx", 0.50)
    $ play_sound (doorknock) 
    pause 0.5
    with hpunch
    
    "....."
    $ play_sound (doorknock)
    pause 0.5
    with hpunch

    pause 3.0

    $ preferences.set_volume("sfx", 0.70)

    $ play_sound(yawn)

    pause 2.0
    
    $ preferences.set_volume("voice", 0.35)
    $ preferences.set_volume("music", 0.20)
    voice "m2.ogg"
    m "Oh yes. It definitely starts with my mom's yelling in the morning."
    $ preferences.set_volume("voice", 0.40)
    voice "m3.ogg"
    m "Yes mom... Please stop knocking on the door."

    show mom worried at left with dissolve
    voice "mm2.ogg"
    mm "It's your first day at school honey..."

    voice "mm3.ogg"
    mm "I told you to sleep early last night. Did you play games all night again?"

    voice "m4.ogg"
    m "Ehehe......"

    scene kitchen with fade
    show mom happy at left with dissolve
    $ preferences.set_volume("voice", 0.45)
    voice "mm4.ogg"
    mm "Go now and eat breakfast with me. Your father left early for work."

    voice "m5.ogg"
    m "What did you cook for breakfast [mm]?"

    show mom happy closed at left with dissolve
    voice "mm5.ogg"
    mm "I made your favorite foods! A scrambled egg, tocino and some bacon."
    $ timeout_label = None
    hide mom happy with dissolve
    $ preferences.set_volume("voice", 0.40)
    $ preferences.set_volume("sfx", 0.40)
    menu: 
        
        # voice "mm6.ogg"
        mm "What do you wanna eat?"

        "Scrambled eggs.":
            voice "m6.ogg"
            m "Nothing beats [mm]'s scrambled eggs."

        "Tocino":
            voice "m7.ogg"
            m "The sweet taste of tocino means a very good morning."

        "Bacon":
            voice "m8.ogg"
            m "Crispy and juicy bacon. The best breakfast food invented."

        "Of course, all of it!":
            voice "m267.ogg"
            m "All of these dishes in one plate..."
            voice "m9.ogg"
            m "I hope my stomach won't hurt when I'm outside. Haha...."
            
            python:
                if persistent.achievementList[1] == False:


                    achievement.grant("I Love Mom's Breakfast")
                    renpy.notify("Achievement Unlocked: I Love Mom's Breakfast")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    persistent.achievementList[1] = True
                    renpy.pause(1.5)
            
            show mom worried with dissolve
            voice "mm7.ogg"
            mm "I hope so too! Ahahaha~"
            hide mom worried with dissolve
    $ preferences.set_volume("sfx", 0.99)
    $ play_sound(eat,fadein=0.5)
    "{i}Munch munch munch....{\i}"
    pause 8
    $ preferences.set_volume("voice", 0.90)        
    voice "m10.ogg"
    m "Thank you for the food, Mom!"
    $ preferences.set_volume("sfx", 0.50)
    show mom happy at left with dissolve
    $ preferences.set_volume("voice", 0.50)   
    voice "mm8.ogg"
    mm "No worries! It's gonna be a big day for you honey."

    "...."

    hide mom happy with dissolve
    $ law = ''
    $ preferences.set_volume("sfx", 0.30)
    menu:
        "I should first look at some news before leaving..."

        "Grab the newspaper.":
            $ play_sound (paper)
            pause 0.5
            $ law = 'paper'
            
            python:

                if persistent.achievementList[2] == False:
                
                    achievement.grant("Newspaper Guy")
                    renpy.notify("Achievement Unlocked: Newspaper Guy")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    persistent.achievementList[2] = True

            jump law

        "Open the TV.":
            $ play_sound (tv)
            pause 0.5
            $ law = 'tv'
            python:

                if persistent.achievementList[3] == False:
                
                    achievement.grant("TV Guy")
                    renpy.notify("Achievement Unlocked: TV Guy")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    persistent.achievementList[3] = True
            jump law


label law:
    
    scene black

    $ yuiStoryProgress += 1

    if law == 'paper':

        show image "images/paper1.png" with dissolve
        pause 3.0
        hide image "images/paper1.png" with dissolve
        play sound "audio/sfx/newspaper.wav" 
        show image "images/ssacover.jpg" with dissolve
        pause 3.0
        play sound "audio/sfx/newspaper.wav"
        hide image "images/ssacover.jpg"
        show image "images/cnnssa.jpg" with dissolve
        pause 3.0
        play sound "audio/sfx/newspaper.wav"
    
    else:
        show image "images/tv.jpg" with pixellate
        pause 3.0
        hide image "images/tv.jpg" with dissolve
        show image "images/ssacover.jpg" with dissolve
        pause 3.0
        show image "images/cnnssa.jpg" with dissolve
        pause 3.0
        hide image "images/cnnssa.jpg"
        show image "images/duterte.jpg" with dissolve
        pause 3.0
        hide image "images/duterte.jpg" 
         
    
    # Show punishments

    show image "images/punishment1.jpg" with dissolve
    pause 3.0
    show image "images/punishment2.jpg" with dissolve
    pause 3.0




    # centered "\“On the 17th of April Year 2019, a new law called {color=#f00}{b}Republic Act No. 11313{/b}{/color} 
    # or also known as {color=#f00}{b}Safe Spaces Act{/b}{/color} has been approved by the President.\""

    # centered "The Safe Spaces Act is an act defining gender-based sexual harassment 
    # in streets, public spaces, online, workplaces, and educational or training institutions."  

    # centered "This law stated that both men and women must have equality, 
    # security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    # and educational and training institutions."

    scene kitchen with fade

    "This is a really great law. I should probably take some notes of this law..."

    show screen newNote with fade

    pause 1.5

    show screen showNotesButton with dissolve

    "If you look at the top right part of the screen, there is a button."

    "This button will log important parts of the law. So always check it out~"

    stop music fadeout 0.5

    $ renpy.end_replay()
    

label goingToSchool:

    scene outside with fade

    $ play_music(poppy)

    voice "bm19.ogg"
    "Well, that was a great law. Hopefully I can teach someone about it."

    voice "bm20.ogg"
    "Hmmm. As expected, there will be a class introduction soon. How should I introduce myself?"

    voice "bm21.ogg"
    "Ehem....."

    voice "bm22.ogg"
    "\"How y'all doin' everyone! The greatest future attorney is in this class. The name's Mark!\""

    voice "bm23.ogg"
    "How's that? Hmmm..."

    voice "bm24.ogg"
    "No... that's... way too embarassing."

    voice "bm25.ogg"
    "How about..."

    voice "bm26.ogg"
    "\"Pleased to meet you everyone. Please call me Mark.\""

    "...."

    voice "bm27.ogg"
    "Yeah that'll work. Short and simple."
    
    voice "bm28.ogg"
    "They don't need to know that I am dreaming to be an attorney someday."

    "{i}8:15 AM...{/i}"

    $ play_sound(carleave,fadein=1.5)

    pause 2.0 
    "Should I take a jeep or train today?"
    $ timeout = 8
    $ timeout_label = "meetWithKurt"
    show screen displayHBBPoints 
    menu:
        # Story will diverge from this point. Will converge at some point.
        "Should I take a jeep or train today?"
        
        # Meet Yui
        "Take the train.":

            
            $ metYui = True
            $ renpy.end_replay()
            jump meetWithYui

        # Meet Kurt(friend)
        "Ride a jeep.":

            $ renpy.end_replay()
            jump meetWithKurt

    


label meetWithKurt:
    $ persistent.unlockKurtney = True
    stop music
    pause 0.5
    play sound "audio/music/Piano2.ogg"fadein 0.3
    scene school gate 
    show screen jeepTransition 
    with fade
    pause 3.0
    hide screen jeepTransition with dissolve
    $ play_music(relax, fadein=8)
    $ metYui = False
    scene bg jeep n with fade
    $ persistent.unlockJeep = True

    python:

        if persistent.achievementList[5] == False:
                
            achievement.grant("Bayad Po")
            renpy.notify("Achievement Unlocked: Bayad Po")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[5] = True

    pause 3.0
    $ preferences.set_volume(channel="sound", 0.5)
    $ play_sound(people,fadein=0.2,fadeout=5.0) 
    pause 5
    
    "Mark!"

    "Mark!!!"

    "Dude!!"

    $ play_sound(carleave,fadein=0.5)


    "Uhmm someone is calling me?"

    "From where?"

    
    "???" "Dude! Are you deaf?"

    $ play_sound(punch,fadein=0.5)
    "Bam!!" with vpunch

    "Ouch that hurts..."

    voice "m11.ogg"
    m "Oh.. it is you [kk]!"

    show kurtney happy teeth with dissolve

    voice "m12.ogg"
    m "Why'd you hit me in the back of my head?"

    show kurtney angry talk with dissolve

    voice "kk2.ogg"
    kk "Dude you almost rode the jeep without me."

    voice "m13.ogg"
    m "Sorry I didn't notice you at all."

    show kurtney smile zorder 3 with dissolve

    voice "kk3.ogg"
    kk "Well its fine. Atleast I'm going to school with you."

    $_dismiss_pause = False
    show movie intro at offscreenleft
    show ymagenta zorder 2 at offscreenright
    with ease
    
    play sound "audio/fast.wav" volume 0.5

    show movie intro at left
    show ymagenta zorder 2 at right
    with ease

    show k name zorder 3 at offscreenright
    with ease

    play sound "audio/ting.wav"

    show kurtney happy teeth zorder 3 at left
    show k name zorder 3 at left
    with MoveTransition(0.4)

    voice "bm51.ogg"
    "This is [kk]. My weird childhood friend."

    voice "bm52.ogg"
    "We have been friends since elementary school. She is a little boyish and sometimes annoying."

    voice "bm53.ogg"
    "But I don't hate it at all."

    play sound "audio/fast.wav" volume 0.5

    $_dismiss_pause = False
    show movie intro at offscreenright
    show ymagenta zorder 2 at offscreenleft  
    with ease
    
    show kurtney smile zorder 3 at center
    show k name zorder 2 at offscreenright
    with MoveTransition(0.2)
    $ renpy.pause(0.3, hard=True)

    show kurtney talk opened with dissolve

    voice "kk4.ogg"
    kk "Did you know? Something crazy happened to me today. Good thing I found you."

    voice "m143.ogg"
    m "What happened?"

    voice "kk5.ogg"
    kk "There was this guy... standing at the corner of our street."

    voice "kk6.ogg"
    kk "He looked unfamiliar to me so I asked him if he was looking for someone or he got lost."

    voice "m15.ogg"
    m "So? Was he lost or what?"

    show kurtney angry talk with dissolve

    voice "kk7.ogg"
    kk "Crazy freaking dude told me, \"You look beautiful today as well.\""

    voice "m16.ogg"
    m "That's sexual harassment..."

    voice "m17.ogg"
    m "What does he look like?"

    voice "kk8.ogg"
    kk "He wears a hoodie and a sweat pants."

    voice "m18.ogg"
    m "Let me know when you see this guy again."

    show kurtney happy teeth with dissolve

    voice "kk9.ogg"
    kk "Thanks dude! I'm lucky I have someone like you."

    voice "kk10.ogg"
    kk "Ohhhh and speaking of you..."

    voice "kk11.ogg"
    kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"

    voice "m215.ogg"
    m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

    show kurtney happy teeth with dissolve

    voice "kk12.ogg"
    kk "You poor little thing. Don't worry, I'll always be here for you so you don't look like a loser."

    voice "m216n.ogg"
    m "Well, don't even talk like you have one."

    voice "kk13.ogg"
    kk "Hahaha~ Don't worry about me. I'm more worried about your future."

    voice "m217n.ogg"
    m "I'm not a child for you to worry about."

    voice "kk14.ogg"
    kk "Haha!!"

    voice "m22.ogg"
    m "Hey, do you wanna hear something interesting?"

    voice "m23.ogg"
    m "It is related to what happened to you earlier."

    show kurtney talk opened with dissolve

    voice "kk15.ogg"
    kk "What? If it's boring then I'm not listening to you."

    #show kurt without headphone

    voice "m24.ogg"
    m "I saw the news this morning. There was a new law.."

    voice "kk16.ogg"
    kk "What kind of law?"

    hide kurtney talk opened with dissolve

    $ firstTryWrong = False
    $ timeout = 15
    $ timeout_label = "kurtFirstQuestionTimerOut"

    menu kurtFirstQuestion:
        # voice "bm43.ogg"
        "Aaaaah... What is it again? The law that was approved on 17th of April, 2019?"

        "Re-semiprivate Act No. 11313":
            "Wrong answer!"
            $ firstTryWrong = True
            jump kurtFirstQuestion

        "Reprivate Act No. 11313":
            "Think again..."
            $ firstTryWrong = True
            jump kurtFirstQuestion

        "Republic Act No. 11313":
            "Correct!!"
            if firstTryWrong is False:

                $ hbbpoints += 3
                $ play_sound(addPoints)
                "You received {color=#40ff00}3 HBB Points.{/color}"
            jump kurtIntroSecond

        "Rebuild Act No. 11313":
            "Not the right answer."
            $ firstTryWrong = True
            jump kurtFirstQuestion

    label kurtFirstQuestionTimerOut:
        $ firstTryWrong = True
        voice "m25.ogg"
        m "Republic Act No. 11313"

    #######################################

    label kurtIntroSecond:
        show kurtney happy teeth with dissolve
        voice "kk17.ogg"
        kk "That's cool. Tell me more about it."

        voice "m26.ogg"
        m "Yeah its a great law."

        voice "m27.ogg"
        m "It is also known as ...."

        hide kurtney happy teeth with dissolve

        $ firstTryWrong = False
        $ timeout = 15
        $ timeout_label = "kurtSecondQuestionTimerOut"

    menu kurtSecondQuestion:
        "It is also known as ...."
        
        "Safe Spaces Act":
            "Great answer!"
            if firstTryWrong is False:
                $ hbbpoints += 3
                $ play_sound(addPoints)
                "You received {color=#40ff00}3 HBB Points.{/color}"
            jump kurtIntroThird
            
        "Safe Pace Act":
            "Wait this is wrong."
            $ firstTryWrong = True
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
            jump kurtSecondQuestion
        
        "Safe Guardian Act":
            "Not the right answer."
            $ firstTryWrong = True
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
            jump kurtSecondQuestion
       
        "Safe Insurrance Act":
            "Not the greatest answer."
            $ firstTryWrong = True
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"      
            jump kurtSecondQuestion

    label kurtSecondQuestionTimerOut:
        $ firstTryWrong = True
        $ subtractPoints()
        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
        voice "m98.ogg"
        m "Safe Spaces Act"

    label kurtIntroThird:

        show kurtney talk opened with dissolve
        voice "kk18.ogg"
        kk "So it is called \"Safe Spaces Act\"?"

        voice "m28.ogg"
        m "Yeah! It's a cool name right."

        #show kurt open mouth
        voice "kk19.ogg"
        kk "Sure. But what does it mean?"

        $ firstTryWrong = False
        $ timeout = 10
        $ timeout_label = "kurtInfo"

        hide kurtney talk opened with dissolve 

    menu kurtThirdQuestion:
        # voice "bm45.ogg"
        "Wait, what does the Safe Spaces Act mean again?"

        "To protect Earth from aliens.":
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"        

            voice "m29.ogg"
            m "To protect Earth from aliens."

            show kurtney angry talk with dissolve

            voice "kk20.ogg"
            kk "Dude are you serious?"

            voice "kk21.ogg"
            kk "Stop spouting nonsense."
            
            voice "m30.ogg"
            m "Hahaha~ I'm just kidding!"

            voice "m31.ogg"
            m "The law was created to..."
            

            jump kurtInfo

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
        "To protect men and women from gender-based sexual harassment.":
            "Nice job! Correct answer."
            $ hbbpoints += 3
            $ play_sound(addPoints)
            "You received {color=#40ff00}3 HBB Points.{/color}"

            pause 0.5 

            if hbbpoints == 9:
                python:

                    if persistent.achievementList[6] == False:
                    
                        achievement.grant("Ace Attorney")
                        renpy.notify("Achievement Unlocked: Ace Attorney")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[6] = True
            
            label kurtInfo:
                $ yuiStoryProgress += 1

                hide kurtney angry talk with dissolve

                voice "m191.ogg"
                m "To protect men and women from gender-based sexual harassment."

                voice "m32.ogg"
                m "Gender-based streets and public spaces sexual harassment include..."

                voice "m33.ogg"
                m "a) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs."

                voice "m34.ogg"
                m "b) Persistent uninvited comments or gestures on a person's appearance."

                voice "m35.ogg"
                m "c) Relentless requests for personal details."

                voice "m36.ogg"
                m "d) Statement of sexual comments and suggestions."

                voice "m37.ogg"
                m "e) Public masturbation or flashing of private parts, groping, making offensive body gestures 
                at someone, and other similar lewd sexual actions."

                voice "m38.ogg"
                m "f) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. 
                This may include cursing, leering and intrusive gazing, and taunting."

                voice "m39.ogg"
                m "g) Persistent telling of sexual jokes, use of sexual names."

                voice "m40.ogg"
                m "And last but not the least."
                
                voice "m41.ogg"
                m "h) Stalking."

                show screen newNote with fade
                pause 1.0

                show kurtney talk opened with dissolve

                voice "kk22.ogg"
                kk "That was a lot! How'd you memorize it?"

                voice "m42.ogg"
                m "Well you know... I wanted to be an attorney. So this much is not that big deal."

                show kurtney happy teeth with dissolve

                voice "kk23.ogg"
                kk "Attorney Mark? Sounds nice haha~"

                voice "m43.ogg"
                m "Stop mocking me dude."

                show kurtney talk opened with dissolve

                voice "kk24.ogg"
                kk "So what happens when I do any of those things?"

                voice "m44.ogg"
                m "Let's continue later dude. We are close to the school."

                show kurtney smile with dissolve

                voice "kk25.ogg"
                kk "Tell me about it okay? It's an interesting law."

                

        "To protect public and online spaces from danger.":
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"

            voice "m45.ogg"
            m "To protect public and online spaces from danger."

            show kurtney angry talk with dissolve

            voice "kk26.ogg"
            kk "What danger? Explain it clearly."

            voice "m46.ogg"
            m "Uhhhh.. wait let me remember..."

            voice "m47.ogg"
            m "Errr... it is to..."

            jump kurtInfo

        ########################################
    $ renpy.end_replay()

    label confrontation:

        stop music
        pause 0.5
        play sound "audio/music/Piano5.ogg"fadein 0.3
        scene walk
        show screen stalkerTransition 
        with fade
        pause 3.0
        hide screen stalkerTransition with dissolve
        $ play_music(Lurking, fadein=8)
        $ persistent.unlockWalk = True

        $ play_sound(walking,fadein=0.3,fadeout=5.0)
        scene black with fade

        "A peaceful morning for a first day of school."

        "Or so I thought..."
        scene walk with fade

        show kurtney happy teeth with dissolve

        # voice "kk131.acc"
        kk "Hahaha~ I miss summer vacation."

        voice "m48.ogg"
        m "Oh shut up. All you do is play games and watch anime."

        # voice "kk132.acc"
        kk "Are you talking about yourself? Ahahaha~"

        voice "m49.ogg"
        m "Whatever."

        scene walk with fade

        "While peacefully chatting ang walking to school, [kk] saw something she doesn't want to see."

        show kurtney talk opened with dissolve

        voice "kk27.ogg"
        kk "Hey, Mark..."

        voice "m50.ogg"
        m "Hmmm?"

        voice "kk28.ogg"
        kk "Look behind our back..."

        voice "m51.ogg"
        m "Back?"

        hide kurtney talk opened

        show stalker neutral with fade

        pause 3.0

        hide stalker neutral with fade

        voice "m52.ogg"
        m "What the hell? Is that the stalker guy from what you've said earlier?"

        show kurtney smile with dissolve

        voice "kk29.ogg"
        kk "Watch your mouth. He might hear you and do something bad."

        voice "m53.ogg"
        m "And now you're concerned for me?"

        voice "m54.ogg"
        m "I should be the one worrying for you."

        show kurtney blush close with dissolve

        voice "kk30.ogg"
        kk "Of course, you're my precious childhood friend."

        voice "m55.ogg"
        m "Hahaha~ whatever. I got this."

        scene walk with fade

        menu:
            "What should I do?"

            "Run straight to the school gate.":
                pause 0.5
                $ subtractPoints()
                "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                voice "m56.ogg"
                m "[kk]..."

                pause 0.5

                python:

                    if persistent.achievementList[7] == False:
                    
                        achievement.grant("Escape Artist")
                        renpy.notify("Achievement Unlocked: Escape Artist")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[7] = True

                show kurtney talk opened with dissolve

                voice "kk31.ogg"
                kk "Yeah?"

                voice "m57.ogg"
                m "Hold my hand."

                show kurtney blush small with dissolve

                voice "kk32.ogg"
                kk "Wha? Are you st-stupid?"

                voice "m58.ogg"
                m "Do it!"

                show kurtney blush close with dissolve

                voice "kk33.ogg"
                kk "O-o-okayyy...."

                scene black with fade

                $ play_sound(running)

                voice "bm29.ogg"
                "With all my might and strength reserved for this day, I grabbed [kk]'s hand and ran like a mad dog."

                voice "bm30.ogg"
                "What a crazy person!"

                scene school gate with fade

                voice "bm31.ogg"
                "Looking at my back, the guy is nowhere to be seen."

                voice "m59.ogg"
                m "Pant pant pant..."

                show kurtney blush close with dissolve

                voice "kk34.ogg"
                kk "Hey tell me what're you trying to do before doing that..."

                voice "kk35.ogg"
                kk "Stupid..."

                voice "m60.ogg"
                m "Hahaha~ I just want to get away though. Why did you suddenly become red?"


                
            "Pick a fight with the stalker.":
                pause 0.5
                $ subtractPoints()
                "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"

                voice "m61.ogg"
                m "Hey, what do you want?"

                show stalker talk with fade

                voice "stalk1.mp3"
                "???" "Hmmm.. Are you her boyfriend?"

                voice "m62.ogg"
                m "No! She's my childhood friend."

                voice "stalk2.mp3"
                "???" "Then take this."

                $ play_sound(punch)

                "BAM!" with vpunch

                $ play_sound(punch)

                "AAHHH!" with hpunch

                $ play_sound(punch)

                "PAAAK!" with vpunch

                voice "m63.ogg"
                m "AAAAAAH!!!"

                scene black with fade
                pause 1.0
                scene walk with fade

                pause 0.5

                python:

                    if persistent.achievementList[8] == False:
                    
                        achievement.grant("Punching Bag")
                        renpy.notify("Achievement Unlocked: Punching Bag")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[8] = True

                show kurtney worry with dissolve

                voice "kk36.ogg"
                kk "Heyyyyyyy..."

                voice "kk37.ogg"
                kk "Wake up Mark..."

                voice "m64.ogg"
                m "What the heck happened?"

                show kurtney happy teeth with dissolve

                voice "kk38.ogg"
                kk "Well, he knocked the soul out of you. Hahaha~"

                voice "m65.ogg"
                m "This is no laughing matter. What happened to him?"

                show kurtney smile with dissolve

                voice "kk39.ogg"
                kk "He ran away when a lot of people were looking at us."

                voice "m67.ogg"
                m "O-ohhh I see... Ughhhh my head hurts."

                

            "Confront the stalker and tell him that you'll report him to the police.":
                    pause 0.5
                    $ hbbpoints += 3
                    $ play_sound(addPoints)
                    "You received {color=#40ff00}3 HBB Points.{/color}"

                    scene walk with fade 

                    voice "m213.ogg"
                    m "Excuse me. Stop whatever you're doing. You're disrupting our lives."

                    show stalker talk with dissolve

                    voice "stalk3.mp3"
                    "???" "Who the hell are you?"

                    voice "stalk4.mp3"
                    "???" "What's your deal, huh?"

                    voice "stalk5.mp3"
                    "???" "Stupid kid standing up to me huh."

                    voice "m69.ogg"
                    m "I am her friend. I will not hesitate to report you to the police this instant!"

                    hide stalker talk
                    show stalker angry 
                    with dissolve

                    voice "stalk6.mp3"
                    "???" "Calm down buddy. No reason to be angry. I'll leave now. Enjoy your day."

                    voice "stalk7.mp3"
                    "???" "I won't forget this! Be careful from now on."

                    hide stalker angry 

                    scene walk 
                    
                    with fade

                    "After a few minutes, the stalker was out of sight."

                    stop music

                    voice "m70.ogg"
                    m "Sighhhh. Hopefully this doesn't happen to you again."

                    show kurtney worry with dissolve

                    $ play_music(evans,fadein=1.5)

                    voice "kk40.ogg"
                    kk "I hope so. You'll be there to protect me right?"

                    voice "m71.ogg"
                    m "Nope. Not me. But the police. Haha~"

                    show kurtney angry talk with dissolve

                    voice "kk41.ogg"
                    kk "Wha?! Stupid."

                    hide kurtney angry talk with dissolve

        
    label kurtneyOfficerScene:
        stop music fadeout 2.0
        scene black with fade

        pause 1.0 

        scene walk with fade

        show police neutral with dissolve 

        $play_music(garden) 

        voice "newOfficer51.mp3"
        "???" "Excuse me!"

        voice "kk42.ogg"
        kk "Ehhh? A police officer?"

        voice "m72.ogg"
        m "Oh great. This makes things easy."

        "The police officer was running towards us with a confused look on his face."

        voice "newOfficer52.mp3"
        o "Excuse me young ones... I just saw what happened earlier. Can you tell me more about the event?"

        voice "m73.ogg"
        m "Uhmmmm my friend here was getting stalked by someone..."

        voice "newOfficer53.mp3" 
        o "A stalker huh?"

        voice "newOfficer54.mp3"
        o "Did you know that stalking is a grave crime? According to the Safe Spaces Act that is."

        voice "m74.ogg"
        m "Yes sir, I've read a bit about that law."

        hide police neutral
        show kurtney talk opened 
        with dissolve

        voice "kk43.ogg"
        kk "Hey Mark. It was that law that you told me earlier right?"

        voice "m75.ogg"
        m "Yeah it is."

        hide kurtney talk opened
        show police neutral
        with dissolve

        voice "newOfficer55.mp3"
        o "Stalking is a serious crime. Do you guys want to learn about the punishment for violating the Safe Spaces Act?"

        $ yuiStoryProgress += 1

        hide police neutral with dissolve

        menu :
            
            o "Do you want to learn more about the punishments of Safe Spaces Act?"

            "Yes, please tell me about the punishments.":
                hide police neutral with dissolve
                pause 0.5
                $ play_sound(addPoints)
                $ hbbpoints += 3
                "You received {color=#40ff00}3 HBB Points.{/color}"
                
                show kurtney happy teeth with dissolve

                python:

                    if persistent.achievementList[9] == False:
                    
                        achievement.grant("Teach Me About Punishments")
                        renpy.notify("Achievement Unlocked: Teach Me About Punishments")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[9] = True

                kk "!!!!"

                voice "kk44.ogg"
                kk "I-I-I want to learn it too..."

                hide kurtney happy teeth
                show police neutral
                with dissolve

                voice "newOfficer12.mp3"
                o "Sure thing. Lemme just take out my handbook."

                pause 2.0

                voice "newOfficer13.mp3"
                o "Uhhh it says here..."

                voice "newOfficer14.mp3"
                o "On Section 12 of the Safe Spaces Act, 
                it states the {color=#30ff45}Specific Acts and Penalties{/color} for Gender-Based Sexual Harassment in Streets and Public Spaces."

                voice "newOfficer15.mp3"
                o "This is quite long so listen carefully okay?"

                with fade

                voice "newOfficer16.mp3"
                o "a) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs;" 
                
                voice "newOfficer17.mp3"
                o"Persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination;" 
                
                voice "newOfficer18.mp3"
                o "The use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs;" 
                
                voice "newOfficer19.mp3"
                o "The persistent telling of sexual jokes, use of sexual names, comments and demands..."

                voice "newOfficer19c.mp3"
                o "...and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety." 

                voice "newOfficer20.mp3"
                o "The penalties will be...!"
                
                voice "newOfficer21.mp3"
                o "{color=#30ff45}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

                voice "newOfficer22.mp3"
                o "{color=#30ff45}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)"

                voice "newOfficer23.mp3"
                o "{color=#30ff45}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)"

                voice "newOfficer24.mp3"
                o "The next on the list!"

                with fade

                voice "newOfficer25.mp3"
                o "b) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening;"
                
                voice "newOfficer26.mp3"
                o "Or intimidating the offended party including flashing of private parts, public masturbation, groping, and similar lewd sexual actions."

                voice "newOfficer27.mp3"
                o "The penalties you will face is...!"
                
                voice "newOfficer28.mp3"
                o "{color=#30ff45}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

                voice "newOfficer29.mp3"
                o "{color=#30ff45}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)"

                voice "newOfficer30.mp3"
                o "{color=#30ff45}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)"

                voice "newOfficer31.mp3"
                o "Moving on!"

                with fade

                voice "newOfficer32.mp3"
                o "c) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person;"

                voice "newOfficer33.mp3"
                o "Or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks..."

                voice "newOfficer33c.mp3"
                o "...or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b)."

                voice "newOfficer34.mp3"
                o "You will face the penalties of...!"

                voice "newOfficer35.mp3"
                o "{color=#30ff45}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP."

                voice "newOfficer36.mp3"
                o "{color=#30ff45}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)"
                
                voice "newOfficer37.mp3"
                o "{color=#30ff45}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)"

                hide police neutral with fade

                m "......"

                voice "m76.ogg"
                m "My head hurts... Ahahaha!"

                show kurtney talk opened with dissolve

                voice "kk45.ogg"
                kk "Wait, that's a really good law, Officer!"
                
                hide kurtney talk closed

            "No, I don't really care.":
                pause 0.5
                $ subtractPoints()
                "Your points have been deducted by 1 HBB Point."
                
        $ renpy.end_replay()
        show screen newNote with fade
        pause 2.0
        stop music
        jump schoolCeremony


label meetWithYui:
    $ persistent.unlockYui = True
    stop music
    pause 1.5
    play sound "audio/music/Transition1.ogg" fadein 1.0
    scene bg train 
    show screen trainTransition 
    with fade
    pause 3.0
    hide screen trainTransition
    $ persistent.unlockTrain = True
    $ persistent.unlockTrain2 = True
    scene train landscape with fade

    python:

        if persistent.achievementList[4] == False:
                
            achievement.grant("Beep Card")
            renpy.notify("Achievement Unlocked: Beep Card")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[4] = True

    pause 2.5

    $play_sound(trainambience,fadein=0.1)
    $ preferences.set_volume("sfx", 0.20)
    pause 5.0

    voice "bm32.ogg"

    $ preferences.set_volume("voice", 0.45)
    "Aaaaaaah~ The landscape is so nice."

    voice "bm33.ogg"
    "I wish every morning was something like this..."

    voice "bm34.ogg"
    "But that's a pointless wish."
    
    scene trainpeople with fade
    pause 2.0
    
    voice "bm35.ogg"
    "Eh, it is surprisingly quiet today..."

    voice "bm36.ogg"
    "Even though its the first day of class?"

    voice "bm37.ogg"
    "Well, I shouldn't be complaining about this."

    stop sound fadeout 5.0
    
    $ play_music(evans,fadein=1.0)

    voice "bm38.ogg"
    "I kinda like this atmosphere."

    voice "bm39.ogg"
    "Hopefully, this day goes successful."

    "...."

    $ play_sound(operator, fadein=3.0,fadeout=0.5)

    scene bg train with fade

    pause 2.0

    "Operator" "Arriving at station. Please check your belongings before getting out. Thank you."

    pause 3.0

    scene yui harassment with fade
    $ preferences.set_volume("sfx", 0.30)
    $ play_sound(people,fadein=3.0,fadeout=1.0)

    "{i}Crowd noises...{/i}"

    "Moving closer towards the exit... I hear some conversation."
    stop sound fadeout 0.5
    $ preferences.set_volume("voice", 0.32)
    voice "man1line1.mp3" 
    "???" "Hey there sexy little miss. Are you free tonight and have a drink." 
    $ preferences.set_volume("voice", 0.28)
    voice "man2line1.mp3"
    "???" "Don't worry, we won't do anything do bad to you hehehe..."
    $ preferences.set_volume("voice", 0.22)
    voice "man3line1.mp3"
    "???" "Do you need money or anything? Just tell us."
    $ preferences.set_volume("voice", 0.45)
    voice "bm40.ogg"
    "I can see three old men sexually harassing a young student girl."

    voice "bm41.ogg"
    "I notice that the girl is trembling and shaking."
    
    voice "yui109.ogg"
    "Girl" "Plea-please l-l-leave me alo-lone..."

    pause 2.0
    with fade
    $ preferences.set_volume("voice", 0.28)
    voice "man1line2.mp3"
    "???" "Hahaha!! She's scared like a child."

    voice "man2line2.mp3"
    "???" "Hey, you're teasing her too much. She might report us."

    voice "man3line2.mp3"
    "???" "Boss, don't worry. She can't even say the sentence straight."

    $ preferences.set_volume("sfx", 0.30)
    pause 1.5
    with fade
    $ timeout = 10
    $ timeout_label = "notSaveYui"
    $ deathFlag = False
    $ metYui = True
    menu trainScene:
        "What should I do?"


        "I'll pick a fight with them." if deathFlag is False:
            pause 0.5

            $ deathFlag = True
            $ preferences.set_volume("voice", 0.50)
            voice "m77.ogg"
            m "Hey you bastards! Stop sexually harrassing that girl."
            $ preferences.set_volume("voice", 0.25)
            voice "man1line3.mp3"
            "???" "Who the hell are you? His boyfriend perhaps?"
            $ preferences.set_volume("voice", 0.29)
            voice "man2line3.mp3"
            "???" "You little punk talking to me like that. I'll crush you."

            voice "man3line3.mp3"
            "???" "Take this you little pesky boy."
            $ preferences.set_volume("sfx", 0.20)
            $ play_sound(punch)

            "BAM!" with vpunch

            $ play_sound(punch)
            with fade
            "AAHHH!" with hpunch

            $ play_sound(punch)
            with fade
            "PAAAK!" with vpunch

            with fade
            $ preferences.set_volume("voice", 0.35)
            voice "m78.ogg"
            m "AAAAAAH!!!"

            pause 1.5

            python:

                if persistent.achievementList[8] == False:
                    
                    achievement.grant("Punching Bag")
                    renpy.notify("Achievement Unlocked: Punching Bag")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    persistent.achievementList[8] = True
                    renpy.pause(1.5)

            jump withOfficer

        "I'll go and inform the train security.":
            "Good choice!"
            
            $ play_sound(addPoints)
            $ hbbpoints += 3
            "You received {color=#40ff00}3 HBB Points.{/color}"
            #hide yui worry closed
            $ preferences.set_volume("voice", 0.40)
            scene bg train morning 
            show police neutral 
            with fade
            voice "m79.ogg"
            m "Officer! Officer!!"

            voice "m80.ogg"
            m "I saw three old men catcalling and sexually harassing a girl student! Please help me."

            $ preferences.set_volume("voice", 0.25)
            voice "newOfficer1.mp3"
            o "I see. Bring me to them."

            label withOfficer:

                hide police neutral with dissolve
                show yui harassment
                with fade

                $ preferences.set_volume("voice", 0.40)
                voice "m81.ogg"
                m "Officer! Here!"
                
                voice "m106.ogg"
                m "These old men are catcalling and making unwanted invitations to this girl."

                show police neutral with dissolve
                $ preferences.set_volume("voice", 0.30)
                voice "newOfficer2.mp3"
                o "HEY YOU BASTARDS!"
                $ preferences.set_volume("voice", 0.23)
                voice "newOfficer3.mp3"
                o "Face the consequences of your crimes!"

                with hpunch

                voice "man1line4.mp3"
                "???" "What the hell. Run guys!!"
                $ preferences.set_volume("voice", 0.20)
                voice "man2line4.mp3"
                "???" "Holy crap don't leave me."
                $ preferences.set_volume("voice", 0.30)
                with vpunch

            #show Yui
            stop music fadeout 0.5
            hide police neutral
            scene bg train morning
            show yui wow 
            with fade
            $ preferences.set_volume("music", 0.15)
            $ play_music(tutorial, fadein=0.5)
            
            voice "yui1.ogg"
            "Girl" "Uwaaaaah! Thank y-y-you sooo much!!"
            $ preferences.set_volume("voice", 0.40)
            voice "m82.ogg"
            m "Ohhh... I didn't really do anything..."

            show yui smile close with dissolve
            voice "yui2.ogg"
            "Girl" "You saved my life...."

            voice "m83.ogg"
            m "Life?"

            show yui smile opened with dissolve
            
            voice "yui3.ogg"
            "Girl" "Uhmm..."
            
            voice "yui4.ogg"
            "Girl" "Can you tell me your name?"

            voice "m84.ogg"
            m "Ohhh. My name is Mark. How about you?"

            show yui blush with dissolve
            voice "yui5.ogg"
            "Girl" "Y-Y-Yu.."

            voice "m85.ogg"
            m "Yu?"

            show yui surprised blush with dissolve

            voice "bm42.ogg"
            "She's gotten a bit red of a sudden..."

            show yui blush closed zorder 3 with dissolve
            voice "yui6.ogg"
            "Girl" "Ple-please call me Yui."

            $_dismiss_pause = False
            show movie intro at offscreenright
            show ypurple zorder 2 at offscreenleft
            with ease

            play sound "audio/fast.wav" volume 0.5

            show movie intro at right
            show ypurple zorder 2 at left
            with ease

            show y name zorder 3 at offscreenleft
            with ease

            play sound "audio/ting.wav"

            show yui yandere mode zorder 3 at right
            show y name zorder 2 at left
            with MoveTransition(0.4)

            voice "m86.ogg"
            m "[y], huh? What a cute name."

            play sound "audio/fast.wav" volume 0.5

            $_dismiss_pause = False
            show movie intro at offscreenleft
            show ypurple zorder 2 at offscreenright
            with ease

            show yui yandere mode at center 
            show y name zorder 2 at offscreenleft
            with MoveTransition(0.2)
            $ renpy.pause(0.3, hard=True)

            show yui surprised blush with dissolve
            voice "yui7.ogg"
            y "EHHH?!! Cute?"

            show yui blush closed with dissolve
            voice "yui8.ogg"
            y "{i}......waaah!{/i}"

            voice "m87.ogg"
            m "Hey, [y]. I saw you earlier that you were shaking and trembling."

            show yui worry with dissolve
            voice "yui9.ogg"
            y "Yeah that was embarassing to see...."

            show yui worry closed with dissolve
            voice "yui10.ogg"
            y "You see, when I was a child... I had a trauma."

            voice "m88.ogg"
            m "A trauma? Can I hear more of this?"
            voice "yui11.ogg"
            y "Uhmmm y-yes..."

            show yui worry opened with dissolve
            voice "yui12.ogg"
            y "When I was in 4th Grade, my boy classmates would make fun of my appearance."

            voice "yui106.ogg"
            y "It made me stop going to school... And I was homeschooled since then."

            # Wrong file. Missing voice
            voice "m215n.ogg"
            m "I can't imagine how you must feel. My heart hurts for you."

            show yui worry closed with dissolve

            voice "m89.ogg"
            m "You know what? I have something interesting to tell you!"

            show yui wow with dissolve

            voice "yui13.ogg"
            y "What is it?"

            voice "m90.ogg"
            m "It's about a law."

            voice "yui14.ogg"
            y "A law? What kind of law?"

            voice "m91.ogg"
            m "It is something related to what you experienced earlier."
            $ timeout = 15
            $ timeout_label = "yuiFirstQuestionTimerOut"
            $ yuiFirstAnswer = True
            hide yui wow with dissolve
            voice "bm43.ogg"
            menu yuiFirstQuestion:
                
                "Aaaaah... What is it again? The law that was approved on 17th of April, 2019?"

                "Re-semiprivate Act No. 11313":
                    
                    voice "m92.ogg"
                    m "Re-semiprivate Act No. 11313"

                    "Wrong answer!"

                    if hbbpoints >= 1:
                        $ subtractPoints()
                        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"

                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

                "Reprivate Act No. 11313":
                    
                    voice "m93.ogg"
                    m "Reprivate Act No. 11313"
                    "Not this... Think again..."
                    if hbbpoints >= 1:
                        $ subtractPoints()
                        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

                "Republic Act No. 11313":
                    
                    voice "m94.ogg"
                    m "Republic Act No. 11313"
                    "Great answer!"

                    if yuiFirstAnswer:

                        $ hbbpoints += 3
                        $ play_sound(addPoints)
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                        
                    jump yuiIntroSecond
                    

                "Rebuild Act No. 11313":
                    
                    voice "m95.ogg"
                    m "Rebuild Act No. 11313"
                    "Not the right answer."
                    if hbbpoints >= 1:
                        $ subtractPoints()
                        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

            #######################################

            label yuiFirstQuestionTimerOut:
                m "Correct Answer: Republic Act No. 11313"

            label yuiIntroSecond:

            voice "m96.ogg"
            m "The law is Republic Act No. 11313."

            show yui wow with dissolve

            voice "yui107.ogg"
            y "What is that law?"

            voice "m97.ogg"
            m "This law is..."
            $ timeout_label = "yuiSecondQuestionTimerOut"
            $ yuiSecondAnswer = True
            hide yui wow with dissolve
            voice "bm44.ogg"
            menu yuiSecondQuestion:
                
                "It is also known as ...."
                
                "Safe Spaces Act":
                    
                    voice "m98.ogg"
                    m "Safe Spaces Act"
                    "Correct!!"

                    if yuiSecondAnswer:

                        $ hbbpoints += 3
                        $ play_sound(addPoints)
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                    jump yuiThirdIntro
                    
                "Safe Pace Act":
                    
                    voice "m99.ogg"
                    m "Safe Pace Act"
                    "Wait this is wrong."
                    $ yuiSecondAnswer = False
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    

                    jump yuiSecondQuestion
                
                "Safe Guardian Act":
                    
                    voice "m100.ogg"
                    m "Safe Guardian Act"
                    "Not the right answer."
                    $ yuiSecondAnswer = False
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    
                    jump yuiSecondQuestion
            
                "Safe Insurrance Act":
                    
                    voice "m101.ogg"
                    m "Safe Insurance Act"
                    "Not the greatest answer."
                    $ yuiSecondAnswer = False
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                         
                    jump yuiSecondQuestion

            label yuiSecondQuestionTimerOut:
                $ subtractPoints()
                "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                
                voice "m98.ogg"
                m "Safe Spaces Act"
            
            label yuiThirdIntro:

                show yui wow with dissolve

                voice "yui15.ogg"
                y "So it is called \"Safe Spaces Act\"?"

                voice "m102.ogg"
                m "Yeah! It's a cool name right?"

                voice "yui16.ogg"
                y "Uhm. But what does it mean?"

                $ yuiThirdAnswer = True
                $ timeout_label = "yuiInfo"

                hide yui wow with dissolve
            voice "bm45.ogg"
            menu yuiThirdQuestion:
                
                "Wait, what does the Safe Spaces Act mean again?"

                "To protect Earth from aliens.":
                    pause 0.5
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    
                    show yui smile close with dissolve

                    voice "yui17.ogg"
                    y "Wait that's really funny~"

                    voice "yui18.ogg"
                    y "Please tell it to me seriously..."
                    
                    voice "m30.ogg"
                    m "Hahaha~ I'm just kidding!"

                    voice "m31.ogg"
                    m "The law was created to..."
                    $ yuiThirdAnswer = False
                    jump yuiThirdQuestion

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
                "To protect men and women from gender-based sexual harassment.":
                    "Nice job! Correct answer."
                    if yuiThirdAnswer:
                        $ play_sound(addPoints)
                        $ hbbpoints += 3
                        "You received {color=#40ff00}3 HBB Points.{/color}"

                        if hbbpoints == 9:
                        
                            python:

                                if persistent.achievementList[6] == False:
                                
                                    achievement.grant("Ace Attorney")
                                    renpy.notify("Achievement Unlocked: Ace Attorney")
                                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                                    persistent.achievementList[6] = True
                        
                    
                    show yui neutral with dissolve
                    label yuiInfo:
                        $ yuiStoryProgress += 1
                        

                        voice "m191.ogg"
                        m "To protect men and women from gender-based sexual harassment."

                        voice "m32.ogg"
                        m "Gender-based streets and public spaces sexual harassment include..."

                        voice "m33.ogg"
                        m "a) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs."

                        voice "m34.ogg"
                        m "b) Persistent uninvited comments or gestures on a person's appearance."

                        voice "m35.ogg"
                        m "c) Relentless requests for personal details."

                        voice "m36.ogg"
                        m "d) Statement of sexual comments and suggestions."

                        voice "m37.ogg"
                        m "e) Public masturbation or flashing of private parts, groping, making offensive body gestures 
                        at someone, and other similar lewd sexual actions."

                        voice "m38.ogg"
                        m "f) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. 
                        This may include cursing, leering and intrusive gazing, and taunting."

                        voice "m39.ogg"
                        m "g) Persistent telling of sexual jokes, use of sexual names."

                        voice "m40.ogg"
                        m "And last but not the least."

                        voice "m41.ogg"
                        m "h) Stalking."

                        show screen newNote with fade
                        pause 1.0

                        show yui wow with dissolve
                        voice "yui19.ogg"
                        y "That was a lot! How'd you memorize it?"

                        voice "m42.ogg"
                        m "Well you know... I wanted to be an attorney. So this much is not that big deal."

                        show yui smile opened with dissolve
                        voice "yui20.ogg"
                        y "You wanted to be an attorney? That sounds really nice~"

                        voice "m103.ogg"
                        m "Thank you ehehe..."

                        jump yuiConflictResolved


                "To protect public and online spaces from danger.":
                    pause 0.5
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    
                    voice "yui21.ogg"
                    y "What danger? Please explain it clearly."

                    voice "m192.ogg"
                    m "Uhhhh.. wait let me remember..."

                    voice "m193.ogg"
                    m "Errr... it is to..."

                    $ yuiThirdAnswer = False

                    jump yuiThirdQuestion

                    

        # voice "bm46.ogg"
        "I'll pretend that I didn't hear the conversation.":
            $ preferences.set_volume("sfx", 0.10)
            pause 0.5
            $ play_sound(subPoints)
            "Your have lost all your points!"
            $ hbbpoints -= hbbpoints
            jump notSaveYui
            

            
    label notSaveYui:
        $ badEndingGame = True
        $ preferences.set_volume("voice", 0.50)
        voice "bm46.ogg"
        "I'll pretend that I didn't hear the conversation."

        voice "bm47.ogg"
        "I should just ignore them..."

        voice "bm48.ogg"
        "I don't wanna get in trouble."

        scene white
        $ timeout_label = None
        menu:
            "You have met a bad ending!"

            "Retry from the start.":
                jump yui_start_case_1

            "Return to Main Menu":
                return

        # IMPLEMENT BAD ENDING!

    
    label yuiConflictResolved:
        hide yui smile opened
        show police neutral with fade       
        
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer4.mp3"
        o "Hey kids. You better get going now. I'll clean this mess up."

        voice "newOfficer5.mp3"
        o "Based on the Implementing Rules and Regulation of Republic Act No. 11313..."

        voice "newOfficer6.mp3"
        o "Those guys broke the law by (1) Catcalling and making unwanted invitations."

        voice "newOfficer7.mp3"
        o "(2) Making statements of sexual comments and suggestions."

        voice "newOfficer8.mp3"
        o "(3) Making advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety." 
        $ preferences.set_volume("voice", 0.25)
        voice "newOfficer9.mp3"
        o "This may include cursing, leering and intrusive gazing, and taunting."
        $ preferences.set_volume("voice", 0.40)
        voice "m104.ogg"
        m "WOW! That's a really great law."
        $ preferences.set_volume("voice", 0.20)
        voice "newOfficer10.mp3"
        o "I know kid."
        $ preferences.set_volume("voice", 0.25)
        voice "newOfficer11.mp3"
        o "Do you want to learn more about the punishments of Safe Spaces Act?"

        $ yuiStoryProgress += 1

        $ timeout = 10
        $ timeout_label = "ignorePunishment"

        hide police neutral with dissolve

    menu punishments:
        
        o "Do you want to learn more about the punishments of Safe Spaces Act?"

        "Yes, please tell me about the punishments.":
            hide police neutral with dissolve
            pause 0.5
            $ hbbpoints += 3
            $ play_sound(addPoints)
            "You received {color=#40ff00}3 HBB Points.{/color}"
            
            show yui smile close with dissolve

            y "!!!!"
            $ preferences.set_volume("voice", 0.40)
            voice "yui22.ogg"
            y "I-I-I want to learn it too..."

            python:

                if persistent.achievementList[9] == False:
                    
                    achievement.grant("Teach Me About Punishments")
                    renpy.notify("Achievement Unlocked: Teach Me About Punishments")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    persistent.achievementList[9] = True

            hide yui smile close
            show police neutral
            with dissolve
            $ preferences.set_volume("voice", 0.25)
            voice "newOfficer12.mp3"
            o "Sure thing. Lemme just take out my handbook."

            pause 1.0

            voice "newOfficer13.mp3"
            o "Uhhh it says here..."

            voice "newOfficer14.mp3"
            o "On Section 12 of the Safe Spaces Act, 
            it states the {color=#30ff45}Specific Acts and Penalties{/color} for Gender-Based Sexual Harassment in Streets and Public Spaces."

            voice "newOfficer15.mp3"
            o "This is quite long so listen carefully okay?"

            with fade

            voice "newOfficer16.mp3"
            o "a) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs;" 
            
            voice "newOfficer17.mp3"
            o"Persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination;" 
            
            voice "newOfficer18.mp3"
            o "The use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs;" 
            
            voice "newOfficer19.mp3"
            o "The persistent telling of sexual jokes, use of sexual names, comments and demands..." 

            voice "newOfficer19c.mp3"

            o "...and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety."

            voice "newOfficer20.mp3"
            o "The penalties will be...!"
            
            voice "newOfficer21.mp3"
            o "{color=#30ff45}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            voice "newOfficer22.mp3"
            o "{color=#30ff45}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)"

            voice "newOfficer23.mp3"
            o "{color=#30ff45}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)"

            voice "newOfficer24.mp3"
            o "The next on the list!"

            with fade

            voice "newOfficer25.mp3"
            o "b) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening;"
            
            voice "newOfficer26.mp3"
            o "Or intimidating the offended party including flashing of private parts, public masturbation, groping, and similar lewd sexual actions."

            voice "newOfficer27.mp3"
            o "The penalties you will face is...!"
             
            voice "newOfficer28.mp3"
            o "{color=#30ff45}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            voice "newOfficer29.mp3"
            o "{color=#30ff45}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)"

            voice "newOfficer30.mp3"
            o "{color=#30ff45}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)"

            voice "newOfficer31.mp3"
            o "Moving on!"

            with fade

            voice "newOfficer32.mp3"
            o "c) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person;"

            voice "newOfficer33.mp3"
            o "Or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks..."

            voice "newOfficer33c.mp3"
            o "...or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b)."

            voice "newOfficer34.mp3"
            o "You will face the penalties of...!"

            voice "newOfficer35.mp3"
            o "{color=#30ff45}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP."

            voice "newOfficer36.mp3"
            o "{color=#30ff45}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)"
            
            voice "newOfficer37.mp3"
            o "{color=#30ff45}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)"

            hide police neutral with fade

            m "......"

            voice "m194.ogg"
            m "My head hurts... Ahahaha!"

            show yui wow with dissolve

            voice "yui23.ogg"
            y "Wait, that's a really good law, Officer!"

            scene bg train morning with fade

            jump trainEndScene
            

        "No, I don't really care.":
            jump ignorePunishment
    
    label ignorePunishment:

        voice "m105.ogg"
        m "No, I don't really care."

        show police neutral with dissolve

        voice "newOfficer38.mp3"
        o "Ohhhh that's a shame."
        $ subtractPoints()
        $ hbbpoints -= 3
        "Your {color=#30ff45}HBB Points{/color} have been deducted by 3!"
        
    
    label trainEndScene:


        show screen newNote 
        pause 2.0

        show police neutral

        voice "newOfficer39.mp3"
        o "Now go on your way. I'll take care of them. In jail of course."
        $ preferences.set_volume("voice", 0.40)
        voice "m195.ogg"
        m "Sir, can I ask for your name?"
        $ preferences.set_volume("voice", 0.25)
        voice "newOfficer40.mp3"
        o "Oh it's Greg. Find me whenever you are troubled."
        $ preferences.set_volume("voice", 0.40)
        voice "m196.ogg"
        m "Thank you very much sir!"

        hide police neutral with fade

        show yui worry opened with dissolve

        voice "yui3.ogg"
        y "Uhmmm..."

        voice "yui24.ogg"
        y "See you Mark! Thank you again..."

        voice "m197.ogg"
        m "Bye Yui. No worries. I just can't stand it when I see someone getting harassed."

        show yui blush with dissolve
        voice "yui25.ogg"
        y "Uhhhm.. I hope I..." 
        voice "yui26.ogg"
        y "I can see you aga--"

        scene black with fade

        $ play_sound(trainpass,fadein=3.0,fadeout=2.0)

        pause 5.0

        #Train sound

        scene bg train morning with fade
        "{i}A train passed by.{/i}"

        voice "m198.ogg"
        m "What?"

        show yui surprised blush with dissolve
        voice "yui27.ogg"
        y "No, you heard nothing!!! Goodbye!"

        scene black with fade

        stop music fadeout 1.0

        $ renpy.end_replay()

        jump schoolCeremony

label schoolCeremony:

    scene aerial 
    show screen schoolTransition
    with fade
    play sound "audio/music/Piano2.ogg"

    pause 5.0
    hide screen schoolTransition
    with fade

    $ play_music(quirky,fadein=0.2)
    voice "bm49.ogg"
    "Borneul Highschool. A prestigious school where only the best can enter."

    scene school building with fade

    voice "bm50.ogg"
    "I'm so lucky to be here."

    "...."

    scene audi1 with fade

    pause 1.0 
    $ preferences.set_volume("sfx", 0.20)
    $ play_sound(speaker,fadein=0.5,fadeout=0.5)

    "President" "To all the newcomer students, I welcome you!"

    "President" "I hope that you can achieve your dreams in this school."

    scene audi2 with dissolve

    "President" "To all those that are nearing graduation, I hope you achieved what you wanted here."

    scene audi3 with dissolve
    $ preferences.set_volume("sfx", 0.28)
    $ play_sound(clap,fadein=2.0)

    "President" "That is all for my speech. Thank you!"

    "{i}Students clapping{/i}"

    show kurtney happy teeth with dissolve
    

    if metYui is True:
        $ preferences.set_volume("sfx", 0.40)
        voice "kk46.ogg"
        kk "Dude! I hope we are classmates in this new school year."

        voice "m108.ogg"
        m "Oh please no."

        show kurtney angry talk with dissolve

        voice "kk47.ogg"
        kk "Why? I'm fun to hang out with right?"

        voice "m214.ogg"
        m "Yeah yeah whatever you say."

        $_dismiss_pause = False
        show movie intro at offscreenleft
        show ymagenta zorder 2 at offscreenright
        with ease
        
        play sound "audio/fast.wav" volume 0.5

        show movie intro at left
        show ymagenta zorder 2 at right
        with ease

        show k name zorder 3 at offscreenright
        with ease

        play sound "audio/ting.wav"

        show kurtney happy teeth zorder 3 at left
        show k name zorder 3 at left
        with MoveTransition(0.4)

        voice "bm51.ogg"
        "This is [kk]. My weird childhood friend."

        voice "bm52.ogg"
        "We have been friends since elementary school. She is a little boyish and sometimes annoying."

        voice "bm53.ogg"
        "But I don't hate it at all."

        play sound "audio/fast.wav" volume 0.5

        $_dismiss_pause = False
        show movie intro at offscreenright
        show ymagenta zorder 2 at offscreenleft  
        with ease
        
        show kurtney smile zorder 3 at center
        show k name zorder 2 at offscreenright
        with MoveTransition(0.2)
        $ renpy.pause(0.3, hard=True)

        show kurtney happy teeth with dissolve
        $ preferences.set_volume("voice", 0.60)
        voice "kk11.ogg"
        kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"
        $ preferences.set_volume("voice", 0.40)
        voice "m215.ogg"
        m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

        show kurtney smile with dissolve
        $ preferences.set_volume("voice", 0.60)
        voice "kk12.ogg"
        kk "You poor little thing. Don't worry, I'll always be here for you so you don't look like a loser."

        voice "m216n.ogg"
        m "Well, don't even talk like you have one."

        show kurtney happy teeth with dissolve

        voice "kk13.ogg"
        kk "Hahaha~ Don't worry about me. I'm more worried about your future."

        voice "m217n.ogg"
        m "I'm not a child for you to worry about."
        $ preferences.set_volume("voice", 0.40)
        voice "kk14.ogg"
        kk "Haha!!"

    else:
        
        voice "kk46.ogg"
        kk "Dude! I hope we are classmates in this new school year."

        voice "m108.ogg"
        m "Oh please no."

        show kurtney angry talk

        voice "kk47.ogg"
        kk "Why? I'm fun to hang out with right?"

        voice "m214.ogg"
        m "Yeah yeah whatever you say."


    
    $ renpy.end_replay()
    jump afterCeremony

label afterCeremony:

    scene audi4 

    show kurtney smile
    with fade
    $ preferences.set_volume("voice", 0.60)
    voice "kk48.ogg"
    kk "Lemme check the school bulletin to know our section."
    $ preferences.set_volume("voice", 0.50)
    voice "m109.ogg"
    m "Sure dude. Gonna go to the bathroom first."

    voice "kk49.ogg"
    kk "Meet me near the school bulletin okay?"
    
    voice "m110.ogg"
    m "Yeah just go."

    scene football with fade
    $ preferences.set_volume("music", 0.15)
    voice "bm54.ogg"
    "A new school year..."

    voice "bm55.ogg"
    "I hope it is fun..."

    scene pools with fade

    voice "bm56.ogg"
    "Last year, I was a loner in my class."

    voice "bm57.ogg"
    "But thankfully, I have [kk]. She's a really good childhood friend."

    
    $ preferences.set_volume("sfx", 0.30)
    #Flag to check if USER accepts lunch invite
    $ lunchWithYui = True
    stop music fadeout 2.0
    pause 1.0
    scene hallway 
    show screen lostTransition
    play sound "audio/music/Transition2.ogg"
    with fade
    pause 3.0
    hide screen lostTransition
    $ persistent.unlockHallway = True
    $ preferences.set_volume("music", 0.12)
    $ play_music(meeting,fadein=0.5)
    $ preferences.set_volume("voice", 0.45)
    if metYui is True:

        "???" "Hey..."

        "???" "M-M-Mark!"

        show yui blush closed with dissolve

        voice "m111.ogg"
        m "Ehhhhh!!!?"

        voice "m112.ogg"
        m "Yui?! You go to my school?"

        show yui blush with dissolve
        voice "yui28.ogg"
        y "Y-Yeah! Did you not no-notice my uniform?"

        voice "m113.ogg"
        m "I did not notice it at all. Oh my!"

        voice "m199.ogg"
        m "So you are a First Year student."

        voice "m114.ogg"
        m "Why didn't you tell me?"

        voice "m115.ogg"
        m "No.. sorry. It's my fault."

        show yui smile close with dissolve
        voice "yui29.ogg"
        y "No... it's fine! I forgot to tell you we go to the same school."

        show yui worry opened with dissolve
        voice "yui30.ogg"
        y "Uhm... M-M-Mark?"

        voice "m116.ogg"
        m "Yeah?"
        voice "yui31.ogg"
        y "Can you help me get to my classroom?"

        voice "m117.ogg"
        m "Are you perhaps lost?"

        show yui smile close with dissolve
        voice "yui32.ogg"
        y "Yeah... this school is really big."

        voice "m118.ogg"
        m "No wonder. It's just like me when I was a First Year student."

        voice "m119.ogg"
        m "You are currently in the Second Year's building."

        scene hallway with fade



        # This choice will determine who will eat lunch with MC
        $ timeout_label = "leaveYui"
        menu findRoomWithYui:
    
            "Go and find the classroom with Yui.":

                scene school building with fade
                voice "m200.ogg"
                m "Haaa.."

                show yui blush closed with dissolve
                voice "yui33.ogg"
                y "Waaaah.. I'm so sweaty."

                voice "m120.ogg"
                m "Yeah it's kinda far from our building. Hahaha~"

                voice "m121.ogg"
                m "Just go inside there. All First Year classes are in this building."

                show yui blush with dissolve

                "{i}8:50 AM...{/i}"

                voice "m122.ogg"
                m "The first bell is gonna ring now."

                voice "m123.ogg"
                m "I'm going back now [y]!"

                voice "m124.ogg"
                m "Have fun in there!"

                show yui blush closed with dissolve
                voice "yui34.ogg"
                y "W-w-waaaait Mark!"
                voice "yui3.ogg"
                y "Uhm...."

                show yui blush with dissolve
                voice "yui35.ogg"
                y "If it's fine with you.."
                voice "yui36.ogg"
                y "Can I treat you later in lunch? As a thanks for helping me..."

                $ timeout_label = "notLunch"

                menu:
                    "Ehhhh? I've never been invited by a girl to lunch. What should I do?"

                    "Sure I'll go eat with you.":
                        $ persistent.unlockCafeteria = True
                        
                        voice "m125.ogg"
                        m "Sure I'll go eat with you."

                        show yui wow with dissolve
                        voice "yui37.ogg"
                        y "For real? Waaaah!"

                        show yui smile close with dissolve

                        python:

                            if persistent.achievementList[13] == False:
                                    
                                achievement.grant("Lunch Date")
                                renpy.notify("Achievement Unlocked: Lunch Date")
                                renpy.play("audio/sfx/achievement.ogg",channel="sound")
                                persistent.achievementList[13] = True

                        voice "m126.ogg"
                        m "Wait why are you so happy?"

                        voice "m127.ogg"
                        m "Ready your money though. I'm a big eater."

                        voice "yui38.ogg"
                        y "Ehehe.. sure! You can choose whatever you want."

                        $ play_sound(bell) 

                        "{i}♫ Kin kon kan kon ♫{/i}"

                        show yui worry with dissolve

                        pause 2.0

                        voice "m128.ogg"
                        m "Oh crap that's the bell!"

                        voice "m129.ogg"
                        m "I'll be going now [y]!"

                        show yui smile opened with dissolve
                        voice "yui39.ogg"
                        y "See you later.... M-Mark."

                        jump lunch

                    "Sorry, maybe next time?":

                        label notLunch:
                            
                            voice "m130.ogg"
                            m "Sorry, maybe in another day."

                            show yui worry with dissolve
                            voice "yui40.ogg"
                            y "Oh.... that's... a shame."

                            show yui worry closed with dissolve
                            voice "yui41.ogg"
                            y "I... I see..."

                            show yui smile close with dissolve
                            voice "yui42.ogg"
                            y "See you..."

                            scene school building with fade

                            "She left running while her hands is in her eyes."

                            "...."

                            jump lunch

            "Go to [kk] in the school bulletin and leave Yui":

                label leaveYui:
                    $ lunchWithYui = False
                    
                    voice "m131.ogg"
                    m "I'm sorry [y]. I can't help you. I have somewhere to go with my friend."

                    show yui worry with dissolve
                    voice "yui43.ogg"
                    y "Ah.... Is that so?"

                    show yui worry closed with dissolve
                    voice "yui44.ogg"
                    y "That's a real shame."

                    show yui smile close with dissolve
                    voice "yui45.ogg"
                    y "I'll be going now Mark."

                    scene hallway with fade

                    "She left running with a troubled expression on her face."

                    "...."

                    jump lunch
    else:

        voice "yui3.ogg"
        "???" "Uhmmm..."
        
        voice "yui108.ogg"
        "???" "Excu-cuse m-m-me....!"

        "Looking at my back, there is someone pull my sleeves..."

        show yui smile close with fade

        voice "m201.ogg"
        m "Uhhhh.. Hello?"

        voice "m202.ogg"
        m "You are?"
        voice "yui31.ogg"
        "Girl" "Can you help me get to my classroom?"

        voice "m117.ogg"
        m "Are you perhaps lost?"

        show yui worry opened with dissolve
        voice "yui32.ogg"
        "Girl" "Yeah... this school is really big."

        voice "m203.ogg"
        m "No wonder. It's just like me when I was a First Year student. Haha~"

        voice "m216.ogg"
        m "You are currently in the Second Year's building."

        show yui neutral with dissolve
        voice "yui3.ogg"
        "Girl" "Uhmm..."
        voice "yui4.ogg"
        "Girl" "Can you tell me your name?"

        voice "m204.ogg"
        m "Ohhh. My name is Mark. How about you?"

        show yui blush with dissolve
        voice "yui5.ogg"
        "Girl" "Y-Y-Yu.."

        voice "m205.ogg"
        m "Yu?"

        show yui surprised blush with dissolve

        "She's gotten a bit red of a sudden..."

        show yui blush closed with dissolve
        voice "yui6.ogg"
        "Girl" "Ple-please call me Yui."

        voice "m206.ogg"
        m "[y], huh? What a cute name."

        show yui surprised blush with dissolve
        voice "yui7.ogg"
        y "EHHH?!! Cute?"

        show yui blush closed with dissolve
        voice "yui8.ogg"
        y "{i}......waaah!{/i}"

        # ADD MORE

        scene hallway with dissolve

        jump findRoomWithYui

label lunch:

    stop music fadeout 1.0

    pause 1.0
    $ preferences.set_volume("music", 0.15)
    $ play_music(relax, fadein=2.0)

    if lunchWithYui is True:

        scene black with fade

        pause 2.0

        scene class1 with fade

        voice "t1.ogg"
        t "To get the answer of this equation..."

        voice "t2.ogg"
        t "You must first..."

        $ play_sound(bell) 

        "{i}♫ Kin kon kan kon ♫{/i}"

        show clarrise talk with dissolve
        voice "t3.ogg"
        t "Okay Class! You may now take your lunch."
        voice "t4.ogg"
        t "We will have a quiz after your lunch."

        with vpunch

        "Everyone" "WHAT?!!"

        pause 1.0

        scene class1
        show kurtney talk opened 
        with fade
        $ preferences.set_volume("voice", 0.50)
        voice "kk50.ogg"
        kk "Hey dude wanna go to cafeteria?"

        voice "m132.ogg"
        m "Sorry dude. I'm meeting someone today."

        show kurtney happy teeth with dissolve
        $ preferences.set_volume("voice", 0.40)
        voice "kk51.ogg"
        kk "Meeting someone? Hey hey hey what's happening to Mr. Mark, huh?"

        voice "m133.ogg"
        m "I'm going ahead. Eat with yourself."

        show kurtney angry talk with dissolve

        voice "kk52.ogg"
        kk "Wah! This little punk."
        stop music fadeout 0.5
        scene black with fade
        
        pause 1.0

        scene bg cafeteria with fade

        show yui smile close with dissolve

        pause 2.0
        $ preferences.set_volume("sfx", 0.20)
        $ play_sound(people,fadein=2.0,fadeout=0.5)
        $ preferences.set_volume("voice", 0.50)
        voice "yui110.ogg"
        y "Hey Mark! Here!"

        

        voice "m134.ogg"
        m "Sorry [y]. Did you wait?"

        show yui neutral with dissolve
        voice "yui46.ogg"
        y "No... I just got here..."

        voice "m135.ogg"
        m "Is that so? Then it's fine."

        show yui smile opened with dissolve
        voice "yui47.ogg"
        y "So what do you want to eat?"

        voice "yui48.ogg"
        y "Just tell me. I got everything covered."
        $ persistent.unlockCafeteria = True
        $ play_music(morning, fadein=0.5)
        $ preferences.set_volume("music", 0.12)
        scene bg cafeteria with fade

        $ timeout_label = None
        menu:
            "What should I eat?"

            "Chicken Curry {image=curry.png}":
                voice "m000.mp3"
                m "I want the Chicken Curry hehehe."

                show yui wow with dissolve
                voice "yui111.ogg"
                y "Eh, you like Indian dishes?"

                voice "m136.ogg"
                m "Yeah they taste good."

                y "I... I see."

            "Tonkotsu(Pork) Ramen. {image=ramen.png}":
                
                voice "m208.ogg"
                m "I want the Tonkotsu Ramen."

                show yui wow with dissolve

                y "Eh, you like Japanese dishes?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "yui41.ogg"
                y "I... I see."

            "Quarter Pound Burger with Large Fries. {image=burger.jpg}":
                
                voice "m209.ogg"
                m "I want the Quarter Pounder Burger."

                show yui wow with dissolve
                voice "yui50.ogg"
                y "Eh, you like American fast-food?"

                
                voice "m136.ogg"
                m "Yeah they taste good."

                voice "yui41.ogg"
                y "I... I see."

            "12\" All Meat Pizza with Thin Crust. {image=pizza.jpg}":
                
                voice "m137.ogg"
                m "I want the All Meat Pizza."

                show yui wow with dissolve
                voice "yui51.ogg"
                y "Eh, you like pizza huh?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "yui41.ogg"
                y "I... I see."

            "Apple Risotto. {image=risotto.jpg}":
                
                voice "m138.ogg"
                m "I want the Risotto."

                show yui wow with dissolve
                voice "yui52.ogg"
                y "Eh, you like Italian food huh?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "yui41.ogg"
                y "I... I see." 

            "All of it. All in. Just do it.":
                
                voice "m139.ogg"
                m "I want everything in today's menu."

                show yui wow with dissolve
                voice "yui53.ogg"
                y "Ehhh? There's no way you can finish all of it."

                
                voice "m140.ogg"
                m "I've done it once. With my friend of course."

                
                voice "m141.ogg"
                m "The moment you said \"I've got everything covered\", I already knew what to do."

                show yui smile close with dissolve
                voice "yui54.ogg"
                y "Hahaha~ Okay I get it!"

                python:

                    if persistent.achievementList[14] == False:
                            
                        achievement.grant("Big Eater")
                        renpy.notify("Achievement Unlocked: Big Eater")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[14] = True
                pause 2.0
    
    else:
        scene black with fade

        pause 2.0

        scene class1 with fade

        voice "t1.ogg"
        t "To get the answer of this equation..."

        voice "t2.ogg"
        t "You must first..."

        $ play_sound(bell) 

        "{i}♫ Kin kon kan kon ♫{/i}"

        show clarrise talk with dissolve

        voice "t3.ogg"
        t "Okay Class! You may now take your lunch."

        voice "t4.ogg"
        t "We will have a quiz after your lunch."

        with hpunch

        "Everyone" "WHAT?!!"

        pause 1.0

        scene class1
        show kurtney talk opened 
        with fade

        voice "kk50.ogg"
        kk "Hey dude wanna go to cafeteria?"

        voice "m142.ogg"
        m "Yeah sure. Are you going to treat me?"

        show kurtney happy teeth with dissolve

        voice "kk53.ogg"
        kk "Keep on dreaming. Maybe I'll treat you when you get a girlfriend~"

        scene bg cafeteria with fade
        
        voice "m207.ogg"
        m "Dude this sucks."

        show kurtney talk opened with dissolve

        voice "kk54.ogg"
        kk "What?"

        voice "m144.ogg"
        m "Nothing."

        show kurtney happy teeth with dissolve

        voice "kk55.ogg"
        kk "Okay I'll treat to something just for today!"

        voice "kk56.ogg"
        kk "And while you still don't have a girlfriend, I'll eat with you so don't look like a loser!"

        voice "m145.ogg"
        m "Whatever!!! Arghhhh..."

        $ timeout_label = None

        menu:
            "What should I eat?"

            "Tonkotsu(Pork) Ramen. {image=ramen.png}":
                
                voice "m208.ogg"
                m "I want the Tonkotsu Ramen."

                show kurtney talk opened with dissolve

                voice "kk57.ogg"
                kk "Eh, you like Japanese dishes?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "kk58.ogg"
                kk "I... I see."

            "Quarter Pound Burger with Large Fries. {image=burger.jpg}":
                
                voice "m209.ogg"
                m "I want the Quarter Pounder Burger."

                show kurtney talk opened with dissolve

                voice "kk59.ogg"
                kk "Eh, you like American fast-food?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "kk58.ogg"
                kk "I... I see."

            "12\" All Meat Pizza with Thin Crust. {image=pizza.jpg}":
                
                voice "m209.ogg"
                m "I want the All Meat Pizza."

                show kurtney talk opened with dissolve

                voice "kk60.ogg"
                kk "Eh, you like pizza huh?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "kk58.ogg"
                kk "I... I see."

            "Apple Risotto. {image=risotto.jpg}":
                
                voice "m138.ogg"
                m "I want the Risotto."

                show kurtney talk opened with dissolve

                voice "kk61.ogg"
                kk "Eh, you like Italian food huh?"

                voice "m136.ogg"
                m "Yeah they taste good."

                voice "kk58.ogg"
                kk "I... I see." 

            "All of it. All in. Just do it.":
                
                voice "m139.ogg"
                m "I want everything in today's menu."

                show kurtney talk opened with dissolve
                voice "kk62.ogg"
                kk "Ehhh? There's no way you can finish all of it."

                voice "m210.ogg"
                m "Of course you'll help me. HAHAHA~"

                voice "m141.ogg"
                m "The moment you said \"I've got everything covered\", I already knew what to do."

                show kurtney talk opened with dissolve

                voice "kk63.ogg"
                kk "Hahaha~ Okay I get it!"

                python:

                    if persistent.achievementList[14] == False:
                            
                        achievement.grant("Big Eater")
                        renpy.notify("Achievement Unlocked: Big Eater")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[14] = True

        "...."
        scene black with fade
        pause 2.0
    $ renpy.end_replay()
    jump socialStudiesQuiz

label socialStudiesQuiz:
    stop music fadeout 1.0
    $ play_music(everyone,fadein=3.0)
    scene class1
    show screen quizTransition
    pause 3.0
    hide screen quizTransition
    show clarrise talk 
    with fade
    $ preferences.set_volume("voice", 0.40)
    

    
    voice "t5.ogg"
    t "Okay Class! Listen up!"

    
    voice "t19.ogg"
    t "There will be a surprise quiz today."
    

    show clarrise talk close with dissolve
    voice "t6.ogg"
    t "It is a 10 item quiz. Make sure to review your notes."

    voice "t7.ogg"
    t "The topic is about the Republic Act No. 11313 also known as \"Safe Spaces Act.\""

    scene class1 with fade

    # Implement notes

    if metYui is True:
        "No way!!! I know this law. I could ace this test."

        show kurtney talk opened with dissolve
        $ preferences.set_volume("voice", 0.60)
        voice "kk64.ogg"
        kk "Hey future Attorney Mark. Do you know this law?"
        $ preferences.set_volume("voice", 0.40)
        voice "m146.ogg"
        m "Of course. Leave it to me."
    else:
        "No way!!! I know this law. I could ace this test."

        show kurtney talk opened with dissolve

        voice "kk65.ogg"
        kk "Hey dude. Isn't this what you've just told me earlier in the jeep?"

        voice "m147.ogg"
        m "Yeah dude. Did you remember what I said?"

        show kurtney happy teeth with dissolve

        voice "kk66.ogg"
        kk "I'll try to remember it haha~"

    jump quiz

label quiz:
    $ quizPoints = 0
    $ quizNum = []
    scene class1
    

    "Your goal in this quiz to score high points! At the end of the quiz, your correct points will be added to HBB Points!"

    "Don't worry! Getting wrong answers will not reduce your points!"

    "Goodluck!"

    pause 2.0

    show clarrise talk
    with fade
    hide screen showNotesButton
    show screen displayScore
    $ preferences.set_volume("voice", 0.45)
    voice "t8.ogg"
    t "Okay Class! Ready or not, here I go!"
    show clarrise talk close with dissolve
    voice "t9.ogg"
    t "First Question!"
    hide clarrise talk close with dissolve
    $ timeout = 20
    $ timeout_label = "one"
    menu:
        
        "This law recognizes that both men and women must have equality, security, and safety not only 
        in private but also on the streets, public spaces, online, workplaces and educational and training institutions."

        "Republic Act No. 11616":
            ""
        "Republic Act No. 11313":
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
            voice "m148.ogg"
            m "Alright! That was an easy one."
        "Republic Act No. 11717":
            ""
        "Republic Act No. 11919":
            ""
    label one:
    $ timeout_label = "two"
    show clarrise talk with dissolve
    voice "t10.ogg"
    t "Second Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    menu:
        
        "Republic Act No. 11313 is commonly known as \"S____ S______ A__\""

        "Save Spaceship Act":
            ""
        "Safe Spaces Act":
            voice "m149.ogg"
            m "Okay got that one in the bag!"
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "Sale Summer Act":
            ""
        "Super Smash Act":
            ""
    label two:
    $ timeout = 10
    show clarrise talk with dissolve
    voice "t11.ogg"
    t "Third Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "three"
    menu:
        
        "Catcalling is a gender-based sexual harassment covered in Safe Spaces Act."
        "True":
            voice "m211.ogg"
            m "That is a freebie."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label three:
    show clarrise talk with dissolve
    voice "t12.ogg"
    t "Fourth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "four"
    menu:
        
        "Making unwanted invitations is a gender-based sexual harassment covered in Safe Spaces Act."
        "True":
            voice "m150.ogg"
            m "Easy."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label four:
    show clarrise talk with dissolve
    voice "t13.ogg"
    t "Fifth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "five"
    menu:
        
        "Stalking is included as a gender-based sexual harassment in Safe Spaces Act."
        "True":
            voice "m151.ogg"
            m "Okay doing good!"
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label five:
    show clarrise talk with dissolve
    voice "t14.ogg"
    t "Sixth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "six"
    menu:
        
        "Situation: You see your classmate in the classroom getting sexually harassed by a teacher. What do you do?"
        "Do nothing.":
            ""
        "Join in the act.":
            ""
        "Confront the teacher.":
            ""
        "Record the evidence and report to the faculty/police.":
            voice "m152.ogg"
            m "Nice going!"
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
    label six:
    show clarrise talk with dissolve
    voice "t15.ogg"
    t "Seventh Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "seven"
    menu:
        
        "Gender-based sexual harassment can also be commited in Public Utility Vehicles(PUV)."
        "True":
            voice "m153.ogg"
            m "That wasn't hard."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label seven:    
    show clarrise talk with dissolve
    voice "t16.ogg"
    t "Eight Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "eight"
    menu:
        
        "Gender-based sexual harassment can also be commited in Streets and Public Spaces."
        "True":
            voice "m154.ogg"
            m "The easiest."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label eight:
    show clarrise talk with dissolve
    voice "t17.ogg"
    t "Ninth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "nine"
    menu:
        
        "The cyberspace is also covered in Safe Spaces Act."
        "True":
            voice "m155.ogg"
            m "Got it in the bag."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label nine:
    show clarrise talk with dissolve
    voice "t18.ogg"
    t "Last Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "ten"
    menu:
        
        "Public masturbation or flashing of private parts, groping, making offensive body gestures at someone, 
        and other similar lewd sexual actions is a gender-based sexual harassment in Safe Spaces Act."
        "True":
            voice "m156.ogg"
            m "Easy money."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label ten:
    
    # Check quiz score
        

    scene class1 with fade

    "Class" "WAAAAAAA!"

    "Everyone is turning their heads. Asking if they did well."

    show kurtney talk opened with dissolve
    $ preferences.set_volume("voice", 0.60)
    voice "kk67.ogg"
    kk "What the hell. That was hard."

    hide kurtney talk opened
    $ preferences.set_volume("voice", 0.40)
    voice "m157.ogg"
    m "Was it? I don't think so. Haha~"

    python:
        for i in quizNum: 
            if quizNum[i] == 1:
                hbbpoints += 1
    $ preferences.set_volume("voice", 0.50)
    voice "m158.ogg"
    m "I got [quizPoints] points baby."

    python:
        if quizPoints == 10:

            if persistent.achievementList[15] == False:
                            
                achievement.grant("Galaxy Brain")
                renpy.notify("Achievement Unlocked: Galaxy Brain")
                renpy.play("audio/sfx/achievement.ogg",channel="sound")
                persistent.achievementList[15] = True

    pause 2.5

    $ play_sound(addPoints)

    "[quizPoints] points have been added to your HBB Points!"



    "Mark, with a smile on his face, knew he did well."

    hide screen displayScore

    $ renpy.end_replay()

    show screen showNotesButton

    stop music fadeout 2.0
    pause 2.0

    

    # Show achievement if perfect
    # Show test result



label pervTeacher:
    
    scene class2
    show screen pervTransition
    play sound "audio/music/Piano5.ogg"
    $ persistent.unlockClass = True
    pause 3.0

    hide screen pervTransition

    scene black with fade

    centered "1 Week Later..."
    
    scene class2 with fade
    $ preferences.set_volume("sfx", 0.21)
    $ play_sound(people,fadein=0.2,fadeout=3.0)
    $ preferences.set_volume("music", 0.15)
    "Classroom noises...."
    pause 2.0

    show kurtney talk opened with dissolve

    $ play_music(doll,fadein=3.0)
    $ preferences.set_volume("voice", 0.60)
    voice "kk68.ogg"
    kk "Hey Mark, did you hear the news?"

    voice "m212.ogg"
    m "What news?"
    
    voice "kk69.ogg"
    kk "It's about [t]."

    voice "m159.ogg"
    m "What happened to [t]."

    voice "kk70.ogg"
    kk "Based on what I heard, she got sick and is in the hospital."
    $ preferences.set_volume("music", 0.27)
    $ preferences.set_volume("voice", 0.45)
    voice "kk71.ogg"
    kk "The school faculty doesn't know when she's going back."

    voice "m160.ogg"
    m "She's in critical condition?"

    voice "kk72.ogg"
    kk "I don't know dude. That's all I know."

    voice "kk73.ogg"
    kk "Ohh! I almost forgot."

    voice "kk74.ogg"
    kk "There will be someone substituting [t]."

    voice "m160n.ogg"
    m "Who?"
    $ preferences.set_volume("sfx", 0.40)
    $ play_sound(walking,fadein=0.5,fadeout=3.0)

    show kurtney angry talk with dissolve

    voice "kk75.ogg"
    kk "They say he's a nasty person."

    voice "m161.ogg"
    m "O-ohh..."

    hide kurtney angry talk with dissolve

    "Noise of footsteps towards the door."
    $ preferences.set_volume("sfx", 0.25)
    $ play_sound(doorcreak)

    pause 2.0
    $ preferences.set_volume("sfx", 0.20)
    $ play_sound(pervlaugh,fadein=1.0)

    pause 1.0

    "???" "Hwehehehe..."

    stop sound fadeout 0.5

    with hpunch

    "Everyone in the classroom gasped."

    show butch creepy smile at right with dissolve
    $ preferences.set_volume("voice", 0.28)
    voice "newButch1.mp3"
    "???" "I hope we all get along, everyone hehehe~"

    voice "newButch2.mp3"
    "???" "I will be your substitute teacher for this class."

    voice "newButch3.mp3"
    "???" "Call me Professor Butch."
    
    voice "newButch4.mp3"
    b "These are some nice looking girls, huh?"

    voice "newButch5.mp3"
    b "Hehehehe... perfect for my taste."
    $ preferences.set_volume("voice", 0.40)
    voice "bm58.ogg"
    "What the hell did he just say?"

    voice "bm59.ogg"
    "Looking at [kk], she is about to stand up."

    show kurtney talk angry at left with dissolve
    $ preferences.set_volume("voice", 0.50)
    voice "kk76.ogg"
    kk "What did you say?!"

    voice "m162.ogg"
    m "You idiot..."

    show butch creepy laugh with dissolve
    $ preferences.set_volume("voice", 0.28)
    voice "newButch6.mp3"
    b "Oh did I ask you to talk? You'll be receiving a failing grade."

    $ play_sound(pervlaugh,fadein=1.0)
    b "Hehehe~"

    hide butch creepy laugh with dissolve

    show kurtney talk opened at center with dissolve
    $ preferences.set_volume("voice", 0.50)
    voice "kk77.ogg"
    kk "What?!"

    show kurtney talk angry at center with dissolve

    "I whispered in Kurt's ears."
    $ preferences.set_volume("voice", 0.45)
    voice "m163.ogg"
    m "Just let it slide dude. I will find a way to report this nasty professor."

    show kurtney smile with dissolve

    voice "kk78.ogg"
    kk "O-O-Okaay..."

    jump talkOnHarass


label talkOnHarass:
    $ helpedYui = False
    scene black with fade
    centered "A few days later..."

    if lunchWithYui is True:
        scene school building with fade
        
        "What a nice landscape."

        "I see [y] walking across the ground. With a sad expression on her face."

        show yui worry closed with fade
        voice "m164.ogg"
        m "Hey [y]! How's your class doing?"

        voice "m165.ogg"
        m "You called me out to talk about something?"

        show yui worry opened with dissolve
        voice "yui55.ogg"
        y "Y-yeah..."

        show yui worry with dissolve
        voice "yui56.ogg"
        y "It's about that law you talked about."

        voice "m166.ogg"
        m "The Safe Spaces Act? What about it?"

        voice "yui57.ogg"
        y "I have something to talk about related to it...."

        voice "m167.ogg"
        m "Tell me about it."

        hide yui worry with dissolve

        "While clasping her hands firmly for a while, she finally opened her mouth."

        show yui worry opened with dissolve
        voice "yui58.ogg"
        y "It's about my professor..."
        
        voice "yui59.ogg"
        y "He's doing something bad... And I can't do anything to stop it."

        voice "m168.ogg"
        m "Who's this professor? Is he teaching here?"

        show yui angry with dissolve
        voice "yui60.ogg"
        y "Y-yeah... I hate him. That disgusting person."

        voice "yui61.ogg"
        y "When he gave a test the other day... He stares at the girls in a lascivious manner."

        voice "yui62.ogg"
        y "When we are in the laboratory, he sneakily touches the butt of some of the girls."

        voice "yui63.ogg"
        y "Then he says, \"It's not my fault that you are sexy.\""

        voice "yui64.ogg"
        y "And then one time, he..."

        show yui crying with fade
        voice "yui65.ogg"
        y "He suddenly touched my shoulders... and pinched it in a manner that is so disgusting. Then he whispered something to my ear."

        voice "m169.ogg"
        m "WHAT?!" with vpunch

        show yui angry with dissolve
        voice "yui66.ogg"
        y "Aaaaah! I hate him. Just remembering it makes me puke."

        voice "yui67.ogg"
        y "I was almost close to crying in the classroom. I was really shaking and trembling."

        voice "yui68.ogg"
        y "The girls in my class can't speak up to him. Also when the boys stand up for us, he gives them a failing mark."

        voice "m170.ogg"
        m "Tell me who is this nasty person?"

        show yui worry opened with dissolve
        voice "yui69.ogg"
        y "H-h-his name is Butch..."

        voice "yui70.ogg"
        y "They said he was a new faculty teacher..."

        voice "m171.ogg"
        m "I see. So he's also teaching the First Year students."

        show yui worry with dissolve
        voice "yui71.ogg"
        y "M-Mark! I have a favor! Please help me out."

        voice "m172.ogg"
        m "Ahhhh..."

        $ badEndingGame = False
        $ helpedYui = False
        $ timeout = 10
        $ timeout_label = "ignorePerv"
        menu:
            "Should I help her out?"

            "Help her.":
                $ helpedYui = True
                pause 0.5

                $ hbbpoints += 5
                $ play_sound(addPoints)
                "You received {color=#40ff00}5 HBB Points.{/color}"

                python:

                    if persistent.achievementList[16] == False:
                                    
                        achievement.grant("Lending A Helping Hand")
                        renpy.notify("Achievement Unlocked: Lending A Helping Hand")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[16] = True


                voice "m173.ogg"
                m "Okay [y]! I will help you."

                voice "yui72.ogg"
                y "Thank you so much!"

                voice "yui73.ogg"
                y "Also before I forget to say... There was someone who took a video when he was doing the crime."

                voice "m174.ogg"
                m "Really? Then this will be easy. It should be a solid evidence for his disgusting act."

                $ yuiSpecial = True

                jump arrestButch

            "Don't help her.":
                jump ignorePerv
                
        label ignorePerv:
            $ badEndingGame = True

            voice "m175.ogg"
            m "I'm afraid I cannot help. I might get in trouble."

            if not kurtneyHelp:
                voice "kk79.ogg"
                kk "Is that so? That's a real shame..."

            else:
                voice "yui74.ogg"
                y "Is that so? That's a real shame..."

            jump badEndStory

    else:
        scene class2
        show kurtney talk opened
        with fade

        voice "kk80.ogg"
        kk "Dude... I have something to talk about."

        voice "kk81.ogg"
        kk "It's about that law you talked about."

        voice "m176.ogg"
        m "The Safe Spaces Act? What about it?"

        show kurtney smile with dissolve

        voice "kk82.ogg"
        kk "I think we can use this law against that professor."

        voice "m177.ogg"
        m "Tell me more about it."

        show kurtney angry talk with dissolve

        voice "kk83.ogg"
        kk "Just the other day, one of our girl classmate got sexually harassed."

        voice "m178.ogg"
        m "Really? That's bad."

        show kurtney talk opened with dissolve

        voice "kk84.ogg"
        kk "I've also got stories from other girls in First Year. According to them..."

        show kurtney angry talk with dissolve

        voice "kk85.ogg"
        kk "When he gave a test the other day... He stares at the girls in a lascivious manner."

        voice "kk86.ogg"
        kk "When they are in the laboratory, he sneakily touches the butt of some of the girls."

        voice "kk87.ogg"
        kk "Then he says, \"It's not my fault that you are sexy.\""

        voice "kk88.ogg"
        kk "And then one time, he... he tried to grope someone."

        voice "m179.ogg"
        m "Dude this is getting worse."

        voice "m180.ogg"
        m "We really need to do something."

        voice "kk89.ogg"
        kk "Yeah I know. Here comes the good part dude."

        voice "m181.ogg"
        m "What is good in this?"

        voice "kk90.ogg"
        kk "Someone took a video of that nasty bastard doing the crime."

        voice "m182.ogg"
        m "Really? That a solid evidence then!"

        voice "kk91.ogg"
        kk "I know right! That disgusting creep should rot in jail forever."

        show kurtney happy teeth with dissolve

        # voice "kk130.acc"
        kk "Now will you help me out?"

        show kurtney smile with dissolve

        voice "kk92.ogg"
        kk "Because of you, I learned of the Safe Spaces Act. I knew of the things which a person shouldn't ever do."

        voice "kk93.ogg"
        kk "You wanted to be an Attorney right? Help me use this \"Safe Spaces Act\" to arrest that nasty piece of ****."

        $ timeout_label = "ignorePerv"
        menu:
            "Should I help her?"

            "Help her.":
                pause 0.5

                $ hbbpoints += 5
                $ play_sound(addPoints)
                "You received {color=#40ff00}5 HBB Points.{/color}"

                python:

                    if persistent.achievementList[16] == False:
                                    
                        achievement.grant("Lending A Helping Hand")
                        renpy.notify("Achievement Unlocked: Lending A Helping Hand")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        persistent.achievementList[16] = True



                voice "m183.ogg"
                m "Okay [kk]! I will help you."

                voice "kk94.ogg"
                kk "Thank you so much!"

                $ renpy.end_replay()

                jump arrestButch

            "Don't help her.":
                $ kurtneyHelp = False
                $ renpy.end_replay()
                jump ignorePerv

    $ renpy.end_replay()

label arrestButch:
    stop music fadeout 0.5
    scene school gate with fade
    play sound "audio/music/Transition2.ogg"
    show screen arrestTransition
    pause 3.0
    hide screen arrestTransition

    scene black
    centered "A few days later..."

     
    $ preferences.set_volume("music", 0.12)
    $ play_music(fight,fadein=0.9)
    $ preferences.set_volume("voice", 0.30)
    $ preferences.set_volume("sfx", 0.15)
    if helpedYui is True:
        scene class2
        show butch smile
        with fade

        voice "newButch7.mp3"
        b "Bring out a pen and paper. We will be having a surprise quiz."

        hide butch smile
        $ preferences.set_volume("sfx", 0.25)
        show butch creepy laugh
        $ play_sound(pervlaugh,fadein=1.0)

        b "Hwehehehehewehweh"

        "Everyone" "What?!!"

        with hpunch

        pause 2.0

        hide butch creepy laugh with dissolve

        pause 2.0

        with fade
        $ preferences.set_volume("sfx", 0.13)
        $ play_sound(siren,fadein=1.0)
        $ preferences.set_volume("voice", 0.50)
        voice "m184.ogg"
        m "Hey [kk]! Something good will happen today."

        show kurtney talk opened with dissolve
        $ preferences.set_volume("voice", 0.60)
        voice "kk95.ogg"
        kk "What? There's nothing good happening when there's a surprise quiz."

        voice "kk96.ogg"
        kk "Police sirens?! Whaaaat?"

        voice "m185.ogg"
        m "Just wait and see dude. Haha~"

        voice "kk97.ogg"
        kk "Whatever Attorney Mark."

        voice "m186.ogg"
        m "Shut up."

        scene black

        window hide

        centered "A few minutes later..."

        scene hallway
        $ preferences.set_volume("sfx", 0.50)
        $ play_sound(walking,fadein=0.5)

        window hide

        "Footsteps can be heard in the hallway."

        pause 3.0

        scene class2
        $ preferences.set_volume("sfx", 0.50)
        $ play_sound(doorknock)
        $ preferences.set_volume("voice", 0.28)
        voice "newOfficer41.mp3"
        "???" "Excuse me. Please open the door."
        $ preferences.set_volume("sfx", 0.35)
        $ play_sound(radio,fadein=0.5)
        "Police radio echoing..."
        pause 1.5
        show butch angry with dissolve
        $ preferences.set_volume("voice", 0.35)
        voice "newButch8.mp3"
        b "Who the hell is disturbing my class!!!"

        hide butch angry
        $ preferences.set_volume("sfx", 0.50)
        $ play_sound(doorknock)

        "Continuous knocking on the door."
        
        $ play_sound(doorcreak)

        "Creeeeek. The door opens."

        show police neutral with fade

        "Uniformed personnels came in. They appear to be police."
        $ preferences.set_volume("voice", 0.50)
        voice "m187.ogg"
        m "Officer Greg!!!"

        hide police neutral with dissolve

        show butch suprise with dissolve
        $ preferences.set_volume("voice", 0.30)
        voice "newButch9.mp3"
        b "Why is there police here?!!"

        hide butch suprise with dissolve
        $ preferences.set_volume("sfx", 0.29)
        $ play_sound(people,fadein=4.0)

        "Everyone" "What's happening? Why are they here? Did someone kill?"

        show police neutral with fade
        $ preferences.set_volume("voice", 0.40)
        voice "newOfficer42.mp3"
        o "Everyone please calm down."
        stop sound fadeout 0.5
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer43.mp3"
        o "We have received a complaint that someone is sexually harassing a student."

        $ play_sound(radio)
        "Police radio echoing..."

        "The policeman looks at Butch."

        hide police neutral

        show butch angry 

        with dissolve

        voice "newButch10.mp3"
        b "What the hell are you looking at? I don't know anything about that."

        hide butch angry

        show police neutral

        with dissolve

        voice "newOfficer44.mp3"
        o "Don't explain to me. Everything that you say will be used against you."

        voice "newOfficer45.mp3"
        o "The complainant showed a solid proof of evidence."

        voice "newOfficer46.mp3"
        o "You will be coming with us. Do not resist."

        hide police with fade

        $ play_sound(people,fadein=4.0)

        "Everyone" "*gasps*"

        show police neutral with fade
        $ preferences.set_volume("voice", 0.47)
        voice "newOfficer47.mp3"
        o "Hey future Attorney! It looks like it went fine."
        $ preferences.set_volume("voice", 0.55)
        voice "m188.ogg"
        m "Waaah! Officer Greg you actually came."
        stop sound fadeout 0.5
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer48.mp3"
        o "It's because of you, we caught this disgusting molester. Thank you."
        $ preferences.set_volume("voice", 0.50)
        voice "m189.ogg"
        m "Are you praising me? Hahaha~ No big deal. I am destined to be the greatest Attorney anyways."
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer49.mp3"
        o "Hahaha! I like that attitude. Keep doing good things young man."
        $ preferences.set_volume("voice", 0.50) 
        voice "m190.ogg"
        m "Yes Sir!"

        stop sound fadeout 2.0

    # Kurt scene
    else:
        scene class2
        show butch smile
        with fade

        voice "newButch7.mp3"
        b "Bring out a pen and paper. We will be having a surprise quiz."

        hide butch smile
        $ preferences.set_volume("sfx", 0.25)
        show butch creepy laugh
        $ play_sound(pervlaugh,fadein=1.0)

        b "Hwehehehehewehweh"

        "Everyone" "What?!!"

        with hpunch

        pause 2.0

        hide butch creepy laugh with dissolve

        pause 2.0

        with fade
        $ preferences.set_volume("sfx", 0.13)
        $ play_sound(siren,fadein=1.0)
        $ preferences.set_volume("voice", 0.50)
        voice "m184.ogg"
        m "Hey [kk]! Something good will happen today."

        show kurtney talk opened with dissolve
        $ preferences.set_volume("voice", 0.60)
        voice "kk95.ogg"
        kk "What? There's nothing good happening when there's a surprise quiz."

        voice "kk96.ogg"
        kk "Police sirens?! Whaaaat?"

        voice "m185.ogg"
        m "Just wait and see dude. Haha~"

        voice "kk97.ogg"
        kk "Whatever Attorney Mark."

        voice "m186.ogg"
        m "Shut up."

        scene black

        window hide

        centered "A few minutes later..."

        scene hallway
        $ preferences.set_volume("sfx", 0.50)
        $ play_sound(walking,fadein=0.5)

        window hide

        "Footsteps can be heard in the hallway."

        pause 3.0

        scene class2
        $ preferences.set_volume("sfx", 0.50)
        $ play_sound(doorknock)
        $ preferences.set_volume("voice", 0.28)
        voice "newOfficer41.mp3"
        "???" "Excuse me. Please open the door."
        $ preferences.set_volume("sfx", 0.35)
        $ play_sound(radio,fadein=0.5)
        "Police radio echoing..."
        pause 1.5
        show butch angry with dissolve
        $ preferences.set_volume("voice", 0.35)
        voice "newButch8.mp3"
        b "Who the hell is disturbing my class!!!"

        hide butch angry
        $ preferences.set_volume("sfx", 0.50)
        $ play_sound(doorknock)

        "Continuous knocking on the door."
        
        $ play_sound(doorcreak)

        "Creeeeek. The door opens."

        show police neutral with fade

        "Uniformed personnels came in. They appear to be police."
        $ preferences.set_volume("voice", 0.50)
        voice "m187.ogg"
        m "Officer Greg!!!"

        hide police neutral with dissolve

        show butch suprise with dissolve
        $ preferences.set_volume("voice", 0.30)
        voice "newButch9.mp3"
        b "Why is there police here?!!"

        hide butch suprise with dissolve
        $ preferences.set_volume("sfx", 0.29)
        $ play_sound(people,fadein=4.0)

        "Everyone" "What's happening? Why are they here? Did someone kill?"

        show police neutral with fade
        $ preferences.set_volume("voice", 0.40)
        voice "newOfficer42.mp3"
        o "Everyone please calm down."
        stop sound fadeout 0.5
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer43.mp3"
        o "We have received a complaint that someone is sexually harassing a student."

        $ play_sound(radio)
        "Police radio echoing..."

        "The policeman looks at Butch."

        hide police neutral

        show butch angry 

        with dissolve

        voice "newButch10.mp3"
        b "What the hell are you looking at? I don't know anything about that."

        hide butch angry

        show police neutral

        with dissolve

        voice "newOfficer44.mp3"
        o "Don't explain to me. Everything that you say will be used against you."

        voice "newOfficer45.mp3"
        o "The complainant showed a solid proof of evidence."

        voice "newOfficer46.mp3"
        o "You will be coming with us. Do not resist."

        hide police with fade

        $ play_sound(people,fadein=4.0)

        "Everyone" "*gasps*"

        show police neutral with fade
        $ preferences.set_volume("voice", 0.47)
        voice "newOfficer47.mp3"
        o "Hey future Attorney! It looks like it went fine."
        $ preferences.set_volume("voice", 0.55)
        voice "m188.ogg"
        m "Waaah! Officer Greg you actually came."
        stop sound fadeout 0.5
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer48.mp3"
        o "It's because of you, we caught this disgusting molester. Thank you."
        $ preferences.set_volume("voice", 0.50)
        voice "m189.ogg"
        m "Are you praising me? Hahaha~ No big deal. I am destined to be the greatest Attorney anyways."
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer49.mp3"
        o "Hahaha! I like that attitude. Keep doing good things young man."
        $ preferences.set_volume("voice", 0.50) 
        voice "m190.ogg"
        m "Yes Sir!"

        stop sound fadeout 2.0

        hide police neutral
        show kurtney talk opened 
        with dissolve

        voice "kk98.ogg"
        kk "Hey! Don't forget about me!!"

        show police neutral 
        hide kurtney talk opened
        with fade
        $ preferences.set_volume("voice", 0.30)
        voice "newOfficer50.mp3"
        o "Oh yes, the Attorney's friend. You will also receive compensation."

        hide police neutral
        show kurtney angry talk with dissolve
        $ preferences.set_volume("voice", 0.50)
        voice "kk99.ogg"
        kk "Nevermind compensation, why is my name \"Attorney's friend\"?!!!"

        hide police neutral

        with dissolve

        $ play_sound(crowdlaugh,fadein=1.5)

        "Everyone" "HAHAHAHA!!!"

        $ kurtneySpecial = True
    
    jump goodEndStory

label goodEndStory:

    $ goodEnding = True

    scene black

    pause 3.0

    centered "[b] was thrown into court later on to be imprisoned."

    centered "Mark was awarded a badge of honor of the school."

    centered "But that's not all!"

    centered "Mark became famous in school and many girls talked to him."

    centered "As in the words of Mark...."

    centered "\"Justice will always prevail!\""

    centered "--Greatest Attorney That Ever Lived."

    show good ending with pixellate

    pause 5.0
    hide good ending with pixellate

    centered "GOOD END"
    python:

        if persistent.achievementList[11] == False:
                    
            achievement.grant("Good End")
            renpy.notify("Achievement Unlocked: Good End")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[11] = True

    stop music fadeout 3.0

    pause 3.0

    $ renpy.end_replay()

    if hbbpoints >= 20 and yuiSpecial:
        jump specialEndYui
    elif hbbpoints >= 20 and kurtneySpecial:
        jump specialEndKurtney
    $ timeout_label = None
    menu:
        "You have met a good ending! Hint: To unlock bonus content, finish with 20 HBB Points above."

        "Retry from the start.":
            jump yui_start_case_1

        "Return to Main Menu":
            return




label badEndStory:

    scene black

    centered "[b] went on to harass lots of students. This went on without anyone stopping him because of his position."

    centered "When the police caught on to the news, [b] went on to hiding. Never getting caught for his crimes."

    show bad ending with pixellate

    pause 5.0

    hide bad ending with pixellate
    centered "BAD END"

    python:

        if persistent.achievementList[10] == False:
                    
            achievement.grant("Bad End")
            renpy.notify("Achievement Unlocked: Bad End")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[10] = True

    $ renpy.end_replay()
    $ timeout_label = None
    scene white
    menu:
        "You have met a bad ending! Hint: To unlock bonus content, finish with a good ending and 20 HBB Points above."

        "Retry from the start.":
            jump yui_start_case_1

        "Return to Main Menu":
            return

label specialEndYui:

    # Library scene
    
    pause 3.0
    scene black with fade
    centered "A few days later..."

    scene hallway with fade
    
    $ play_music(quirky)
    
    voice "m217.ogg"
    m "Peace has finally been restored!"

    voice "m218.ogg"
    m "After the incident, the police organization talked to me about doing part-time job for them."

    voice "m219.ogg"
    m "I guess that's not too bad. I can get some experience."

    show kurtney worry with fade 
    $ preferences.set_volume("voice", 0.60) 
    voice "kk100.ogg"
    kk "Heeeey! Why didn't you wait for me earlier this morning?"
    $ preferences.set_volume("voice", 0.50) 
    voice "m220.ogg"
    m "I'm sorry! I was going to meet a friend."

    voice "kk101.ogg"
    kk "A friend? You? There's no way that's possible."

    voice "m221.ogg"
    m "Oh! And there she is!"

    "....."

    voice "m222.ogg"
    m "Hey Yui!"

    hide kurtney worry
    show yui blush at left
    with dissolve
    $ preferences.set_volume("voice", 0.45) 
    voice "yui75.ogg"
    y "Good morning Mark! Did you see my message last night?"

    voice "m223.ogg"
    m "Yeah but I wasn't able to reply. I was too sleepy."

    voice "yui76.ogg"
    y "No its fine!"

    show kurtney talk opened at right with dissolve

    voice "kk102.ogg"
    kk "What the hell is happening?"
    $ preferences.set_volume("voice", 0.40) 
    show yui smile opened at left with dissolve
    voice "yui77.ogg"
    y "Oh I'm sorry for not introducing myself."

    voice "yui78.ogg"
    y "My name is Yui and I am a First Year."
    $ preferences.set_volume("voice", 0.45) 
    voice "kk103.ogg"
    kk "I'm his childhood friend and his classmate."
    $ preferences.set_volume("voice", 0.40) 
    voice "yui79.ogg"
    y "Oh I see!"

    show kurtney smile at right with dissolve
    $ preferences.set_volume("voice", 0.45)
    voice "kk104.ogg"
    kk "So what's your relationship with Mark?"
    $ preferences.set_volume("voice", 0.40)
    show yui blush closed at left with dissolve
    voice "yui80.ogg"
    y "O-ohhh we are f-frie-"
    $ preferences.set_volume("voice", 0.45)
    voice "m224.ogg"
    m "Hey [kk] you're being rude."

    show yui smile opened at left with dissolve 

    voice "m225.ogg"
    m "I just happened to run into her in the school ceremony. She was lost and couldn't find her classroom so I helped her."

    show kurtney happy teeth at right with dissolve

    voice "kk105.ogg"
    kk "Is that all?"

    show yui blush at left with dissolve 
    voice "yui81.ogg"
    y "H-He also saved my life..."

    voice "kk106.ogg"
    kk "Saved your life you say?"
    $ preferences.set_volume("voice", 0.42)
    voice "m226.ogg"
    m "Well, it was because of Professor Butch."

    voice "m227.ogg"
    m "That bastard was also teaching in First Year and sexually harassed students."

    voice "m228.ogg"
    m "It just so happened that [y] came to me and asked for help. That's all."

    show yui smile close at left  
    show kurtney smile at right 
    with dissolve
    voice "kk107.ogg"
    kk "Hmmmm! I see..."

    voice "kk108.ogg"
    kk "That's good."

    voice "kk109.ogg"
    kk "For you I guess."

    voice "m229.ogg"
    m "What? You're not happy that I saved her?"

    show kurtney angry talk at right with dissolve

    voice "kk110.ogg"
    kk "No! I..."

    kk "...."

    voice "kk111.ogg"
    kk "Ugh! Whatever. You're pissing me off."

    hide kurtney angry talk at right 
    hide yui smile close at left 
    with fade

    voice "m230.ogg"
    m "Uhhh sorry about that. She's a little bit weird."
    $ preferences.set_volume("voice", 0.37)
    show yui blush with dissolve
    voice "yui83.ogg"
    y "It's fine! Actually I'm quite jealous cause she has a childhood friend like you..."
    $ preferences.set_volume("voice", 0.42)
    voice "m231.ogg"
    m "Jealous? Why? I'm not that really great though."
    $ preferences.set_volume("voice", 0.39)
    voice "yui84.ogg"
    y "You are! You saved my life."

    voice "yui85.ogg"
    y "As a matter of fact, I want to request something to you."

    voice "m232.ogg"
    m "What is it? As long as I can do it."

    voice "yui86.ogg"
    y "You said that you were not that good at studying right?"

    voice "m233.ogg"
    m "Yeah?"

    voice "yui82.ogg"
    y "I want to help you out. The midterm test are also coming near."

    voice "m234.ogg"
    m "Really? That would be great!"

    voice "yui87.ogg"
    y "So uhm..."

    voice "yui88.ogg"
    y "Will you come with me to the library after school?"

    "...."

    menu:
        "Come to library with Yui after school?"

        "Study with her.":
            jump libraryDate

        "Don't study.":
            jump creditss



label libraryDate:

    stop music
    scene library with fade
    $ preferences.set_volume("music", 0.18)
    $ preferences.set_volume("voice", 0.39)
    $ play_music(tutorial)
    
    voice "m235.ogg"
    m "Do you know the answer to this one?"

    voice "yui89.ogg"
    y "Ohh that's easy."

    voice "m236.ogg"
    m "Sorry I'm really bad at math."

    voice "yui90.ogg"
    y "It's okay. That's why I'm here to help you."

    voice "yui91.ogg"
    y "To answer this equation...."

    voice "yui92.ogg"
    y "You use this formula."

    voice "m237.ogg"
    m "Ohh so it goes just like that huh?"

    voice "yui93.ogg"
    y "Yup! It's easy right?"

    voice "m238.ogg"
    m "[y] you're really good at teaching!"

    voice "m239.ogg"
    m "When I'm in class, what goes in my left ear comes out in my right ear."

    voice "yui94.ogg"
    y "Hahahaha!"

    scene black with fade 

    centered "After some time..."
    $ preferences.set_volume("music", 0.15)
    scene library with fade
    voice "yui95.ogg"
    y "Mark? Do you have a girlfriend?"

    voice "m240.ogg"
    m "I have none. Why?"

    voice "yui96.ogg"
    y "What am I for you?"

    voice "m258.ogg"
    m "A friend?"

    voice "yui97.ogg"
    y "You see, I think I..."

    voice "m241.ogg"
    m "What is this drama?"

    voice "yui98.ogg"
    y "Please I'm serious!"

    voice "m242.ogg"
    m "Okay I'm listening."

    voice "yui99.ogg"
    y "I think I've fallen in love."

    voice "m243.ogg"
    m "That's good for you!"

    voice "m244.ogg"
    m "With who?"

    voice "yui100.ogg"
    y "Are you not listening?!!"

    voice "m245.ogg"
    m "Can you repeat it again?"

    voice "yui101.ogg"
    y "Gosh. This is so embarassing. I've fallen in love with you! Please don't make me say it again."

    voice "m246.ogg"
    m "Whaaaaa?"

    voice "m247.ogg"
    m "Why meeee?"

    voice "yui102.ogg"
    y "I don't know!! I was just happy that you saved me. Then the next day, my mind can't stop thinking about you."

    voice "yui103.ogg"
    y "You've always been in my mind since then!"

    voice "yui104.ogg"
    y "So... Mark."

    voice "yui105.ogg"
    y "Will you please go out with me?"

    stop music fadeout 0.5
    python:

        if persistent.achievementList[12] == False:
                        
            achievement.grant("Special End")
            renpy.notify("Achievement Unlocked: Special End")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[12] = True
    pause 3.0
    $ preferences.set_volume("music", 0.30)
    $ preferences.set_volume("sfx", 0.30)
    hide screen displayHBBPoints
    hide screen showNotesButton
    jump creditss


label specialEndKurtney:

    pause 3.0
    scene black with fade
    centered "A few days later..."

    scene hallway with fade

    $ play_music(quirky)
    
    voice "m217.ogg"
    m "Peace has finally been restored!"

    voice "m218.ogg"
    m "After the incident, the police organization talked to me about doing part-time job for them."

    voice "m219.ogg"
    m "I guess that's not too bad. I can get some experience."

    show kurtney worry with fade 

    voice "kk100.ogg"
    kk "Heeeey! Why didn't you wait for me earlier this morning?"

    voice "m248.ogg"
    m "I was on cleaning duty today dude. I'm sorry."

    voice "m249.ogg"
    m "Also, I told you last night that I'm on cleaning duty. Did you forgot?"

    voice "kk112.ogg"
    kk "Yeah I think. I was busy playing games."

    scene class2 with fade

    pause 0.5

    show kurtney happy teeth with dissolve

    voice "kk113.ogg"
    kk "Hey Mark! What do you say going to arcade after school?"

    voice "m250.ogg"
    m "Sounds like a good idea!"

    voice "kk114.ogg"
    kk "Wanna go? I'll treat you."

    voice "m251.ogg"
    m "Woah really? Is this really you?"

    voice "kk115.ogg"
    kk "Whaaaat? I'm being this kind to you and you still complain?"

    voice "m252.ogg"
    m "I get it. I get it. Let's go! This'll be fun."

    voice "m253.ogg"
    m "It's been a long time since we've gone to the arcade."

    voice "kk116.ogg"
    kk "Yeah!"

    voice "kk117.ogg"
    kk "Also, it's my way of thanking you for helping me the other day."

    voice "m254.ogg"
    m "Don't mind it. You're my precious childhood friend."

    voice "kk118.ogg"
    kk "Seriously. Stop that."

    voice "m198.ogg"
    m "What?"

    voice "kk119.ogg"
    kk "Nothing!"

    scene arcade with fade
    $ play_music(jazzy)
    $ play_sound(arcade, fadein=0.5,fadeout=0.5)
    
    voice "m255.ogg"
    m "There's a lot of people here, huh."

    voice "kk120.ogg"
    kk "Let's go try this claw machine!"

    voice "m256.ogg"
    m "Yeah sure."

    voice "kk121.ogg"
    kk "Please get me this stuffed toy..."

    m "I'll try. I haven't done this in a long time"

    voice "kk122.ogg"
    kk "You can do it!!!"

    # voice "m257.ogg"
    # m "What if I win?"

    # kk "You'll never win in a race against me though?"

    # voice "m259.ogg"
    # m "I guess I never won a single racing game against you. Hahahaha!"

    pause 5.0

    window hide

    stop sound fadeout 0.5

    scene town with fade

    window show

    "........."

    $ play_music(evans,fadein=0.5)

    m "That was a lot of fun!"
    # voice "m260.ogg"
    # m "In the end, I still lost."

    voice "kk123.ogg"
    kk "I'll never forget this moment."

    m "Hahaha we can do this again sometime."
    # voice "m261.ogg"
    # m "You driving maniac."

    voice "kk124.ogg"
    kk "Uhmm Mark? Can I request something?"

    voice "m262.ogg"
    m "So what is it? Your request?"

    voice "kk125.ogg"
    kk "Hmmmm."

    voice "kk126.ogg"
    kk "Do you promise you'll not get angry?"

    voice "m263.ogg"
    m "Yeah! As long as its not jumping off a cliff. Then it's fine."

    voice "kk127.ogg"
    kk "H-H-Hold..."

    voice "m264.ogg"
    m "Hold?"

    voice "kk128.ogg"
    kk "Hold my hands..."

    voice "m265.ogg"
    m "Did it get hurt? Sure I'll hold your hands."

    kk ".........."

    voice "m266.ogg"
    m "Why'd you suddenly got red?"

    voice "kk129.ogg"
    kk "You stupid monkey!"
    
    pause 3.0
    python:

        if persistent.achievementList[12] == False:
                        
            achievement.grant("Special End")
            renpy.notify("Achievement Unlocked: Special End")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            persistent.achievementList[12] = True
    stop music fadeout 0.5
    hide screen displayHBBPoints
    hide screen showNotesButton
    play music "audio/music/Future-Business_v001.mp3" fadein 0.5
    
    jump creditss











    
    




