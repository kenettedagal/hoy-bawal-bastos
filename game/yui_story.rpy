image kitchen = im.Scale("images/bg kitchen.webp", 1920, 1080)
image outside = im.Scale("images/bg outside.webp", 1920, 1080)

define kk = Character('Kurt')
define y = Character('Yui')

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

                    jump info

                    

        "I'll pretend that I didn't hear the conversation.":
            m "I should just ignore them..."

            m "I don't wanna get in trouble."

            # IMPLEMENT BAD ENDING!

            #Train end scene       
    "Officer" "Hey kids. You better get going now. I'll clean this mess up."

    m "Yes Sir."

    y "Uhmmm..."

    y "See you Mark! Thank you again..."

    m "Goodbye Yui. No worries. I just can't stand it when I see someone getting harassed."

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


return
