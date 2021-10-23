image kitchen = im.Scale("images/bg kitchen.webp", 1920, 1080)
image outside = im.Scale("images/bg outside.webp", 1920, 1080)

define kk = Character('Kurt')
define y = Character('Yui')
define t = Character('Teacher Clarisse')
define b = Character('Butch')

default points = 0

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

    centered "The Safe Spaces Act is an act defining gender-based sexual harassment 
    in streets, public spaces, online, workplaces, and educational or training institutions."  

    centered "This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions."

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
        # Story will diverge from this point. Will converge at some point.

        # Meet Yui
        "Take the train.":
            jump meetWithYui

        # Meet Kurt(friend)
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

    kk "Haha!!"

    m "Hey, do you wanna hear something interesting?"

    kk "What? If it's boring then I'm not listening to you."

    #show kurt without headphone

    m "I saw the news this morning. There was a new law.."

    kk "What kind of law?"

    $ firstTryWrong = False

    menu kurtFirstQuestion:
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

                $ points += 3
                "You received {color=#40ff00}3 HBB Points.{/color}"
            

        "Rebuild Act No. 11313":
            "Not the right answer."
            $ firstTryWrong = True
            jump kurtFirstQuestion

    #######################################
    kk "That's cool. Tell me more about it."

    m "Yeah its a great law."

    $ firstTryWrong = False

    menu kurtSecondQuestion:
        "It is also know as ...."
        
        "Safe Spaces Act":
            "Great answer!"
            if firstTryWrong is False:
                $ points += 3
                "You received {color=#40ff00}3 HBB Points.{/color}"
            
        "Safe Pace Act":
            "Wait this is wrong."
            $ firstTryWrong = True
            jump kurtSecondQuestion
        
        "Safe Guardian Act":
            "Not the right answer."
            $ firstTryWrong = True
            jump kurtSecondQuestion
       
        "Safe Insurrance Act":
            "Not the greatest answer."
            $ firstTryWrong = True      
            jump kurtSecondQuestion

    kk "So it is called \"Safe Spaces Act\"?"

    m "Yeah! It's a cool name right."

    #show kurt open mouth
    kk "Sure. But what does it mean?"

    menu kurtThirdQuestion:
        "Wait, what does the Safe Spaces Act mean again?"

        "To protect Earth from aliens.":
            kk "Dude are you serious?"

            kk "Stop spouting nonsense."
            
            m "Hahaha~ I'm just kidding!"

            m "The law was created to..."

            jump kurtInfo

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
        "To protect men and women from gender-based sexual harassment.":
            "Nice job! Correct answer."
            $ points += 3
            "You received {color=#40ff00}3 HBB Points.{/color}"
            
            label kurtInfo:
                m "To protect men and women from gender-based sexual harassment."

                m "Gender-based streets and public spaces sexual harassment include..."

                m "a) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs."

                m "b) Persistent uninvited comments or gestures on a person's appearance."

                m "c) Relentless requests for personal details."

                m "d) Statement of sexual comments and suggestions."

                m "e) Public masturbation or flashing of private parts, groping, making offensive body gestures 
                at someone, and other similar lewd sexual actions."

                m "f) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. 
                This may include cursing, leering and intrusive gazing, and taunting."

                m "g) Persistent telling of sexual jokes, use of sexual names."

                m "And last but not the least."
                
                m "h) Stalking."

                kk "That was a lot! How'd you memorize it?"

                m "Well you know... I wanted to be a lawyer. So this much is not that big deal."

                kk "Attorney Mark? Sounds nice haha~"

                m "Stop mocking me dude."

                kk "So what happens when I do any of those things?"

                m "Let's continue later dude. We are close to the school."

                kk "Tell me about it okay? It's an interesting law."

        "To protect public and online spaces from danger.":
            kk "What danger? Explain it clearly."

            m "Uhhhh.. wait let me remember..."

            m "Errr... it is to..."

            jump kurtInfo

        ########################################

    jump schoolCeremony


label meetWithYui:
    scene bg train with fade

    "Eh, it is surprisingly quiet today..."

    "Even though its the first day of class?"

    "Well, I shouldn't be complaining about this."

    "I kinda like this atmosphere."

    "Hopefully, this day goes successful."

    "...."

    "Operator" "Arriving at station. Please check your belongings before getting out. Thank you."

    "{i}Footsteps of people{/i}"

    "Moving closer towards the exit... I hear some conversation."

    "???" "Hey there sexy little miss. Are you free tonight and have a drink." 

    "???" "Don't worry, we won't do anything do bad to you hehehe..."

    "???" "Do you need money or anything? Just tell us."

    "I can see three old men harassing a young student girl."

    "I notice that the girl is trembling and shaking."

    "Girl" "Plea-please l-l-leave me alo-lone..." 

    "???" "Hahaha!! She's scared like a child."

    "???" "Hey, you're teasing her too much. She might report us."

    "???" "Boss, don't worry. She can't even say the sentence straight."

    $ deathFlag = False
    $ metYui = True
    menu trainScene:
        "What should I do?"


        "I'll pick a fight with them." if deathFlag is False:
            $ deathFlag = True

            m "Hey you bastards! Stop harrassing that girl."

            "???" "Who the hell are you? His boyfriend perhaps?"

            "???" "You little punk talking to me like that. I'll crush you."

            "???" "Take this you pesky little boy."

            "BAM!" with vpunch

            "AAHHH!" with hpunch

            "PAAAK!" with vpunch

            m "AAAAAAH!!!"

            "Achievement Unlocked: Punched in the Face"

            "....Officer!"

            jump withOfficer

        "I'll go and inform the train security.":
            "Good choice!"
            $ points += 3
            "You received {color=#40ff00}3 HBB Points.{/color}"

            m "Officer! Officer!!"

            m "I saw three old men harassing a girl student! Please help me."

            "Officer" "I see. Bring me to them."

            label withOfficer:
                m "Officer! Here!"

                m "These old men are harassing this girl."

                "???" "What the hell. Run guys!!"

                "???" "Holy crap don't leave me."

                "???" "Dammnit!"

            #show Yui
            "Girl" "Uwaaaaah! Thank y-y-you sooo much!!"

            m "Ohhh... I didn't really do anything..."

            "Girl" "You saved my life...."

            m "Life?"

            "Girl" "Uhm..."

            m "Yes?"

            "Girl" "Can you tell me your name?"

            m "Ohhh. My name is Mark. How about you?"

            "Girl" "Y-Y-Yu.."

            m "Yu?"

            "She's gotten a bit red of a sudden..."

            "Girl" "Ple-please call me Yui."

            m "[y], huh? What a cute name."

            y "EHHH?!! Cute?"

            y "{i}......waaah!{/i}"

            m "Hey, [y]. I saw you earlier that you were shaking and trembling."

            y "Yeah that was embarassing to see...."

            y "You see, when I was a child... I had a trauma."

            m "A trauma? Can I hear more of this?"

            y "Uhmmm y-yes..."

            y "When I was in 4th Grade, my boy classmates would make fun of my appearance."

            y "It made me stop going to school... And I was homeschooled since then."

            m "I can't imagine how you must feel. My heart hurts for you."

            m "You know what? I have something interesting to tell you!"

            y "What is it?"

            m "It's about a law."

            y "A law? What kind of law?"

            menu yuiFirstQuestion:
                "Aaaaah... What is it again? The law that was approved on 17th of April, 2019?"

                "Re-semiprivate Act No. 11313":
                    "Wrong answer!"
                    jump yuiFirstQuestion

                "Reprivate Act No. 11313":
                    "Think again..."
                    jump yuiFirstQuestion

                "Republic Act No. 11313":
                    "Great answer!"
                    $ points += 3
                    "You received {color=#40ff00}3 HBB Points.{/color}"
                    

                "Rebuild Act No. 11313":
                    "Not the right answer."
                    jump yuiFirstQuestion

            #######################################
            y "What is that law?"

            m "This law is..."

            menu yuiSecondQuestion:
                "It is also know as ...."
                
                "Safe Spaces Act":
                    "Correct!!"
                    $ points += 3
                    "You received {color=#40ff00}3 HBB Points.{/color}"
                    
                "Safe Pace Act":
                    "Wait this is wrong."
                    jump yuiSecondQuestion
                
                "Safe Guardian Act":
                    "Not the right answer."
                    jump yuiSecondQuestion
            
                "Safe Insurrance Act":
                    "Not the greatest answer."      
                    jump yuiSecondQuestion

            y "So it is called \"Safe Spaces Act\"?"

            m "Yeah! It's a cool name right?"

            #show kurt open mouth
            y "Uhm. But what does it mean?"

            menu yuiThirdQuestion:
                "Wait, what does the Safe Spaces Act mean again?"

                "To protect Earth from aliens.":
                    #show yui laugh
                    y "Wait that's really funny~"

                    y "Please tell it to me seriously..."
                    
                    m "Hahaha~ I'm just kidding!"

                    m "The law was created to..."

                    jump yuiInfo

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
                "To protect men and women from gender-based sexual harassment.":
                    "Nice job! Correct answer."
                    $ points += 3
                    "You received {color=#40ff00}3 HBB Points.{/color}"
                    
                    label yuiInfo:
                        m "To protect men and women from gender-based sexual harassment."

                        m "Gender-based streets and public spaces sexual harassment include..."

                        m "a) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs."

                        m "b) Persistent uninvited comments or gestures on a person's appearance."

                        m "c) Relentless requests for personal details."

                        m "d) Statement of sexual comments and suggestions."

                        m "e) Public masturbation or flashing of private parts, groping, making offensive body gestures 
                        at someone, and other similar lewd sexual actions."

                        m "f) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. 
                        This may include cursing, leering and intrusive gazing, and taunting."

                        m "g) Persistent telling of sexual jokes, use of sexual names."

                        m "And last but not the least."

                        m "h) Stalking."

                        y "That was a lot! How'd you memorize it?"

                        m "Well you know... I wanted to be a lawyer. So this much is not that big deal."

                        y "You wanted to be an attorney? That sounds really nice~"

                        m "Thank you ehehe..."

                        y "So what happens to the bad guys when they do those things?"

                        m "Uhm... Wait I'm kinda getting late for the school ceremony."

                        m "I'll talk to you again when I see you in this station!"

                "To protect public and online spaces from danger.":
                    kk "What danger? Please explain it clearly."

                    m "Uhhhh.. wait let me remember..."

                    m "Errr... it is to..."

                    jump yuiInfo

                    

        "I'll pretend that I didn't hear the conversation.":
            m "I should just ignore them..."

            m "I don't wanna get in trouble."

            # IMPLEMENT BAD ENDING!

            #Train end scene       
    "Officer" "Hey kids. You better get going now. I'll clean this mess up."

    "Officer" "Based on the Implementing Rules and Regulation of Republic Act No. 11313..."

    "Officer" "Those guys broke the law by (1) Making unwanted invitations."

    "Officer" "(2) Making statements of sexual comments and suggestions."

    "Officer" "(3) Making advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety." 

    "Officer" "This may include cursing, leering and intrusive gazing, and taunting."

    m "WOW! That's a really great law."

    "Officer" "I know kid."

    "Officer" "Now go on your way. I'll take care of them. In jail of course."
    
    m "Yes sir."

    y "Uhmmm..."

    y "See you Mark! Thank you again..."

    m "Bye Yui. No worries. I just can't stand it when I see someone getting harassed."

    y "Uhhhm.. I hope I can see you aga-"

    #Train sound
    "{i}A train passed by.{/i}"

    m "What?"

    y "No, nothing!!! Goodbye!"

    jump schoolCeremony

label schoolCeremony:
    "B Highschool. A prestigious school where only the best can enter."

    "I'm so lucky to be here."

    "...."

    "Student Council President" "To all the newcomers, I welcome you!"

    "Student Council President" "I hope that you can achieve your dreams in this school."

    "Student Council President" "To all those that are nearing graduation, I hope you achieved what you wanted here."

    "Student Council President" "That is all for my speech. Thank you!"

    "{i}Students clapping{/i}"

    if metYui is True:
        kk "Dude! I hope we are classmates in this new school year."

        m "Oh please no."

        kk "Why? I'm fun to hang out with right?"

        m "Yeah yeah whatever you say."

        "This is Kurt. My weird friend. Our friendship started weird. When I was in 1st Year, this guy randomly talked to me when I was eating alone in cafeteria."

        "But I don't hate it at all."

        kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"

        m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

        kk "You poor little thing."

        m "Well, don't even talk like you have one."

        kk "Hahaha~ Don't worry about me. I'm more worried about your future."

        m "I'm not a child for you to worry about."

        kk "Haha!!"

    else:
        kk "Dude! I hope we are classmates in this new school year."

        m "Oh please no."

        kk "Why? I'm fun to hang out with right?"

        m "Yeah yeah whatever you say."

    jump afterCeremony

label afterCeremony:
    kk "Lemme check the school bulletin to know our section."

    m "Sure dude. Gonna go to the bathroom first."

    kk "Meet me in near the school bulletin okay?"
    
    m "Yeah just go."

    "A new school year..."

    "I hope it is fun..."

    "Last year, I was a loner in my class."

    "But thankfully, I met Kurt. He's a really good friend."

    #Flag to check if USER accepts lunch invite
    $ lunchWithYui = True

    if metYui is True:

        "???" "Hey..."

        "???" "M-M-Mark!"

        m "Ehhhhh!!!?"

        m "Yui?! You go to my school?"

        y "Y-Yeah! Did you not no-notice my uniform?"

        m "I did not notice it at all. Oh my!"

        m "So you are a First Year student."

        m "Why didn't you tell me?"

        m "No.. sorry. It's my fault."

        y "No... it's fine!"

        y "*whispers* You wouldn't want to go with a girl like me..."

        m "What was that? You were mumbling something."

        y "It's totally nothing!"

        y "Uhm... M-M-Mark?"

        m "Yeah?"

        y "Can you help me get to my classroom?"

        m "Are you perhaps lost?"

        y "Yeah... this school is really big."

        m "No wonders. It's just like me when I was a First Year student."

        m "You are currently in the Second Year's building."

        # This choice will determine who will eat lunch with MC
        menu findRoomWithYui:
    
            "Go and find the classroom with Yui.":
                m "Haaa.."

                y "Waaaah.. I'm so sweaty."

                m "Yeah it's kinda far from our building. Hahaha~"

                "{i}8:50 AM{/i}"

                m "The first bell is gonna ring now."

                m "I'm going back now [y]!"

                m "Have fun in there!"

                y "W-w-waaaait Mark!"

                y "Uhm...."

                y "If it's fine with you.."

                y "Can I treat you later in lunch? As a thanks for helping me..."

                menu:
                    "Ehhhh? I've never been invited by a girl to lunch. What should I do?"

                    "Sure I'll go eat with you.":
                        m "Sure I'll go eat with you."

                        y "For real? Waaaah!"

                        m "Wait why are you so happy?"

                        m "Ready your money though. I'm a big eater."

                        y "Ehehe.. sure! You can choose whatever you want."

                        "{i}Ding dong dang {/i}"

                        m "Oh crap that's the bell!"

                        m "I'll be going now [y]!"

                        y "See you later.... M-Mark."

                        jump lunch

                    "Sorry, maybe next time?":
                        m "Sorry, maybe in another day."

                        y "Oh.... that's... a shame."

                        y "I... I see..."

                        y "See you..."

                        "She left running while her hands is in her eyes."

                        "...."

                        jump lunch

            "Go to Kurt in the school bulletin and leave Yui":
                $ lunchWithYui = False
                m "I'm sorry [y]. I can't help you. I have somewhere to go with my friend."

                y "Ah.... Is that so?"

                y "That's a real shame."

                y "I'll be going now Mark."

                "She left running while her hands is in her eyes."

                "...."

                jump lunch
    else:

        "???" "Uhmmm..."

        "???" "Excu-cuse m-m-me....!"

        "Looking at my back, there is someone pull my sleeves..."

        m "Uhhhh.. Hello?"

        m "You are?"

        y "Can you help me get to my classroom?"

        m "Are you perhaps lost?"

        y "Yeah... this school is really big."

        m "No wonders. It's just like me when I was a First Year student. Haha~"

        m "You are currently in the Second Year's building."

        jump findRoomWithYui

label lunch:

    if lunchWithYui is True:
        "{i}Ding dong dang {/i}"

        kk "Hey dude wanna go to cafeteria?"

        m "Sorry dude. I'm meeting someone today."

        kk "Meeting someone? Hey hey hey what's happening to Mr. Mark, huh?"

        m "I'm going ahead. Eat with yourself."

        kk "Wah! This little punk."

        scene bg cafeteria

        y "Hey Mark! Here!"

        m "Sorry [y]. Did you wait?"

        y "No... I just got here..."

        m "Is that so? Then it's fine."

        y "So what do you want to eat?"

        y "Just tell me. I got everything covered."

        menu:
            "What should I eat?"

            "Tonkotsu (Pork Bone) Ramen with Pork Slices and Egg.":
                m "I want the Tonkotsu Ramen."

                show yui surprised with dissolve

                y "Eh, you like Japanese dishes?"

                m "Yeah they taste good."

                y "I... I see."

            "Quarter Pound Burger with Large Fries.":
                m "I want the Quarter Pounder Burger."

                show yui surprised with dissolve

                y "Eh, you like American fast-food?"

                m "Yeah they taste good."

                y "I... I see."

            "12\" All Meat Pizza with Thin Crust.":
                m "I want the All Meat Pizza."

                show yui surprised with dissolve

                y "Eh, you like pizza huh?"

                m "Yeah they taste good."

                y "I... I see."

            "Risotto with Caesar Salad.":
                m "I want the Risotto."

                show yui surprised with dissolve

                y "Eh, you like Italian food huh?"

                m "Yeah they taste good."

                y "I... I see." 

            "All of it. All in. Just do it.":
                m "I want everything in today's menu."

                show yui surprised with dissolve
                y "Ehhh? There's no way you can finish all of it."

                m "I've done it once. With my friend of course."

                m "The moment you said \"I've got everything covered\", I already knew what to do."

                y "Hahaha~ Okay I get it!"
    
    else:
        "{i}Ding dong dang {/i}"

        scene bg cafeteria
        
        m "Dude this sucks."

        kk "What?"

        m "Why am I eating with you."

        kk "Haha~ Just like I said. Go get a girlfriend."

        m "Whatever."

        "...."

    jump socialStudiesQuiz

label socialStudiesQuiz:

    scene bg classroom
    show clarrise 
    with fade

    t "Okay Class! Listen up!"

    t "There will be a surprise quiz today."

    t "It is a 10 item quiz. Make sure to review your notes."

    t "The topic is about the Republic Act No. 11313 also known as \"Safe Spaces Act.\""

    # Implement notes

    if metYui is True:
        "No way!!! I know this law. I could ace this test."

        kk "Hey future Attorney Mark. Do you know this law?"

        m "Of course. Leave it to me."
    else:
        "No way!!! I know this law. I could ace this test."

        show kurt teeth with dissolve

        kk "Hey dude. Isn't this what you've just told me earlier in the jeep?"

        m "Yeah dude. Did you remember what I said?"

        kk "I'll try to remember it haha~"

    jump quiz

label quiz:
    $ quizPoint = 0
    $ quizNum = []
    show clarrise with dissolve
    t "First Question!"

    menu:
        show clarrise talk with dissolve
        "It is the law that recognizes that both men and women must have equality, security, and safety not only 
        in private but also on the streets, public spaces, online, workplaces and educational and training institutions."

        "Republic Act No. 11616":
            ""
        "Republic Act No. 11313":
            quizNum.append(1)
        "Republic Act No. 11717":
            ""
        "Republic Act No. 11919":
            ""
    show clarrise with dissolve
    t "Second Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""

    show clarrise with dissolve
    t "Third Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""
    show clarrise with dissolve
    t "Fourth Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""
    show clarrise with dissolve
    t "Fifth Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""
    show clarrise with dissolve
    t "Sixth Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""
    show clarrise with dissolve
    t "Seventh Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""
    show clarrise with dissolve
    t "Eight Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""
    show clarrise with dissolve
    t "Ninth Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""

    show clarrise with dissolve
    t "Last Question!"

    menu:
        show clarrise talk with dissolve
        ""
        "":
            ""
        "":
            ""
        "":
            ""
        "":
            ""

    "Class" "WAAAAAAA!"

    "Everyone is turning their heads. Asking if they did well."

    kk "What the hell. That was hard."

    m "Was it? I don't think so. Haha~"

    "Mark with a smile on his face, knew he did well."

    # Show achievement if perfect
    # Show test result



label pervTeacher:
    scene black

    centered "1 Week Later..."
    
    scene classroom with fade

    "Classroom noises...."

    show kurt neutral with dissolve

    kk "Hey Mark, did you hear the news?"

    m "What news?"

    kk "It's about [t]."

    m "What happened to [t]."

    kk "Based on what I heard, she got sick and is in the hospital."

    kk "The school faculty doesn't know when she's going back."

    m "She's in critical condition?"

    kk "I don't know dude. That's all I know."

    kk "Ohh! I almost forgot."

    kk "There will be someone substituting [t]."

    m "Who?"

    kk "They say he's a nasty person."

    m "O-ohh..."

    "Noise of footsteps towards the door."

    "???" "Hwehehehe... How you doin' everyone?"

    "Everyone in the classroom gasped."

    show teacher smile with dissolve

    "???" "I hope we all get along, everyone hehehe~"

    "???" "I will be your substitute teacher for this class."

    "???" "Call me Professor Butch."

    b "These are some nice looking girls, huh?"

    b "Hehehehe... perfect for my taste."

    "What the hell did he just say?"

    "Looking at Kurt, he is about to stand up."

    show kurt angry at left with dissolve

    kk "What did you say?!"

    m "You idiot..."

    show teacher closed with dissolve

    b "Oh did I ask you to talk? You'll be receiving a failing grade."

    b "Hehehe~"

    show kurt surprised with dissolve

    kk "Wha-?"

    "I whispered in Kurt's ears."

    m "Just let it slide dude. I will find a way to report this nasty professor."

    jump talkOnHarass


label talkOnHarass:

    scene black
    centered "A few days later..."

    if lunchWithYui is True:
        scene schoolground
        
        "What a nice landscape."

        "I see [y] walking across the ground. With a sad expression on her face."

        show yui sad with fade
        m "Hey [y]! How's your class doing?"

        m "You called me out to talk about something?"

        y "Y-yeah..."

        y "It's about that law you talked about."

        m "The Safe Spaces Act? What about it?"

        y "I have something to talk about related to it...."

        m "Tell me about it."

        "While clasping her hands firmly for a while, she finally opened her mouth."

        y "It's about my professor..."

        y "He's doing something bad... And I can't do anything to stop it."

        m "Who's this professor? Is he teaching here?"

        y "Y-yeah... I hate him. That disgusting person."

        y "When he gave a test the other day... He stares at the girls in a lascivious manner."

        y "When we are in the laboratory, he sneakily touches the butt of some of the girls."

        y "Then he says, \"It's not my fault that you are sexy.\""

        y "And then one time, he..."

        show yui crying with dissolve

        y "He suddenly touched my shoulders... and pinched it in a manner that is so disgusting. Then he whispered something to my ear."

        m "WHAT?!" with vpunch

        show yui angry with dissolve

        y "Aaaaah! I hate him. Just remembering it makes me puke."

        y "I was almost close to crying in the classroom. I was really shaking and trembling."

        y "The girls in my class can't speak up to him. Also when the boys stand up for us, he gives them a failing mark."

        m "Tell me who is this nasty person?"

        show yui sad with dissolve

        y "H-h-his name is Butch..."

        y "They said he was a new faculty teacher..."

        m "I see. So he's also teaching the First Year students. That damned bastard."

        y "M-Mark! I have a favor! Please help me out."

        m "Ahhhh..."

        $ badEndingGame = False
        $ helpedYui = False
        menu:
            "Should I help her out?"

            "Help her.":
                helpedYui = True

                m "Okay [y] I will help you."

                y "Thank you so much!"

                y "Also before I forget to say... There was someone who took a video when he was doing the crime."

                m "Really? Then this will be easy. It should be a solid evidence for his disgusting act."

                jump arrestButch

            "Don't help her.":
                badEndingGame = True

                m "I'm afraid I cannot help. I might get in trouble."

                y "Is that so? That's a real shame..."

                jump badEndStory
                
    else:
        scene schoolground
        show kurt neutral
        with fade

        kk "Dude... I have something to talk about."

        kk "It's about that law you talked about."

        m "The Safe Spaces Act? What about it?"

        kk "I think we can use this law against that professor."

        m "Tell me more about it."

        kk "Just the other day, one of our girl classmate got sexually harassed."

        m "Really? That's bad."

        kk "I've also got stories from other girls in First Year. According to them..."

        kk "When he gave a test the other day... He stares at the girls in a lascivious manner."

        kk "When they are in the laboratory, he sneakily touches the butt of some of the girls."

        kk "Then he says, \"It's not my fault that you are sexy.\""

        kk "And then one time, he... he tried to grope someone."

        m "Dude this is getting worse."

        m "We really need to do something."

        kk "Yeah I know. Here comes the good part dude."

        m "What is good in this?"

        kk "Someone took a video of that nasty bastard doing the crime."

        m "Really? That a solid evidence then!"

        kk "I know right! That disgusting creep should rot in jail forever."

        kk "Now will you help me out?"

        kk "Because of you, I learned of the Safe Spaces Act. I knew of the things which a person shouldn't ever do."

        kk "You wanted to be an Attorney right? Help me use this \"Safe Spaces Act\" to arrest that nasty piece of ****."

        menu:
            "Should I help him?"

            "Help him.":
                jump arrestButch

            "Don't help him.":
                badEndingGame = True
                jump badEndStory

label arrestButch:

    scene black
    centered "A few days later..."

    if helpedYui is True:
        scene classroom
        show teacher smile
        with fade

        b "Bring out a pen and paper. We will be having a surprise quiz."

        "Everyone" "What?!!"

        show kurt neutral

        m "Something good will happen today."

        kk "What? There's nothing good happening when there's a surprise quiz."

        m "Just wait and see dude. Haha~"

        kk "Whatever Attorney Mark."

        m "Shut up."

        scene black

        centered "A few minutes later..."

        scene hallway

        "Footsteps can be heard in the hallway."

        scene classroom

        "???" "Excuse me. Please open the door."

        show teacher closed with dissolve

        b "Who the hell is disturbing my class!!!"

        hide teacher closed

        "Continuous knocking on the door."

        "Creeeeek. The door opens."

        "Uniformed personnels came in. They appear to be police."

        show teacher closed with dissolve

        b "Why is there police here?!!"

        "Everyone" "What's happening? Why are they here? Did someone kill?"

        "Policeman Carl" "Everyone please calm down."

        "Policeman Carl" "We have received a complaint that someone is sexually harassing a student."

        "The policeman looks at Butch."

        b "What the hell are you looking at? I don't know anything about that."

        "Policeman Carl" "Don't explain to me. Everything that you say will be used against you."

        "Policeman Carl" "The complainant showed a solid proof of evidence."

        "Policeman Carl" "You will be coming with us. Do not resist."

        "Everyone" "*gasps*"

        "Officer Greg" "Hey future Attorney! It looks like it went fine."

        m "Waaah! Officer Greg you actually came."

        "Officer Greg" "It's because of you, we caught this disgusting molester. Thank you."

        m "Are you praising me? Hahaha~ No big deal. I am destined to be an Attorney anyways."

        "Officer Greg" "Hahaha! I like that attitude. Keep doing good things young man."

        m "Yes Sir!"

    # Kurt scene
    else:
        scene classroom
        show teacher smile
        with fade

        b "Bring out a pen and paper. We will be having a surprise quiz."

        "Everyone" "What?!!"

        show kurt neutral

        m "Something good will happen today."

        kk "Is it finally happening?"

        m "Yeah I was informed it would be today."

        kk "That's great. Now we just have to sit and watch. Great job Attorney Mark."

        m "Hahahaha~"

        scene black

        centered "A few minutes later..."

        scene hallway

        "Footsteps can be heard in the hallway."

        scene classroom

        "???" "Excuse me. Please open the door."

        show teacher closed with dissolve

        b "Who the hell is disturbing my class!!!"

        hide teacher closed

        "Continuous knocking on the door."

        "Creeeeek. The door opens."

        "Uniformed personnels came in. They appear to be police."

        show teacher closed with dissolve

        b "Why is there police here?!!"

        "Everyone" "What's happening? Why are they here? Did someone kill?"

        "Policeman Carl" "Everyone please calm down."

        "Policeman Carl" "We have received a complaint that someone is sexually harassing a student."

        "The policeman looks at Butch."

        b "What the hell are you looking at? I don't know anything about that."

        "Policeman Carl" "Don't explain to me. Everything that you say will be used against you."

        "Policeman Carl" "The complainant showed a solid proof of evidence."

        "Policeman Carl" "You will be coming with us. Do not resist."

        "Everyone" "*gasps*"

        "Sound of handcuffs being placed on the hands."

        "Officer Greg" "Hey future Attorney! It looks like it went fine."

        m "Waaah! Officer Greg you actually came."

        "Officer Greg" "It's because of you, we caught this disgusting molester. Thank you."

        m "Are you praising me? Hahaha~ No big deal. I am destined to be an Attorney anyways."

        "Officer Greg" "Hahaha! I like that attitude. Keep doing good things young man."

        m "Yes Sir!"

        kk "Hey! Don't forget about me!!"

        "Officer Greg" "Oh yes, the Attorney's friend. You will also receive compensation."

        kk "Nevermind compensation, why is my name \"Attorney's friend\"?!!!"

        "Everyone" "HAHAHAHA!!!"

        $ friendEnding = True
    
    jump yuiEnd


label badEndStory:

    scene black

    centered "[b] went on to harass lots of students. This went on without anyone stopping him because of his position."

    centered "When the police caught on to the news, [b] went on to hiding. Never getting caught for his crimes."

    centered "BAD END"

return
