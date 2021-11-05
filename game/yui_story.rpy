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

    define kk = Character('Kurtney')
    define y = Character('Yui')
    define t = Character('Teacher Clarisse')
    define b = Character('Butch')
    define s = Character(None, kind=nvl)
    define mc = Character("Mark")

    default notebookOpen = False
    default points = 0
    default yuiStoryProgress = 0
    define mm = Character('Mom')
   
    hide screen displayHBBPoints
    scene school gate with fade
    centered "{outlinecolor=#00ff00}{b}{color=#000}{size=50}Story #1{/size}\n\n\n{size=80}A New School Year{/size}{/color}{/b}{/outlinecolor}" 
    #Play iphone alarm tone

    pause 2.0
    play sound "audio/iphone.ogg" 

    scene bg room morning with fade
    

    "{i}7:00 AM....{/i}"
    
    "Ugh...."

    "Shut up Siri."

    "......"
    $ timeout_label = "snooze"
    $ timeout = 10
    menu:

        "Snooze alarm for 5 minutes":
            jump snooze
            
        
        "Get up and fix the bed":
            
            play music "audio/Time for Rest.ogg" fadein 0.3 volume 0.2  
            
            scene bg room morning with dissolve

            "Another day, another dollar..."

            jump breakfastWithMom

label snooze:
    scene black

    "Just a few more minutes...."

    "Zzzzzz...."

    pause 2.0
    play sound "audio/iphone.ogg"

    scene bg room morning with dissolve

    "{i}7:27 AM....{/i}"

    play music "audio/Time for Rest.ogg" fadein 0.3 volume 0.2

    m "NO WAY!!! I ALMOST SLEPT FOR ANOTHER 30 MINUTES!"

    jump breakfastWithMom


label breakfastWithMom:

    mm "Mark! Are you awake?"

    play sound "audio/doorknock.mp3" 
    pause 1.0
    with hpunch
    
    "....."
    play sound "audio/doorknock.mp3"
    pause 1.0
    with hpunch

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
    $ timeout_label = None
    hide mom happy with dissolve
    menu: 
        
        mm "What do you wanna eat?"

        "Scrambled eggs.":
            m "Nothing beats [mm]'s scrambled eggs."

        "Tocino":
            m "The sweet taste of tocino means a very good morning."

        "Bacon":
            m "Crispy and juicy bacon. The best breakfast food invented."

        "Of course, all of it!":
            m "All of these dishes in one plate..."
            m "I hope my stomach won't hurt when I'm outside. Haha...."
            mm "I hope so too! Ahahaha~"
            
    m "Thank you for the food, Mom!"

    show mom happy at left with dissolve
    
    mm "No worries! It's gonna be a big day for you honey."

    "...."

    hide mom happy with dissolve

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

    $ yuiStoryProgress += 1

    centered "\“On the 17th of April Year 2019, a new law called {color=#f00}{b}Republic Act No. 11313{/b}{/color} 
    or also known as {color=#f00}{b}Safe Spaces Act{/b}{/color} has been approved by the President.\""

    centered "The Safe Spaces Act is an act defining gender-based sexual harassment 
    in streets, public spaces, online, workplaces, and educational or training institutions."  

    centered "This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions."

    scene kitchen with fade

    "I should probably take some notes of this law..."

    show screen newNote with fade

    pause 1.5

    show natasha talk with dissolve

    

    n "Hey its me again~"

    show screen showNotesButton with dissolve

    n "If you look at the top left part of the screen, there is a button."

    n "This button will log important parts of the law. So always check it out~"

    n "Bye now!"

label goingToSchool:

    scene outside with fade
    "Well, that was a great law. Hopefully I can teach someone about it."

    "Hmmm. As expected, there will be a class introduction soon. How should I introduce myself?"

    "Ehem....."

    "\"How y'all doin' everyone! The greatest future attorney is in this class. The name's Mark!\""

    "How's that? Hmmm..."

    "No... that's... way too embarassing."

    "How about..."

    "\"Pleased to meet you everyone. Please call me Mark.\""

    "...."

    "Yeah that'll work. Short and simple."
    
    "They don't need to know that I am dreaming to be an attorney someday."

    "{i}8:15 AM...{/i}"

    "Oh!!! I didn't notice the time at all."

    "Should I take a jeep or train today?"
    $ timeout = 8
    $ timeout_label = "meetWithKurt"
    menu:
        # Story will diverge from this point. Will converge at some point.
        "Should I take a jeep or train today?"
        
        # Meet Yui
        "Take the train.":
            $ metYui = True
            jump meetWithYui

        # Meet Kurt(friend)
        "Ride a jeep.":
            jump meetWithKurt


label meetWithKurt:
    $ metYui = False
    scene bg jeep n with fade
    
    "Mark!"

    "Mark!!!"

    "Uhmm someone is calling me?"

    "From where?"

    "???" "Dude! Are you deaf?"

    "Bam!!" with vpunch

    "Ouch that hurts..."

    m "Oh.. it is you [kk]!"

    show kurtney happy teeth with dissolve

    m "Why'd you hit me in the back of my head?"

    show kurtney angry talk with dissolve

    kk "Dude you almost rode the jeep without me."

    m "Sorry I didn't notice you at all."

    show kurtney smile with dissolve

    kk "Well its fine. Atleast I'm going to school with you."

    "This is [kk]. My weird childhood friend."

    "We have been friends since elementary school. She is a little boyish and sometimes annoying."

    "But I don't hate it at all."

    show kurtney talk opened with dissolve

    kk "Did you know? Something crazy happened to me today. Good thing I found you."

    m "What happened?"

    kk "There was this guy... standing at the corner of our street."

    kk "He looked unfamiliar to me so I asked him if he was looking for someone or he got lost."

    m "So? Was he lost or what?"

    show kurtney angry talk with dissolve

    kk "Crazy freaking dude told me, \"You look beautiful today as well.\""

    m "That's sexual harassment..."

    m "What does he look like?"

    kk "He wears a hoodie and a sweat pants."

    m "Let me know when you see this guy again."

    show kurtney happy teeth with dissolve

    kk "Thanks dude! I'm lucky I have someone like you."

    kk "Ohhhh and speaking of you..."

    kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"

    m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

    show kurtney happy teeth with dissolve

    kk "You poor little thing. Don't worry, I'll always be here for you so you don't look like a loser."

    m "Well, don't even talk like you have one."

    kk "Hahaha~ Don't worry about me. I'm more worried about your future."

    m "I'm not a child for you to worry about."

    kk "Haha!!"

    m "Hey, do you wanna hear something interesting?"

    m "It is related to what happened to you earlier."

    show kurtney talk opened with dissolve

    kk "What? If it's boring then I'm not listening to you."

    #show kurt without headphone

    m "I saw the news this morning. There was a new law.."

    kk "What kind of law?"

    hide kurtney talk opened with dissolve

    $ firstTryWrong = False
    $ timeout = 15
    $ timeout_label = "kurtFirstQuestionTimerOut"

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
            jump kurtIntroSecond

        "Rebuild Act No. 11313":
            "Not the right answer."
            $ firstTryWrong = True
            jump kurtFirstQuestion

    label kurtFirstQuestionTimerOut:
        $ firstTryWrong = True
        m "Republic Act No. 11313"

    #######################################

    label kurtIntroSecond:
        show kurtney happy teeth with dissolve
        kk "That's cool. Tell me more about it."

        m "Yeah its a great law."

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
                $ points += 3
                "You received {color=#40ff00}3 HBB Points.{/color}"
            jump kurtIntroThird
            
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

    label kurtSecondQuestionTimerOut:
        $ firstTryWrong = True
        m "Safe Spaces Act"

    label kurtIntroThird:

        show kurtney talk opened with dissolve
        kk "So it is called \"Safe Spaces Act\"?"

        m "Yeah! It's a cool name right."

        #show kurt open mouth
        kk "Sure. But what does it mean?"

        $ firstTryWrong = False
        $ timeout = 10
        $ timeout_label = "kurtInfo"

        hide kurtney talk opened with dissolve 

    menu kurtThirdQuestion:
        "Wait, what does the Safe Spaces Act mean again?"

        "To protect Earth from aliens.":        

            m "To protect Earth from aliens."

            show kurtney angry talk with dissolve

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
                $ yuiStoryProgress += 1

                show kurtney smile with dissolve

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

                show screen newNote with fade
                pause 1.0

                show kurtney talk opened with dissolve

                kk "That was a lot! How'd you memorize it?"

                m "Well you know... I wanted to be an attorney. So this much is not that big deal."

                show kurtney happy teeth with dissolve

                kk "Attorney Mark? Sounds nice haha~"

                m "Stop mocking me dude."

                show kurtney talk opened with dissolve

                kk "So what happens when I do any of those things?"

                m "Let's continue later dude. We are close to the school."

                show kurtney smile with dissolve

                kk "Tell me about it okay? It's an interesting law."

                

        "To protect public and online spaces from danger.":

            m "To protect public and online spaces from danger."

            show kurtney angry talk with dissolve

            kk "What danger? Explain it clearly."

            m "Uhhhh.. wait let me remember..."

            m "Errr... it is to..."

            jump kurtInfo

        ########################################

    scene walk with fade

    "A peaceful morning for a first day of school."

    "Or so I thought..."

    show kurtney happy teeth with dissolve

    kk "Hahaha~ I miss summer vacation."

    m "Oh shut up. All you do is play games and watch anime."

    kk "Are you talking about yourself? Ahahaha~"

    m "Whatever."

    scene walk with fade

    "While peacefully chatting ang walking to school, [kk] saw something she doesn't want to see."

    show kurtney talk opened with dissolve

    kk "Hey, Mark..."

    m "Hmmm?"

    kk "Look behind our back..."

    m "Back?"

    m "What the hell? Is that the stalker guy from what you've said earlier?"

    show kurtney smile with dissolve

    kk "Watch your mouth. He might hear you and do something bad."

    m "And now you're concerned for me?"

    m "I should be the one worrying for you."

    show kurtney blush close with dissolve

    kk "Of course, you're my precious childhood friend."

    m "Hahaha~ whatever. I got this."

    scene walk with fade

    menu:
        "What should I do?"

        "Run straight to the school gate.":
            m "[kk]..."

            show kurtney talk opened with dissolve

            kk "Yeah?"

            m "Hold my hand."

            show kurtney blush small with dissolve

            kk "Wha? Are you st-stupid?"

            m "Do it!"

            show kurtney blush close with dissolve

            kk "O-o-okayyy...."

            scene school gate with fade

            "With all my might and strength reserved for this day, I grabbed [kk]'s hand and ran like a mad dog."

            "Looking at my back, the guy is nowhere to be seen."

            m "Pant pant pant..."

            show kurtney blush close with dissolve

            kk "Hey tell me what're you trying to do before doing that..."

            kk "Stupid..."

            m "Hahaha~ I just want to get away though. Why did you suddenly become red?"


            
        "Pick a fight with the stalker.":

            m "Hey, what do you want?"

            "???" "Hmmm.. Are you her boyfriend?"

            m "No! She's my childhood friend."

            "???" "Then take this."

            "BAM!" with vpunch

            "AAHHH!" with hpunch

            "PAAAK!" with vpunch

            m "AAAAAAH!!!"

            scene black with fade
            pause 1.0
            scene walk with fade

            show kurtney worry with dissolve

            kk "Heyyyyyyy..."

            kk "Wake up Mark..."

            m "What the heck happened?"

            show kurtney happy teeth with dissolve

            kk "Well, he knocked the soul out of you. Hahaha~"

            m "This is no laughing matter. What happened to him?"

            show kurtney smile with dissolve

            kk "He ran away when a lot of people were looking at us."

            m "O-ohhh I see... Ughhhh my head hurts."

            "Achievement Unlocked: Punched in the Face"

        "Confront the stalker and tell him that you'll report him to the police.":
                $ points += 3
                "You received {color=#40ff00}3 HBB Points.{/color}"

                scene walk with fade 

                m "Excuse me. Stop whatever you're doing. You're disrupting our lives."

                "???" "Who the hell are you?"

                m "I am her friend. I will report you to the police this instant!"

                "???" "Calm down. I'll leave now. Enjoy your day."

                scene walk with fade

                "After a few minutes, the stalker was out of sight."

                m "Sighhhh. Hopefully this doesn't happen to you again."

                show kurtney worry with dissolve

                kk "I hope so. You'll be there to protect me right?"

                m "Nope. Not me. But the police. Haha~"

                show kurtney angry talk with dissolve

                kk "Wha?! Stupid."

                hide kurtney angry talk with dissolve

    
label kurtneyOfficerScene:

    show officer with fade  

    "???" "Excuse me!"

    kk "Ehhh? A police officer?"

    m "Oh great. This makes things easy."

    "The police officer was running towards us with a confused look on his face."

    "Officer" "Excuse me young ones... I just saw what happened earlier. Can you tell me more about the event?"

    m "Uhmmmm my friend here was getting stalked by someone..."

    "Officer" "A stalker huh?"

    "Officer" "Did you know that stalking is a grave crime? According to the Safe Spaces Act that is."

    m "Yes sir, I've read a bit about that law."

    hide officer
    show kurtney talk opened 
    with dissolve

    kk "Hey Mark. It was that law that you told me earlier right?"

    m "Yeah it is."

    hide kurtney talk opened
    show officer
    with dissolve

    "Officer" "Stalking is a serious crime. Do you guys want to learn about the punishment for violating the Safe Spaces Act?"

    $ yuiStoryProgress += 1

    hide officer with dissolve

    menu :
        
        "Officer" "Do you want to learn more about the punishments of Safe Spaces Act?"

        "Yes, please tell me about the punishments.":
            hide officer with dissolve
            $ points += 3
            "You received {color=#40ff00}3 HBB Points.{/color}"
            
            show kurtney happy teeth with dissolve

            kk "!!!!"

            kk "I-I-I want to learn it too..."

            hide kurtney happy teeth
            show officer
            with dissolve
            "Officer" "Sure thing. Lemme just take out my handbook."

            pause 2.0

            "Officer" "Uhhh it says here..."

            "Officer" "On Section 12 of the Safe Spaces Act, 
            it states the {color=#ff3d3d}Specific Acts and Penalties{/color} for Gender-Based Sexual Harassment in Streets and Public Spaces."

            "Officer" "This is quite long so listen carefully okay?"

            with fade

            
            s "a) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs, persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination, the use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs, the persistent telling of sexual jokes, use of sexual names, comments and demands, and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety." 

            nvl clear
            
            s "{color=#ff3d3d}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            s "{color=#ff3d3d}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)"

            s "{color=#ff3d3d}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)"

            nvl clear

            s "b) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening or intimidating the offended party including flashing of private parts, public masturbation, groping, and similar lewd sexual actions."

            nvl clear 

            s "{color=#ff3d3d}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            s "{color=#ff3d3d}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)"

            s "{color=#ff3d3d}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)"

            nvl clear

            s "c) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person; or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b)."

            nvl clear

            s "{color=#ff3d3d}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP."

            s "{color=#ff3d3d}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)"
            
            s "{color=#ff3d3d}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)"

            nvl hide

            hide officer

            with fade

            m "......"

            m "My head hurts... Ahahaha!"

            show kurtney talk opened with dissolve

            y "Wait, that's a really good law, Officer!"
            
            hide kurtney talk closed

        "No, I don't really care.":
            $ points -= 3

    show screen newNote with fade
    pause 2.0

    

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

    scene bg train morning with fade

    "{i}Footsteps of people{/i}"

    "Moving closer towards the exit... I hear some conversation."

    "???" "Hey there sexy little miss. Are you free tonight and have a drink." 

    "???" "Don't worry, we won't do anything do bad to you hehehe..."

    "???" "Do you need money or anything? Just tell us."

    "I can see three old men sexually harassing a young student girl."

    "I notice that the girl is trembling and shaking."

    show yui worry with dissolve

    "Girl" "Plea-please l-l-leave me alo-lone..." 

    "???" "Hahaha!! She's scared like a child."

    "???" "Hey, you're teasing her too much. She might report us."

    "???" "Boss, don't worry. She can't even say the sentence straight."

    show yui worry closed with dissolve
    pause 3

    hide yui worry closed with dissolve 
    $ timeout = 10
    $ timeout_label = "notSaveYui"
    $ deathFlag = False
    $ metYui = True
    menu trainScene:
        "What should I do?"


        "I'll pick a fight with them." if deathFlag is False:
            $ deathFlag = True

            m "Hey you bastards! Stop sexually harrassing that girl."

            "???" "Who the hell are you? His boyfriend perhaps?"

            "???" "You little punk talking to me like that. I'll crush you."

            "???" "Take this you pesky little boy."

            show yui worry with dissolve

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
            hide yui worry closed
            m "Officer! Officer!!"

            m "I saw three old men catcalling and sexually harassing a girl student! Please help me."

            show officer with dissolve

            "Officer" "I see. Bring me to them."

            label withOfficer:
                m "Officer! Here!"

                m "These old men are catcalling and making unwanted invitations to this girl."

                "???" "What the hell. Run guys!!"

                "???" "Holy crap don't leave me."

                "???" "Dammnit!"

            #show Yui

            hide officer
            show yui wow with fade
            "Girl" "Uwaaaaah! Thank y-y-you sooo much!!"

            m "Ohhh... I didn't really do anything..."

            show yui smile close with dissolve

            "Girl" "You saved my life...."

            m "Life?"

            show yui smile opened with dissolve

            "Girl" "Uhmm..."

            "Girl" "Can you tell me your name?"

            m "Ohhh. My name is Mark. How about you?"

            show yui blush with dissolve

            "Girl" "Y-Y-Yu.."

            m "Yu?"

            show yui surprised blush with dissolve

            "She's gotten a bit red of a sudden..."

            show yui blush closed with dissolve

            "Girl" "Ple-please call me Yui."

            m "[y], huh? What a cute name."

            show yui surprised blush with dissolve

            y "EHHH?!! Cute?"

            show yui blush closed with dissolve

            y "{i}......waaah!{/i}"

            m "Hey, [y]. I saw you earlier that you were shaking and trembling."

            show yui worry with dissolve

            y "Yeah that was embarassing to see...."

            show yui worry closed with dissolve

            y "You see, when I was a child... I had a trauma."

            m "A trauma? Can I hear more of this?"

            y "Uhmmm y-yes..."

            show yui worry opened with dissolve

            y "When I was in 4th Grade, my boy classmates would make fun of my appearance."

            y "It made me stop going to school... And I was homeschooled since then."

            m "I can't imagine how you must feel. My heart hurts for you."

            show yui worry closed with dissolve

            m "You know what? I have something interesting to tell you!"

            show yui wow with dissolve

            y "What is it?"

            m "It's about a law."

            y "A law? What kind of law?"

            m "It is something related to what you experienced earlier."
            $ timeout = 15
            $ timeout_label = "yuiFirstQuestionTimerOut"
            $ yuiFirstAnswer = True
            hide yui wow with dissolve
            menu yuiFirstQuestion:
                "Aaaaah... What is it again? The law that was approved on 17th of April, 2019?"

                "Re-semiprivate Act No. 11313":
                    m "Re-semiprivate Act No. 11313"

                    "Wrong answer!"
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

                "Reprivate Act No. 11313":
                    m "Reprivate Act No. 11313"
                    "Not this... Think again..."
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

                "Republic Act No. 11313":
                    m "Republic Act No. 11313"
                    "Great answer!"

                    if yuiFirstAnswer:

                        $ points += 3
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                    jump yuiIntroSecond
                    

                "Rebuild Act No. 11313":
                    m "Rebuild Act No. 11313"
                    "Not the right answer."
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

            #######################################

            label yuiFirstQuestionTimerOut:
                m "Correct Answer: Republic Act No. 11313"

            label yuiIntroSecond:

            m "The law is Republic Act No. 11313."

            show yui wow with dissolve

            y "What is that law?"

            m "This law is..."
            $ timeout_label = "yuiSecondQuestionTimerOut"
            $ yuiSecondAnswer = True
            hide yui wow with dissolve
            menu yuiSecondQuestion:
                "It is also known as ...."
                
                "Safe Spaces Act":
                    m "Safe Spaces Act"
                    "Correct!!"

                    if yuiSecondAnswer:

                        $ points += 3
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                    jump yuiThirdIntro
                    
                "Safe Pace Act":
                    m "Safe Pace Act"
                    "Wait this is wrong."
                    $ yuiSecondAnswer = False
                    jump yuiSecondQuestion
                
                "Safe Guardian Act":
                    m "Safe Guardian Act"
                    "Not the right answer."
                    $ yuiSecondAnswer = False
                    jump yuiSecondQuestion
            
                "Safe Insurrance Act":
                    m "Safe Guardian Act"
                    "Not the greatest answer."
                    $ yuiSecondAnswer = False      
                    jump yuiSecondQuestion

            label yuiSecondQuestionTimerOut:
                m "Safe Spaces Act"
            
            label yuiThirdIntro:

                show yui wow with dissolve

                y "So it is called \"Safe Spaces Act\"?"

                m "Yeah! It's a cool name right?"

                #show kurt open mouth
                y "Uhm. But what does it mean?"

                $ yuiThirdAnswer = True
                $ timeout_label = "yuiInfo"

                hide yui wow with dissolve

            menu yuiThirdQuestion:
                "Wait, what does the Safe Spaces Act mean again?"

                "To protect Earth from aliens.":
                    show yui smile close with dissolve

                    y "Wait that's really funny~"

                    y "Please tell it to me seriously..."
                    
                    m "Hahaha~ I'm just kidding!"

                    m "The law was created to..."
                    $ yuiThirdAnswer = False
                    jump yuiThirdQuestion

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
                "To protect men and women from gender-based sexual harassment.":
                    "Nice job! Correct answer."
                    if yuiThirdAnswer:
                        $ points += 3
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                    
                    show yui neutral with dissolve
                    label yuiInfo:
                        $ yuiStoryProgress += 1
                        

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

                        show screen newNote with fade
                        pause 1.0

                        show yui wow with dissolve

                        y "That was a lot! How'd you memorize it?"

                        m "Well you know... I wanted to be an attorney. So this much is not that big deal."

                        show yui smile opened with dissolve

                        y "You wanted to be an attorney? That sounds really nice~"

                        m "Thank you ehehe..."

                        jump yuiConflictResolved


                "To protect public and online spaces from danger.":
                    y "What danger? Please explain it clearly."

                    m "Uhhhh.. wait let me remember..."

                    m "Errr... it is to..."

                    $ yuiThirdAnswer = False

                    jump yuiThirdQuestion

                    

        "I'll pretend that I didn't hear the conversation.":
            jump notSaveYui
            

            
    label notSaveYui:
        "I'll pretend that I didn't hear the conversation."

        "I should just ignore them..."

        "I don't wanna get in trouble."

        jump yui_end

        # IMPLEMENT BAD ENDING!

    
    label yuiConflictResolved:
        hide yui smile opened
        show officer with fade       
        "Officer" "Hey kids. You better get going now. I'll clean this mess up."

        "Officer" "Based on the Implementing Rules and Regulation of Republic Act No. 11313..."

        "Officer" "Those guys broke the law by (1) Catcalling and making unwanted invitations."

        "Officer" "(2) Making statements of sexual comments and suggestions."

        "Officer" "(3) Making advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety." 

        "Officer" "This may include cursing, leering and intrusive gazing, and taunting."

        m "WOW! That's a really great law."

        "Officer" "I know kid."

        "Officer" "Do you want to learn more about the punishments of Safe Spaces Act?"

        $ yuiStoryProgress += 1

        $ timeout = 10
        $ timeout_label = "ignorePunishment"

        hide officer with dissolve

    menu punishments:
        
        "Officer" "Do you want to learn more about the punishments of Safe Spaces Act?"

        "Yes, please tell me about the punishments.":
            hide officer with dissolve
            $ points += 3
            "You received {color=#40ff00}3 HBB Points.{/color}"
            
            show yui smile close with dissolve

            y "!!!!"

            y "I-I-I want to learn it too..."

            hide yui smile close
            show officer
            with dissolve
            "Officer" "Sure thing. Lemme just take out my handbook."

            pause 2.0

            "Officer" "Uhhh it says here..."

            "Officer" "On Section 12 of the Safe Spaces Act, 
            it states the {color=#ff3d3d}Specific Acts and Penalties{/color} for Gender-Based Sexual Harassment in Streets and Public Spaces."

            "Officer" "This is quite long so listen carefully okay?"

            with fade
            
            s "a) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs, persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination, the use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs, the persistent telling of sexual jokes, use of sexual names, comments and demands, and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety." 

            nvl clear
            
            s "{color=#ff3d3d}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            s "{color=#ff3d3d}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)"

            s "{color=#ff3d3d}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)"

            nvl clear

            s "b) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening or intimidating the offended party including flashing of private parts, public masturbation, groping, and similar lewd sexual actions."

            nvl clear 

            s "{color=#ff3d3d}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            s "{color=#ff3d3d}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)"

            s "{color=#ff3d3d}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)"

            nvl clear

            s "c) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person; or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b)."

            nvl clear

            s "{color=#ff3d3d}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP."

            s "{color=#ff3d3d}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)"
            
            s "{color=#ff3d3d}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)"

            nvl hide

            hide officer

            with fade

            m "......"

            m "My head hurts... Ahahaha!"

            show yui wow with dissolve

            y "Wait, that's a really good law, Officer!"

            scene bg train morning with fade

            jump trainEndScene
            

        "No, I don't really care.":
            $ points -= 3
    
    label ignorePunishment:

        m "No, I don't really care."

        show officer with dissolve

        "Officer" "Ohhhh that's a shame."

        $ points -= 3
        "Your {color=#ff3d3d}HBB Points{/color} have been deducted by 3!"
    
    label trainEndScene:


        show screen newNote 
        pause 2.0

        show officer

        "Officer" "Now go on your way. I'll take care of them. In jail of course."
        
        m "Sir, can I ask for your name?"

        "Officer" "Oh it's Greg. Find me whenever you are troubled."

        m "Thank you very much sir!"

        hide officer with fade

        show yui worry opened with dissolve

        y "Uhmmm..."

        y "See you Mark! Thank you again..."

        m "Bye Yui. No worries. I just can't stand it when I see someone getting harassed."

        show yui blush with dissolve

        y "Uhhhm.. I hope I can see you aga-"

        with fade

        #Train sound
        "{i}A train passed by.{/i}"

        m "What?"

        show yui surprised blush with dissolve

        y "No, nothing!!! Goodbye!"

        scene black with fade

        jump schoolCeremony

label schoolCeremony:

    scene aerial with fade
    "B Highschool. A prestigious school where only the best can enter."

    scene school building with fade

    "I'm so lucky to be here."

    "...."

    scene audi1 with fade

    "Student Council President" "To all the newcomer students, I welcome you!"

    "Student Council President" "I hope that you can achieve your dreams in this school."

    scene audi2 with dissolve

    "Student Council President" "To all those that are nearing graduation, I hope you achieved what you wanted here."

    scene audi3 with dissolve

    "Student Council President" "That is all for my speech. Thank you!"

    "{i}Students clapping{/i}"

    show kurtney happy teeth with dissolve
    

    if metYui is True:
        kk "Dude! I hope we are classmates in this new school year."

        m "Oh please no."

        show kurtney angry talk with dissolve

        kk "Why? I'm fun to hang out with right?"

        m "Yeah yeah whatever you say."

        "This is [kk]. My weird childhood friend."

        "We have been friends since elementary school. She is a little boyish and sometimes annoying."

        "But I don't hate it at all."

        show kurtney happy teeth with dissolve

        kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"

        m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

        show kurtney smile with dissolve

        kk "You poor little thing. Don't worry, I'll always be here for you so you don't look like a loser."

        m "Well, don't even talk like you have one."

        show kurtney happy teeth with dissolve

        kk "Hahaha~ Don't worry about me. I'm more worried about your future."

        m "I'm not a child for you to worry about."

        kk "Haha!!"

    else:
        kk "Dude! I hope we are classmates in this new school year."

        m "Oh please no."

        show kurtney angry talk

        kk "Why? I'm fun to hang out with right?"

        m "Yeah yeah whatever you say."

    jump afterCeremony

label afterCeremony:

    scene audi4 

    show kurtney smile
    with fade
    kk "Lemme check the school bulletin to know our section."

    m "Sure dude. Gonna go to the bathroom first."

    kk "Meet me near the school bulletin okay?"
    
    m "Yeah just go."

    scene football with fade

    "A new school year..."

    "I hope it is fun..."

    scene pools with fade

    "Last year, I was a loner in my class."

    "But thankfully, I have [kk]. She's a really good childhood friend."

    #Flag to check if USER accepts lunch invite
    $ lunchWithYui = True

    scene hallway with fade

    if metYui is True:

        "???" "Hey..."

        "???" "M-M-Mark!"

        show yui blush closed with dissolve

        m "Ehhhhh!!!?"

        m "Yui?! You go to my school?"

        show yui blush with dissolve

        y "Y-Yeah! Did you not no-notice my uniform?"

        m "I did not notice it at all. Oh my!"

        m "So you are a First Year student."

        m "Why didn't you tell me?"

        m "No.. sorry. It's my fault."

        show yui smile close with dissolve

        y "No... it's fine! I forgot to tell you we go to the same school."

        show yui worry opened with dissolve

        y "Uhm... M-M-Mark?"

        m "Yeah?"

        y "Can you help me get to my classroom?"

        m "Are you perhaps lost?"

        show yui smile close with dissolve

        y "Yeah... this school is really big."

        m "No wonders. It's just like me when I was a First Year student."

        m "You are currently in the Second Year's building."

        scene hallway with fade

        # This choice will determine who will eat lunch with MC
        $ timeout_label = "leaveYui"
        menu findRoomWithYui:
    
            "Go and find the classroom with Yui.":

                scene school building with fade
                m "Haaa.."

                show yui blush closed with dissolve

                y "Waaaah.. I'm so sweaty."

                m "Yeah it's kinda far from our building. Hahaha~"

                m "Just go inside there. All First Year classes are in this building."

                show yui blush with dissolve

                "{i}8:50 AM...{/i}"

                m "The first bell is gonna ring now."

                m "I'm going back now [y]!"

                m "Have fun in there!"

                show yui blush closed with dissolve

                y "W-w-waaaait Mark!"

                y "Uhm...."

                show yui blush with dissolve

                y "If it's fine with you.."

                y "Can I treat you later in lunch? As a thanks for helping me..."

                $ timeout_label = "notLunch"

                menu:
                    "Ehhhh? I've never been invited by a girl to lunch. What should I do?"

                    "Sure I'll go eat with you.":
                        m "Sure I'll go eat with you."

                        show yui wow with dissolve

                        y "For real? Waaaah!"

                        show yui smile close with dissolve

                        m "Wait why are you so happy?"

                        m "Ready your money though. I'm a big eater."

                        y "Ehehe.. sure! You can choose whatever you want."

                        play sound "audio/bell.mp3" 

                        "{i}♫ Kin kon kan kon ♫{/i}"

                        show yui worry with dissolve

                        pause 2.0

                        m "Oh crap that's the bell!"

                        m "I'll be going now [y]!"

                        show yui smile opened with dissolve

                        y "See you later.... M-Mark."

                        jump lunch

                    "Sorry, maybe next time?":

                        label notLunch:
                            m "Sorry, maybe in another day."

                            show yui worry with dissolve

                            y "Oh.... that's... a shame."

                            show yui worry closed with dissolve

                            y "I... I see..."

                            show yui smile close with dissolve

                            y "See you..."

                            scene school building with fade

                            "She left running while her hands is in her eyes."

                            "...."

                            jump lunch

            "Go to [kk] in the school bulletin and leave Yui":

                label leaveYui:
                    $ lunchWithYui = False
                    m "I'm sorry [y]. I can't help you. I have somewhere to go with my friend."

                    show yui worry with dissolve

                    y "Ah.... Is that so?"

                    show yui worry closed with dissolve

                    y "That's a real shame."

                    show yui smile close with dissolve

                    y "I'll be going now Mark."

                    scene hallway with fade

                    "She left running with a troubled expression on her face."

                    "...."

                    jump lunch
    else:

        "???" "Uhmmm..."

        "???" "Excu-cuse m-m-me....!"

        "Looking at my back, there is someone pull my sleeves..."

        show yui smile close with fade

        m "Uhhhh.. Hello?"

        m "You are?"

        "Girl" "Can you help me get to my classroom?"

        m "Are you perhaps lost?"

        show yui worry opened with dissolve

        "Girl" "Yeah... this school is really big."

        m "No wonders. It's just like me when I was a First Year student. Haha~"

        m "You are currently in the Second Year's building."

        show yui neutral with dissolve

        "Girl" "Uhmm..."

        "Girl" "Can you tell me your name?"

        m "Ohhh. My name is Mark. How about you?"

        show yui blush with dissolve

        "Girl" "Y-Y-Yu.."

        m "Yu?"

        show yui surprised blush with dissolve

        "She's gotten a bit red of a sudden..."

        show yui blush closed with dissolve

        "Girl" "Ple-please call me Yui."

        m "[y], huh? What a cute name."

        show yui surprised blush with dissolve

        y "EHHH?!! Cute?"

        show yui blush closed with dissolve

        y "{i}......waaah!{/i}"

        # ADD MORE

        scene hallway with dissolve

        jump findRoomWithYui

label lunch:

    if lunchWithYui is True:

        scene black with fade

        pause 2.0

        scene classroom lunch1 with fade

        t "To get the answer of this equation..."

        t "You must first..."

        play sound "audio/bell.mp3" 

        "{i}♫ Kin kon kan kon ♫{/i}"

        show clarrise talk with dissolve

        t "Okay Class! You may now take your lunch."

        t "We will have a quiz after your lunch."

        "Everyone" "WHAT?!!"

        pause 1.0

        scene classroom lunch1
        show kurtney talk opened 
        with fade

        kk "Hey dude wanna go to cafeteria?"

        m "Sorry dude. I'm meeting someone today."

        show kurtney happy teeth with dissolve

        kk "Meeting someone? Hey hey hey what's happening to Mr. Mark, huh?"

        m "I'm going ahead. Eat with yourself."

        show kurtney angry talk with dissolve

        kk "Wah! This little punk."

        scene black with fade
        
        pause 1.0

        scene bg cafeteria with fade

        show yui smile close with dissolve

        y "Hey Mark! Here!"

        m "Sorry [y]. Did you wait?"

        show yui neutral with dissolve

        y "No... I just got here..."

        m "Is that so? Then it's fine."

        show yui smile opened with dissolve

        y "So what do you want to eat?"

        y "Just tell me. I got everything covered."

        scene bg cafeteria with fade

        $ timeout_label = None
        menu:
            "What should I eat?"

            "Tonkotsu(Pork) Ramen. {image=ramen.png}":
                m "I want the Tonkotsu Ramen."

                show yui wow with dissolve

                y "Eh, you like Japanese dishes?"

                m "Yeah they taste good."

                y "I... I see."

            "Quarter Pound Burger with Large Fries. {image=burger.jpg}":
                m "I want the Quarter Pounder Burger."

                show yui wow with dissolve

                y "Eh, you like American fast-food?"

                m "Yeah they taste good."

                y "I... I see."

            "12\" All Meat Pizza with Thin Crust. {image=pizza.jpg}":
                m "I want the All Meat Pizza."

                show yui wow with dissolve

                y "Eh, you like pizza huh?"

                m "Yeah they taste good."

                y "I... I see."

            "Apple Risotto. {image=risotto.jpg}":
                m "I want the Risotto."

                show yui wow with dissolve

                y "Eh, you like Italian food huh?"

                m "Yeah they taste good."

                y "I... I see." 

            "All of it. All in. Just do it.":
                m "I want everything in today's menu."

                show yui wow with dissolve
                y "Ehhh? There's no way you can finish all of it."

                m "I've done it once. With my friend of course."

                m "The moment you said \"I've got everything covered\", I already knew what to do."

                show yui smile close with dissolve

                y "Hahaha~ Okay I get it!"
    
    else:
        scene black with fade

        pause 2.0

        scene classroom lunch1 with fade

        t "To get the answer of this equation..."

        t "You must first..."

        play sound "audio/bell.mp3" 

        "{i}♫ Kin kon kan kon ♫{/i}"

        show clarrise talk with dissolve

        t "Okay Class! You may now take your lunch."

        t "We will have a quiz after your lunch."

        "Everyone" "WHAT?!!"

        pause 1.0

        scene classroom lunch1
        show kurtney talk opened 
        with fade

        kk "Hey dude wanna go to cafeteria?"

        m "Yeah sure. Are you going to treat me?"

        show kurtney happy teeth with dissolve

        kk "Keep on dreaming. Maybe I'll treat you when you get a girlfriend~"

        scene bg cafeteria with fade
        
        m "Dude this sucks."

        show kurtney talk opened with dissolve

        kk "What?"

        m "Why am I eating with you."

        show kurtney happy teeth with dissolve

        kk "Haha~ Just like I said. Go get a girlfriend."

        kk "And while you still don't have one, I'll eat with you so don't look like a loser!"

        m "Whatever, keep eating."

        "...."
        scene black with fade
        pause 2.0

    jump socialStudiesQuiz

label socialStudiesQuiz:

    scene classroom morning
    show clarrise talk 
    with fade

    t "Okay Class! Listen up!"

    t "There will be a surprise quiz today."

    show clarrise talk close with dissolve

    t "It is a 10 item quiz. Make sure to review your notes."

    t "The topic is about the Republic Act No. 11313 also known as \"Safe Spaces Act.\""

    scene classroom morning with fade

    # Implement notes

    if metYui is True:
        "No way!!! I know this law. I could ace this test."

        show kurtney talk opened with dissolve

        kk "Hey future Attorney Mark. Do you know this law?"

        m "Of course. Leave it to me."
    else:
        "No way!!! I know this law. I could ace this test."

        show kurtney talk opened with dissolve

        kk "Hey dude. Isn't this what you've just told me earlier in the jeep?"

        m "Yeah dude. Did you remember what I said?"

        show kurtney happy teeth with dissolve

        kk "I'll try to remember it haha~"

    jump quiz

label quiz:
    $ quizPoints = 0
    $ quizNum = []
    scene classroom morning 
    show clarrise talk
    with fade
    hide screen showNotesButton
    t "Okay Class! Ready or not, here I go!"
    show clarrise talk close with dissolve
    t "First Question!"
    hide clarrise talk close with dissolve
    $ timeout = 20
    $ timeout_label = "one"
    menu:
        
        "It is the law that recognizes that both men and women must have equality, security, and safety not only 
        in private but also on the streets, public spaces, online, workplaces and educational and training institutions."

        "Republic Act No. 11616":
            ""
        "Republic Act No. 11313":
            $ quizNum.append(1)
            m "Alright! That was an easy one."
        "Republic Act No. 11717":
            ""
        "Republic Act No. 11919":
            ""
    label one:
    $ timeout_label = "two"
    show clarrise talk with dissolve
    t "Second Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    menu:
        
        "Republic Act No. 11313 is commonly known as \"S____ S______ A__\""

        "Save Spaceship Act":
            ""
        "Safe Spaces Act":
            m "Okay got that one in the bag!"
            $ quizNum.append(1)
        "Sale Summer Act":
            ""
        "Super Smash Act":
            ""
    label two:
    $ timeout = 10
    show clarrise talk with dissolve
    t "Third Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "three"
    menu:
        
        "Catcalling is a gender-based sexual harassment covered in Safe Spaces Act."
        "True":
            m "That is a freebie."
            $ quizNum.append(1)
        "False":
            ""
    label three:
    show clarrise talk with dissolve
    t "Fourth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "four"
    menu:
        
        "Making unwanted invitations is a gender-based sexual harassment covered in Safe Spaces Act."
        "True":
            m "Easy."
            $ quizNum.append(1)
        "False":
            ""
    label four:
    show clarrise talk with dissolve
    t "Fifth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "five"
    menu:
        
        "Stalking is included as a gender-based sexual harassment in Safe Spaces Act."
        "True":
            m "Okay doing good!"
            $ quizNum.append(1)
        "False":
            ""
    label five:
    show clarrise talk with dissolve
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
            m "Nice going!"
            $ quizNum.append(1)
    label six:
    show clarrise talk with dissolve
    t "Seventh Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "seven"
    menu:
        
        "Gender-based sexual harassment can also be commited in Public Utility Vehicles(PUV)."
        "True":
            m "That wasn't hard."
            $ quizNum.append(1)
        "False":
            ""
    label seven:    
    show clarrise talk with dissolve
    t "Eight Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "eight"
    menu:
        
        "Gender-based sexual harassment can also be commited in Streets and Public Spaces."
        "True":
            m "The easiest."
            $ quizNum.append(1)
        "False":
            ""
    label eight:
    show clarrise talk with dissolve
    t "Ninth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "nine"
    menu:
        
        "The cyberspace is also covered in Safe Spaces Act."
        "True":
            m "Got it in the bag."
            $ quizNum.append(1)
        "False":
            ""
    label nine:
    show clarrise talk with dissolve
    t "Last Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "ten"
    menu:
        
        "Public masturbation or flashing of private parts, groping, making offensive body gestures at someone, 
        and other similar lewd sexual actions is a gender-based sexual harassment in Safe Spaces Act."
        "True":
            m "Easy money."
            $ quizNum.append(1)
        "False":
            ""
    label ten:
    
    # Check quiz score
    python:
        for i in quizNum: 
            if quizNum[i] == 1:
                quizPoints += 1

        
    
    scene classroom morning with fade

    "Class" "WAAAAAAA!"

    "Everyone is turning their heads. Asking if they did well."

    show kurtney talk opened with dissolve

    kk "What the hell. That was hard."

    hide kurtney talk opened

    m "Was it? I don't think so. Haha~"

    m "I got [quizPoints] points baby."

    "Mark with a smile on his face, knew he did well."

    # Show achievement if perfect
    # Show test result



label pervTeacher:
    scene black with fade

    centered "1 Week Later..."
    
    scene classroom lunch1 with fade

    "Classroom noises...."

    show kurtney talk opened with dissolve

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

    show kurtney angry talk with dissolve

    kk "They say he's a nasty person."

    m "O-ohh..."

    hide kurtney angry talk with dissolve

    "Noise of footsteps towards the door."

    "???" "Hwehehehe... How you doin' everyone?"

    "Everyone in the classroom gasped."

    show teacher smile1 at right with dissolve

    "???" "I hope we all get along, everyone hehehe~"

    "???" "I will be your substitute teacher for this class."

    "???" "Call me Professor Butch."

    b "These are some nice looking girls, huh?"

    b "Hehehehe... perfect for my taste."

    "What the hell did he just say?"

    "Looking at [kk], she is about to stand up."

    show kurtney talk angry at left with dissolve

    kk "What did you say?!"

    m "You idiot..."

    show teacher closed1 with dissolve

    b "Oh did I ask you to talk? You'll be receiving a failing grade."

    b "Hehehe~"

    hide teacher closed1 with dissolve

    show kurtney talk opened at center with dissolve

    kk "Wha-?"

    show kurtney talk angry at center with dissolve

    "I whispered in Kurt's ears."

    m "Just let it slide dude. I will find a way to report this nasty professor."

    show kurtney smile with dissolve

    kk "O-O-Okaay..."

    jump talkOnHarass


label talkOnHarass:
    $ helpedYui = False
    scene black with fade
    centered "A few days later..."

    if lunchWithYui is True:
        scene schoolground
        
        "What a nice landscape."

        "I see [y] walking across the ground. With a sad expression on her face."

        show yui worry closed with fade
        m "Hey [y]! How's your class doing?"

        m "You called me out to talk about something?"

        show yui worry opened with dissolve

        y "Y-yeah..."

        show yui worry with dissolve

        y "It's about that law you talked about."

        m "The Safe Spaces Act? What about it?"

        y "I have something to talk about related to it...."

        m "Tell me about it."

        hide yui worry with dissolve

        "While clasping her hands firmly for a while, she finally opened her mouth."

        show yui worry opened with dissolve

        y "It's about my professor..."

        y "He's doing something bad... And I can't do anything to stop it."

        m "Who's this professor? Is he teaching here?"

        show yui angry with dissolve

        y "Y-yeah... I hate him. That disgusting person."

        y "When he gave a test the other day... He stares at the girls in a lascivious manner."

        y "When we are in the laboratory, he sneakily touches the butt of some of the girls."

        y "Then he says, \"It's not my fault that you are sexy.\""

        y "And then one time, he..."

        show yui crying with fade

        y "He suddenly touched my shoulders... and pinched it in a manner that is so disgusting. Then he whispered something to my ear."

        m "WHAT?!" with vpunch

        show yui angry with dissolve

        y "Aaaaah! I hate him. Just remembering it makes me puke."

        y "I was almost close to crying in the classroom. I was really shaking and trembling."

        y "The girls in my class can't speak up to him. Also when the boys stand up for us, he gives them a failing mark."

        m "Tell me who is this nasty person?"

        show yui worry opened with dissolve

        y "H-h-his name is Butch..."

        y "They said he was a new faculty teacher..."

        m "I see. So he's also teaching the First Year students. That damned bastard."

        show yui worry with dissolve

        y "M-Mark! I have a favor! Please help me out."

        m "Ahhhh..."

        $ badEndingGame = False
        $ helpedYui = False
        $ timeout = 10
        $ timeout_label = "ignorePerv"
        menu:
            "Should I help her out?"

            "Help her.":
                $ helpedYui = True

                m "Okay [y] I will help you."

                y "Thank you so much!"

                y "Also before I forget to say... There was someone who took a video when he was doing the crime."

                m "Really? Then this will be easy. It should be a solid evidence for his disgusting act."

                jump arrestButch

            "Don't help her.":
                jump ignorePerv
                
        label ignorePerv:
            $ badEndingGame = True

            m "I'm afraid I cannot help. I might get in trouble."

            y "Is that so? That's a real shame..."

            jump badEndStory

    else:
        scene schoolground
        show kurt talk opened
        with fade

        kk "Dude... I have something to talk about."

        kk "It's about that law you talked about."

        m "The Safe Spaces Act? What about it?"

        show kurtney smile with dissolve

        kk "I think we can use this law against that professor."

        m "Tell me more about it."

        show kurtney angry talk with dissolve

        kk "Just the other day, one of our girl classmate got sexually harassed."

        m "Really? That's bad."

        show kurtney talk opened with dissolve

        kk "I've also got stories from other girls in First Year. According to them..."

        show kurtney angry talk with dissolve

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

        show kurtney happy teeth with dissolve

        kk "Now will you help me out?"

        show kurtney smile with dissolve

        kk "Because of you, I learned of the Safe Spaces Act. I knew of the things which a person shouldn't ever do."

        kk "You wanted to be an Attorney right? Help me use this \"Safe Spaces Act\" to arrest that nasty piece of ****."


        menu:
            "Should I help her?"

            "Help her.":
                jump arrestButch

            "Don't help her.":
                jump ignorePerv

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
