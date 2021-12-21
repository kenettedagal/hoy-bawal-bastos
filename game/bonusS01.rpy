 # Main Character
define ray   = Character("Ray Zealsphere", color="#ff0000",ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
define elise = Character("Elise Fonillia", color="#fffb00",ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
define zack  = Character("Zack Ainsteak", color="#ff9900",ctc="ctc", ctc_pause="ctc", ctc_position="fixed")

# Side Character
define kenneth = Character("Kenneth Daberth", color="#0051ff", ctc_pause="ctc", ctc_position="fixed")
define ann = Character("Ann Nozart", color="#ffb5b5", ctc_pause="ctc", ctc_position="fixed")

# Type Writer Effect
init python:
    def type_writer(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/writer.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

# The game starts here.          
label bonusS01:
    $ preferences.set_volume("sfx", 0.30)
    $ preferences.set_volume("voice", 0.40)
    $ preferences.set_volume("music", 0.40)
    $ quick_menu = False
    
    stop music

    play sound "audio/case.mp3" fadeout 0.5

    scene black
    with fade

    with dissolve
    show text "{size=+10}{color=#ff0000}CASE 1:{/color}\n\nKenneth's Desperation{/size}{nw}" at truecenter
    with dissolve

    $ renpy.pause(5.0, hard=True)

    hide text
    with dissolve

    scene bg school
    with fade

    $ quick_menu = True
    
    "{color=#00a62c}{cps=10}{color=#ff0000}Date:{/color} September.17,2020 \n{color=#ff0000}Location:{/color} School (\"Inside a certain clubroom.\") {/cps}{/color}" (callback=type_writer) 

    play sound "audio/next.wav" volume 0.2

    play music "audio/canon.ogg" fadeout 1.0 fadein 1.0 volume 0.3

    scene bg philippines
    with fade

    voice "r1.ogg"
    
    ray "{color=#00a62c}{i}\"A long, long time ago in a beautiful and peaceful country called Philippines....\"{/color}"

    scene bg duterte
    with fade

    voice "r2.ogg"

    ray "{color=#00a62c}{i}\"There was a president named Rodrigo Duterte has been approven a certain law on {color=#ff0000}April 17,2019{/color}....{/color}\""

    scene bg law
    with fade 

    voice "r3.ogg"

    ray "{color=#00a62c}{i}\"And that law is called {color=#ff0000}Republic Act 11313{/color} or also known as {color=#ff0000}Safe Space Act{/color}.{/color}\""

    show bg equality
    with fade

    voice "r4.ogg"

    ray "{color=#00a62c}{i}\"The law stated that both men and women must have equality, security and safety not only in private areas.....\"{/color}"

    show bg safety
    with fade

    voice "r5.ogg"

    ray "{color=#00a62c}{i}\"but also on the streets, public spaces, online, workplaces, educational and training institutions.....\"{/color}"

    scene bg clubroom
    with fade

    play music "audio/Time for Rest.ogg" fadein 0.5 volume 0.3

    voice "r6.ogg"

    ray "Hmm....very intriguing, no matter how many times I read this, it really always enlighten me."

    voice "r7.ogg"

    ray "I guess I should read this again more later especially about the information of potential penalties and consequences to anyone who violated this law."

    play sound "audio/information.wav" volume 0.2

    # Unlock all pages
    $ yuiStoryProgress = 3
    show screen showNotesButton

    "New Information has been added."

    "If you wanna learn more about \"Safe Space Act\" click the button at the top right corner of the screen."

    # !Important ~ add a general log button on the top right corner of the screen for the information you just learn.

    play sound "audio/doorknock.mp3"

    "{i}\"Knock! Knock!\""

    stop sound

    show elise talk neutral with dissolve

    voice "e1.ogg"

    elise "Hey Ray, sorry am late...."

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt001a', 'qt001b','qt001c'])

    show elise surprised

    voice "e2.ogg"

    elise "Huh?! Your reading that again? How many times your gonna read that over and over again, Ray?"

    hide elise surprised with dissolve

    menu:

        elise "{color=#00a62c}\"Huh?! Your reading that again? How many times your gonna read that over and over again, Ray?\"{/color}"

        "Your late!":
            jump qt001a

        "Don't worry, I am just reading this to past time.":         
            jump qt001b

        "Well, this is a reminder to myself.":            
            jump qt001c

label qt001a:
        voice "r8.ogg"
        ray "Your late!"
        show elise talk sad with dissolve
        voice "e3.ogg"
        elise "Yeah...just like I said I'm really sorry."
        show elise angry one
        voice "e4.ogg"
        elise "Also! you don't need to shout geeeshh...."
        voice "r9.ogg"
        ray "Well, I hope you remember the rules and the punishment to anyone whose late."
        jump section2

label qt001b:
        voice "r10.ogg"
        ray "Don't worry, I'm just only reading this to past time."
        show elise smile teeth
        voice "e5.ogg"
        elise "Okay...whatever you say, weirdo hahaha."
        ray "......."
        jump section2

label qt001c:
        voice "r11.ogg"
        ray "Well, this is a reminder to myself."
        show elise smile teeth
        voice "e6.ogg"
        elise "Hahaha, true you should always read that because if you don't you might violate that law hahaha."
        ray "....."
        jump section2

label section2:

    hide elise
    
    play sound "audio/ring.ogg" volume 0.5

    window hide

    show phonecall at truecenter with dissolve

    window show dissolve

    "{i}\"Ray's phone start ringing loudly!\""

    "{i}\"Ray's answer the phone.\""

    show phonecalla at truecenter with dissolve

    stop sound

    play sound "audio/punch.ogg"

    voice "zack1.ogg"

    zack "GENERAL!!!! The client’s accusation is real!!! I also already gathered some {color=#ff9900}evidences{/color} and {color=#ff9900}recorded the scene{/color}!!!!!!!" with vpunch

    voice "zack2.ogg"

    zack "Go to the backside of the gym now!!! Hurry!!! before he do something bad to the client!!!"

    voice "r12.ogg"

    ray "I see, as always good work Major.Zack."

    voice "zack3.ogg"

    zack "Ohh really thanks General hahaha!...wait...Please! just hurry up General."

    voice "r13.ogg"

    ray "Don't worry, we will arrive in the scene in no time."

    voice "zack4.ogg"

    zack "Yes Sir! See you soon."

    "{i}\"Ray stop the phone call.\"{\i}"

    hide phonecall
    hide phonecalla 
    with dissolve

    voice "r14.ogg"

    ray "Lieutenant.Elise! Get ready, we got a case to complete."

    show elise smile closed with dissolve

    voice "e7.ogg"

    elise "Okay! Just give me a sec."

    show elise angry one

    voice "e8.ogg"

    elise "Also! Like I told you don't call me Lieutenant! Geesh!"

    voice "r15.ogg"

    ray "Whatever you say, anyway let’s make a haste Lieutenant.Elise!"

    show elise angry zero

    elise "........"

    scene black
    with fade

    scene bg gym
    with dissolve

    play sound "audio/footsteps.mp3"

    "{i}\"Ray and Elise arrived at the scene.\""

    stop sound

    voice "r16.ogg"

    ray "How's the scene? Major.Zack."

    show zack happy close with dissolve

    voice "zack5.ogg"

    zack "Finally both of you are here! Anyway look overthere!!"

    "{i}Ray and Elise look at the direction his pointing."

    scene black
    with fade

    play music "audio/music/Doll_Dance.ogg" fadein 0.5 fadeout 0.5 volume 0.5

    scene kenneth crime
    with fade

    $ renpy.pause(1.0, hard=True)

    voice "ke1.mp3"

    kenneth "Hehehe, Oh come on baby why are you playing so hard to get hehehe..."

    play sound "audio/breathe.mp3"

    "{i}\"Kenneth's breathe heavily through his mouth.\""

    stop sound

    voice "ann1.ogg"

    ann "Noo!! Please just get away from me! Stop following me!!"

    voice "ke2.mp3"

    kenneth "Hehehe…Ohh come on, don’t you understand! How much I am really obsess to you. Hehehe..."

    voice "ke3.mp3"

    kenneth "I already giving you a lot of hints of how much I love you by {color=#ff0000}staring{/color} at you romantically."

    voice "ann2.ogg"

    ann "Please anyone help me!!...."

    play music "audio/Time for Rest.ogg" fadein 0.5 fadeout 0.5 volume 0.5

    scene bg gym
    with fade

    voice "r17.ogg"

    ray "Hmmm….. it seems this man is really desperate."

    show zack happy opened with dissolve

    voice "zack6.ogg"

    zack "Yeah he is also very creepy, we better give him the right punishment General."

    hide zack happy opened with dissolve

    show elise angry zero with dissolve

    voice "e9.ogg"

    elise "You two! What are you doing?!"

    show elise angry one 

    voice "e10.ogg"

    elise "Just step up to the scene already before this become more worst than it already is!"

    voice "r18.ogg"

    ray "A wise decision, Lieutenant.Elise. I commended you for thinking that."

    show elise angry one

    voice "e11.ogg"

    elise "Geesh!! Just do something already!!"

    play sound "audio/punch.ogg"

    "{i}\"Elise smack Ray's head." with vpunch

    stop sound

    voice "r19.ogg"

    ray "Aww! I am already planning to do that, calm your nerves Lieutenant."

    hide elise

    $ timeout = 7
    $ timeout_label = renpy.random.choice(['qt002a','qt002b'])

    menu:    
        
        "{i}\"How will you approach the scene?\""
        
        "Approach Aggresively":
            jump qt002a
            
        "Approach Politely":
            jump qt002b

label qt002a:
    "{i}Ray approach the scene aggresively."
    voice "r20.ogg"
    ray "Hold it right there! belligerent scum!"
    jump section3

label qt002b:
    "{i}Ray approach the scene politely."
    voice "r21.ogg"
    ray "Hold it right there! crimi...GOOD SIR!"
    jump section3 

label section3:

    show kenneth surprise with dissolve

    voice "ke4.mp3"

    kenneth "Huhhh?!! How long have you been guys standing there!"

    voice "r22.ogg"

    ray "Hahaha....It seems you are not expecting anyone, Mr.Kenneth Dabert."

    show kenneth scared opened

    voice "ke5.mp3"

    kenneth "Huhhh?!! How do you know my name! Don...Don't tell me you guys are the student council officers!"

    voice "r23.ogg"

    ray "Hmm... Sorry to disappoint but no you are wrong about that."

    show kenneth angry opened

    voice "ke6.mp3"

    kenneth "Th-then just tell me who are you guys!!!"

    show kenneth scared teeth

    voice "ke7.mp3"

    kenneth "Also ho...how did you find us here! I am pretty sure no one is following us when we get here."

    voice "r24.ogg"

    ray "Hahaha!! As always, that’s Major.Zack for you. Despite being a airhead, he knowns the right ways to secretly sneak up to his target."

    voice "r25.ogg"

    ray "That’s why I always give you those assignments to secretly investigates potential suspects."

    hide kenneth scared teeth with dissolve
 
    show zack happy teeth with dissolve

    voice "zack7.ogg"

    zack "Hahaha, thanks general."

    hide zack happy teeth with dissolve

    show elise talk confused with dissolve

    voice "e12.ogg"

    elise "Why are you even thanking that idiot, he just call you an airhead you know."

    hide elise talk confused with dissolve

    show kenneth scared opened with dissolve

    voice "ke8.mp3"

    kenneth "Sus-suspect!!! You sound like your saying I did something illegal eyy."

    show kenneth angry teeth

    voice "ke9.mp3"

    kenneth "Anyway just tell me! Who are you guys, suddenly treating me as a suspect. What a bunch of bronze players."

    voice "r26.ogg"

    ray "Well my humble apologies for our rudeness, Mr.Kenneth Dabert. I guess before we proceed on this case we should introduce ourselves first."

    voice "r27.ogg"

    ray "Well then Major.Zack, you may now proceed this introduction first."

    hide kenneth angry teeth with dissolve

    show zack talk asking with dissolve

    voice "zack8.ogg"

    zack "Oh I need to introduce myself right?"

    show zack happy opened zorder 3

    voice "zack9.ogg"

    zack "Okay here we go! My name is {color=#ff9900}Major.Zack{/color}. Nice to meet you!"

    $_dismiss_pause = False
    show movie intro at offscreenleft
    show zorange zorder 2 at offscreenright
    with ease
    
    play sound "audio/fast.wav" volume 0.5

    show movie intro at left
    show zorange zorder 2 at right
    with ease

    show z name zorder 3 at offscreenright
    with ease

    play sound "audio/ting.wav"

    show zack happy close zorder 3 at left
    show z name zorder 3 at left
    with MoveTransition(0.4)

    voice "r28.ogg"

    ray "{i}{color=#00a62c}(\"Zack Ainsteak aka Major.Zack, from class 3-C. Despite being a airhead like I mention earlier.\"){/color}"

    voice "r29.ogg"

    ray "{i}{color=#00a62c}(\"Major.Zack has a proficient skills on concealing his presence. Which give him the perfect role for spy mission investigations and also gathering evidence.\"){/color}"
    
    play sound "audio/fast.wav" volume 0.5

    $_dismiss_pause = False
    show movie intro at offscreenright
    show zorange zorder 2 at offscreenleft  
    with ease
    
    show zack happy close at center 
    show z name zorder 2 at offscreenright
    with MoveTransition(0.2)
    $ renpy.pause(0.3, hard=True)

    voice "r30.ogg"

    ray "Thank you for that wonderful and yet simple introduction Major.Zack, Just like as I expected from you."

    show zack happy teeth

    voice "zack10.ogg"

    zack "Hehehe thanks General."

    voice "r300.ogg"

    ray "Now Lieutenant.Elise, the stage is all yours."

    hide zack happy teeth with dissolve

    show elise angry zero with dissolve

    voice "e14.ogg"

    elise "Okay...fine..Also! How many times do I have to tell you stop calling me Lieutenant!"

    show elise angry one blushed

    voice "e15.ogg"

    elise "It’s really embarrassing you know... especially when there are other people around us!"

    show elise surprised

    voice "e16.ogg"

    elise "Ohh! Sorry about that!!... Okay let me introduce myself."

    show elise talk neutral zorder 3

    voice "e17.ogg"
    
    elise "My name is Elise Fonillia, A third year student. Please to meet you."

    $_dismiss_pause = False
    show movie intro at offscreenright
    show eyellow zorder 2 at offscreenleft
    with ease

    play sound "audio/fast.wav" volume 0.5

    show movie intro at right
    show eyellow zorder 2 at left
    with ease

    show e name zorder 3 at offscreenleft
    with ease

    play sound "audio/ting.wav"

    show elise smile closed zorder 3 at right
    show e name zorder 2 at left
    with MoveTransition(0.4)

    voice "r31.ogg"

    ray "{i}{color=#00a62c}(\"Elise Fonillia aka Lieutenant.Elise, from class 3-B.\"){/color}"

    voice "r32.ogg"

    ray "{i}{color=#00a62c}(\"Like many other people say “Don't judge a book by its cover” and that applies to Lieutenant.Elise.\"){/color}"

    voice "r33.ogg"

    ray "{i}{color=#00a62c}(\"She maybe look like a normal highschool student but don’t get fool by that.\"){/color}"

    voice "r34.ogg"

    ray "{i}{color=#00a62c}(\"Ever since I meet Lieutenant.Elise I notice that she has a strenght more than to a six-footer gorilla.\"){/color}"

    play sound "audio/fast.wav" volume 0.5

    $_dismiss_pause = False
    show movie intro at offscreenleft
    show eyellow zorder 2 at offscreenright
    with ease

    show elise smile closed at center 
    show e name zorder 2 at offscreenleft
    with MoveTransition(0.2)
    $ renpy.pause(0.3, hard=True)

    voice "r35.ogg"

    ray "Thank you for that wonderful and elegant introductions Lieutenant.Elise."

    voice "r36.ogg"

    ray "Well then ladies and gentlemens, as for the next introduction will be next is....."

    show elise angry zero

    elise "....."

    hide elise angry zero with dissolve

    show zack happy opened with dissolve

    voice "zack11.ogg"

    zack "Go General! Yahoo!!!"

    hide zack happy opened with dissolve

    # ! Ray image (optional)

    voice "r37.ogg"

    ray "The last but not the least.....The tactician, the strategist, the mastermind, and also the leader of the {color=#ff0000}HBB Club{/color}!!......"

    play sound "audio/punch.ogg"

    voice "r38.ogg"

    ray "It is I! General.Ray Zealsphere,from class 3-A! at your service!!...." with vpunch

    stop sound

    show zack happy opened with dissolve

    voice "zack12.ogg"

    zack "OOHH YEAHH!! WUHH HOOO!!! GOO GENERAL!"

    hide zack happy opened with dissolve

    show elise angry zero with dissolve

    voice "e18.ogg"

    elise "How stupid...."

    voice "r39.ogg"

    ray "Come on don’t say that Lieutenant.Elise, I may be your General but I am still a human who has a sensitive feelings that can be easily shatter like a wine of glass."

    hide elise angry zero with dissolve

    voice "audio/kennethLine010.mp3"

    show kenneth laugh

    play sound "audio/punch.ogg"

    voice "ke10.mp3"

    kenneth "HEHEHEHE!!! What the hell!!! HEHEHEHE!!!!..." with vpunch

    stop sound

    show kenneth laugh

    voice "ke11.mp3"

    kenneth "You guys are not the student council afterall!!! To be honest I almost got scared....but That's not a problem anymore! Hehehe!!!"

    voice "r40.ogg"

    ray "Hahahaha how foolish of you, we maybe not the student council officers of this school but we still have the right authorities to bring justice to your actions!!"

    voice "r41.ogg"

    ray "Also this student council that you afraid of... let just say that we the {color=#ff0000}HBB Club{/color} might have some connection to them."

    voice "r42.ogg"

    ray "So in case you want to say hello to them,  just ask.\nI could call them anytime you want, Mr.Kenneth Daberth."

    show kenneth lie

    voice "ke12.mp3"

    kenneth "Wha..What do you mean?! In the first place I did not do anything wrong!! Hehehe....that's right!"

    hide kenneth lie with dissolve

    show ann talking 

    play sound "audio/punch.ogg"

    voice "ann3.ogg"

    ann "That's not true!!! Mr.Ray please help me!!! Everything I said yesterday with you guys is true." with vpunch

    stop sound

    voice "r43.ogg"

    ray "Don’t worry, dear client, we hear your humble words that’s why we're here to bring the truth and justice!"

    voice "r44.ogg"

    ray "Major.Zack! Bring me the document files!"

    hide ann talking with dissolve

    show zack happy teeth with dissolve

    voice "zack13.ogg"

    zack "YES SIR!!!"

    play sound "audio/page.mp3"

    "{i}\"Zack's gave Ray a certain document file.\""

    stop sound

    voice "r45.ogg"

    ray "Hmmm I see, very intriguing I must say."

    hide zack happy teeth with dissolve

    show kenneth scared teeth with dissolve

    voice "ke13.mp3"

    kenneth "Wh-what is that document for huh?! Tell me, is it something to do with me right now HUH?!!!!"

    voice "r46.ogg"

    ray "Hold your horses Mr.Kenneth Dabert. Don't worry I will read this document out loud for you."

    play sound "audio/page.mp3"

    "\"Ray start reading the document.\""

    stop sound

    voice "r47.ogg"

    ray "Hmmm I see, Mr.Kenneth Daberth, from class 2-C. Yesterday at 5:27 PM, you got a accusation from this humble lady, she stated here that you been {color=#ff0000}staring{/color} and {color=#ff0000}stalking{/color} her lately."

    show kenneth lie

    voice "ke14.mp3"

    kenneth "Ah..Ahh well so what!!! It’s not like I did something illegal! Hehehe...."

    voice "r48.ogg"

    ray "Well sorry to disappoint you, but you did something illegal and violated a law."

    show kenneth angry opened

    voice "ke15.mp3"

    kenneth "Huu..Huh?! What are you even saying and what kind of law did I even violated in the first place!"

    voice "r49.ogg"

    ray "Mr.Kenneth Daberth, are you perhaps familiar to a law called Republic Act No......"

    voice "r50.ogg"

    voice "r51.ogg"

    ray "......Ahhh..........."

    ray "................................"

    show kenneth angry teeth

    voice "ke16.mp3"

    kenneth "Huh?! why are you suddenly become silent!!! Just tell me already!!!!"

    hide kenneth angry teeth with dissolve

    show elise surprised with dissolve

    voice "e19.ogg"

    elise "Hey Ray, don't tell me you just forgot the law that you almost always reading everyday!"

    voice "r51.ogg"

    ray "No! your mistaken Lieutenant.Elise, Am just trying to ahhh.... mediate! that right! To relax my mind."

    show elise angry three

    voice "e20.ogg"

    elise "Really I hope your not lying Ray... or else..."

    "Elise's clenched her fist intensely."

    voice "r52.ogg"

    ray "Hahaha....do...don't worry, I am done mediating now. I will now tell to Mr.Kenneth Daberth about what kind of law he violated."

    hide elise angry three with dissolve

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt003a','qt003b','qt003d'])

    voice "r53.ogg"

label firstQuestion:

    menu:
        ray "{color=#00a62c}(\"This is bad, what is that law No. again?\"){/color}"
        "Re-semiprivate Act 12345":
            jump qt003a
        "Reprivate Act 22244":
            jump qt003b
        "Republic Act 11313":
            jump qt003c
        "Rebuild Act 11202":          
            jump qt003d


label qt003a:
        voice "r54.ogg"
        ray "The name of the law that you violated is Re-semiprivate Act 12345!"
        show elise angry three with dissolve
        voice "e21_22.ogg"
        elise "Wait! Ray...are you serious, I told you that if your lying...."
        "{i}\"Elise's starting to raise her first.\""
        voice "r55_57_61.ogg"
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        show elise angry zero
        elise "......."
        hide elise angry zero with dissolve
        jump firstQuestion

label qt003b:
        voice "r56.ogg"
        ray "The name of the law that you violated is Reprivate Act 22244!"
        show elise angry three with dissolve
        voice "e21_22.ogg"
        elise "Wait! Ray...what you even saying, I told you if your lying...."
        "{i}\"Elise's starting to raise her first.\""
        voice "r55_57_61.ogg"
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        show elise angry zero
        elise "......."
        hide elise angry zero with dissolve
        jump firstQuestion

label qt003c:
        voice "r58.ogg"
        ray "The name of the law that you violated is {color=#ff0000}Republic Act 11313!{/color}"
        show elise smile teeth with dissolve
        voice "e23.ogg"
        elise "Haaa so your actually just messing around. Geeshh I almost planning to hit you in the face real hard if your actually lying."
        voice "r59.ogg"
        ray "{i}{color=#00a62c}(\".......well thank god I finally remember it.\"){/color}"
        hide elise smile teeth with dissolve
        jump section4

label qt003d:
        voice "r60.ogg"
        ray "The name of the law that you violated is Rebuild Act 11202!"
        show elise angry three with dissolve
        voice "e24.ogg"
        elise "Wait! Ray...are you even for real! I still remember the law that your trying to say, I told you if you lying...."
        "{i}\"Elise's starting to raise her first.\""
        voice "r55_57_61.ogg"
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        voice "r62.ogg"
        ray "{color=#00a62c}(\"Geesh...if you know the answer just say it.... No as the leader I should be the one to say this.\"){/color}"
        show elise angry zero
        elise "......."
        hide elise angry zero with dissolve
        jump firstQuestion

label section4:

    show kenneth angry opened with dissolve

    voice "ke17.mp3"

    kenneth "Republic Act 11313...ahh! What does that law even mean!! Are you sure your not making this up!!"

    hide kenneth angry opened with dissolve

    show elise talk neutral with dissolve

    voice "e25.ogg"

    elise "Come on Ray, be more specific."
    
    hide elise talk neutral with dissolve

    show zack happy opened

    voice "zack14.ogg"

    zack "You got this General!"

    hide zack happy opened with dissolve

    voice "r63.ogg"

    ray "O..Okay calm down everyone, I got this."

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt004a','qt004b','qt004d'])

    voice "r64.ogg"

    menu secondQuestion:

        ray "{color=#00a62c}Of course I know this, Republic Act 11313 is also known as....{/color}"

        "Safe Place Act":
            jump qt004a

        "Safe Guard Act":
            jump qt004b

        "Safe Space Act":
            jump qt004c

        "Safe Security Act":
            jump qt004d

label qt004a:
    voice "r65.ogg"
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Place Act!"
    show zack talk confuse with dissolve
    voice "zack15.ogg"
    zack "Really? I am pretty sure it sounds more like something to do with stars in the galaxy, General."
    voice "r66_68_73.ogg"
    ray "Ohh?! Am just joking! Hahaha!"
    hide zack talk confuse with dissolve
    show elise angry zero with dissolve
    elise "....."
    hide elise angry zero with dissolve
    show kenneth angry opened with dissolve
    voice "ke18.mp3"
    kenneth "Just tell me already!!!" with vpunch
    hide kenneth angry opened
    jump secondQuestion

label qt004b:
    voice "r67.ogg"
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Guard Act!"
    show zack talk confuse with dissolve
    voice "zack16.ogg"
    zack "Safe Guard Act? Sounds like something I used to wash my hands after collecting some evidence, General."
    voice "r66_68_73.ogg"
    ray "Ohh?! Am just joking! Hahaha!"
    hide zack talk confuse with dissolve
    show elise angry zero with dissolve
    elise "....."
    hide elise angry zero with dissolve
    show kenneth angry opened with dissolve
    voice "ke18.mp3"
    kenneth "Just tell me already!!!" with vpunch
    hide kenneth angry opened with dissolve
    jump secondQuestion

label qt004c:
    voice "r69.ogg"
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Space Act!"
    show zack happy opened with dissolve
    voice "zack17.ogg"
    zack "Yeah! That's right, {color=#ff0000}Safe Space Act{/color}! I really like the name of this law."
    voice "r70.ogg"
    ray "I also agree, Major.Zack."
    hide zack happy opened with dissolve
    jump section5

label qt004d:
    voice "r71.ogg"
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Security Act!"
    show zack talk confuse with dissolve
    voice "zack18.ogg"
    zack "Safe Security Act? Hmmm? General I feel like that's not the right name as far as I remember."
    voice "r72.ogg"
    ray "{color=#00a62c}(\"What! That's wrong! Am pretty sure that's the right name. I guess am the airhead, not Major.Zack.\"){/color}"
    voice "r66_68_73.ogg"
    ray "Am just joking! Hahaha!"
    hide zack talk confuse with dissolve
    show elise angry zero with dissolve
    elise "....."
    hide elise angry zero with dissolve
    show kenneth angry opened with dissolve
    voice "ke18.mp3"
    kenneth "Just tell me already!!!" with vpunch
    hide kenneth angry opened with dissolve
    jump secondQuestion

label section5:

    show kenneth confuse with dissolve

    voice "ke19.mp3"

    kenneth "Safe Space Act?"

    voice "r73.ogg"

    ray "It seems your not familiar about what is Safe Space Act, Mr.Kenneth Daberth."

    show kenneth angry opened

    voice "ke20.mp3"

    kenneth "Hell if I know!"

    voice "r74.ogg"

    ray "Then if you please, let me enlighten you about what is this {color=#ff0000}Safe Space Act{/color} that am I speaking of."

    show kenneth lie

    voice "ke21.mp3"

    kenneth "Hmph! Sure! Why not! It’s not like I..I di....did something wrong in the first place!! hehehe....."

    voice "r75.ogg"

    ray "Ohh am not sure about. Now then let me start to explain this to you, Good Sir."

    voice "r76.ogg"

    ray "{color=#ff0000}Republic Act 11313{/color} or also known as {color=#ff0000}Safe Space Act{/color}, is a law that has been approved by our president on {color=#ff0000}April 17,2019{/color}."

    voice "r77.ogg"

    ray "Well, according to this law it stated that {color=#ff0000}intrusive leering{/color} and {color=#ff0000}stalking{/color} is a violation to humans rights."

    show kenneth surprise

    voice "ke22.mp3"
    
    kenneth "Wh...What the hell!!.. I had no idea...."

    voice "r78.ogg"

    ray "Now then, let me tell you the potential consequences that a guilty party have to face for anyone who violated this law."

    show kenneth scared teeth

    voice "ke23.mp3"

    kenneth "...Co..Come ON! tell me! Afterall I didn't do anything wrong!"

    voice "r79.ogg"

    ray "Well, for the {color=#ff0000}first offenders{/color}, violating this law could punish you by a 1000 pesos fine."

    show kenneth surprise

    voice "ke24.mp3"

    kenneth "What?! you serious bruh?! I can buy a lot of skins in-game with that money!"

    voice "r80.ogg"

    ray "Also a community service of twelve hours inclusive of attendance to a Gender Sensitivity Seminar to be conducted by the PNP in coordination with the LGU and the PCW."

    show kenneth scared opened

    voice "ke25.mp3"

    kenneth "What?! community service! like I have time for that!"

    voice "r81.ogg"

    ray "Ohh, Also don't get me wrong this punishment I mentions is just for doing violation acts like {color=#ff0000}intrusive learing{/color}..."

    voice "r82.ogg"

    ray "...while the case of doing things like {color=#ff0000}stalking{/color} to someone has more hasher punishment compare to this one like I mention ealier."

    show kenneth scared teeth

    kenneth "!!!!!"

    voice "r83.ogg"

    ray "Hmmm.... it seems you finally have some grasp about what is this law called Safe Space Act."

    voice "r84.ogg"

    ray "Also as I reminder I only mention the punishment for the first offenders, Mr.Kenneth Daberth."

    voice "r85.ogg"

    ray "I wonder what will happen more if you violated this law more, well I only guarantine you that it will be of course become much more worse."

    show kenneth serious

    kenneth "........."

    kenneth "................"

    kenneth "......................."

    voice "r86.ogg"

    ray "Hmmm? Mr.Kenneth Daberth, are you feeling well right now? It seems you need medical assistance right now."

    show kenneth serious laugh

    voice "ke26.mp3"

    kenneth ".....heheh...hehhehe....heheheh.....HEHEHEHEHE!!!!!"

    show kenneth laugh crazy

    voice "ke27.mp3"

    kenneth "HEHEHEHE!!! WHERE IS YOUR EVIDENCE THAT I DID THOSE THINGS TO THIS UGLY WOMAN????!!!"

    hide kenneth laugh crazy with dissolve

    show ann terrified with dissolve

    voice "ann4.ogg"

    ann "!!!!" with vpunch

    hide ann terrified with dissolve

    show kenneth laugh crazy with dissolve

    voice "ke28.mp3"

    kenneth "THIS UGLY WOMAN ACCUSATION IS NOT ENOUGH TO PROVE THAT I REALLY DID THOSE THINGS TO HER!!"

    voice "r87.ogg"

    ray "Well, that’s true Mr.Kenneth Daberth."

    show kenneth laugh crazy

    voice "ke29.mp3"

    kenneth "GOOD! This is stupid am leaving! Hehehehe...\n{color=#00a62c}(\"GG EZ...hehe...I guess I should go home and play a one match of PoP to forget what happen here. Hehe...\""

    hide kenneth laugh crazy with dissolve

    "{i}Kenneth Daberth nervously leave the scene slowly.{/i}"

    show zack talk surprise with dissolve

    voice "zack19.ogg"

    zack "Ahh! His leaving General..."

    hide zack talk surprise with dissolve

    play sound "audio/punch.ogg"

    voice "r88.ogg"

    ray "Hold up! Mr.Kenneth Daberth! You may have the right to remain silent but we have the EVIDENCE! that can prove to you that your not innocent!" with vpunch

    voice "r89.ogg"

    ray "So are you quite sure you wanna leave right now, or else maybe tomorrow the Student Council might have give you a visit."

    show kenneth angry teeth with dissolve

    voice "ke30.mp3"

    kenneth "!!!!" with vpunch

    hide kenneth angry teeth with dissolve

    show zack surprise opened with dissolve

    voice "zack20.ogg"

    zack "Wait really!!! We have the evidence General?!!!"

    hide zack surprise opened with dissolve

    show elise angry zero with dissolve

    elise "......"

    hide elise angry zero with dissolve

    voice "r90.ogg"

    ray "Hahaha....have you already forgotten, Major.Zack. You mention earlier that you already manage to gathered some evidence for this case."

# Flashback part:
    window hide

    play sound "audio/flash.mp3"
    
    scene white
    with dissolve
    
    scene bg flash
    with dissolve

    window show dissolve

    play sound "audio/ring.ogg" volume 0.5

    "{i}\"Ray's phone start ringing loudly!\""

    stop sound

    zack "GENERAL!!!! The client’s accusation is real, I also already gathered some {color=#ff9900}evidences{/color} and {color=#ff9900}recorded the scene{/color}!!!!!!!" with vpunch

    window hide

    play sound "audio/flash.mp3"

    scene white
    with dissolve

    scene bg gym
    with dissolve

    window show dissolve

    show zack happy opened with dissolve

    voice "zack21.ogg"

    zack "Oh yeah your right General! I finally remember, I did in fact gathered some evidences earlier...."

    show zack talk confuse

    voice "zack22.ogg"

    zack "...but....General....."

    voice "r91.ogg"

    ray "But what? Major.Zack."

    show zack talk confuse

    voice "zack23.ogg"

    zack "Well General....its true that I did in fact collected some evidences earlier which is currently right now inside my evidence pouch archive....."

    voice "r92.ogg"

    ray "Hahaha, That's good to know Major.Zack, you are really doing your job properly. I respect that."

    voice "zack24.ogg"

    show zack talk worried

    zack "Haha.. Thanks General, but the my problem right now is that I don't know which evidence you want me to present right now."

    voice "r93.ogg"

    ray "It’s fine Major.Zack, that’s one of your flaws but I understand. So don’t be nervous right now, but instead be rest assured because I got you covered."

    voice "r94.ogg"

    ray "Afterall, if your job is to spy and find evidences. Then my job is to used those information you gathered to show them and reveal to them the truth and justice."

    show zack happy opened

    voice "zack25.ogg"

    zack "Wow, that's awesome General!"

    hide zack happy opened with dissolve

    show elise talk confused with dissolve

    voice "e26.ogg"

    elise "Haaaa....You guys are really hopeless....Ray are you really sure that Zack really do have the evidence for this case?"

    voice "r95.ogg"

    ray "Hoo? Don't worry Lieutenant.Elise, soon you will get your moment to shine."

    show elise angry one

    voice "e27.ogg"

    elise "Haa?!!...That's not what am worried for, idiot."

    hide elise angry one with dissolve

    show kenneth angry teeth with dissolve

    play sound "audio/punch.ogg"

    voice "ke30.mp3"

    kenneth "HEY!! YOU GUYS STOP FOOLING AROUND!! JUST SHOW ME THAT EVIDENCE YOUR TALKING ABOUT!!" with vpunch

    hide kenneth angry teeth with dissolve

    show zack happy opened with dissolve

    voice "zack26.ogg"

    zack "General! Hurry! What evidence you want me to present?!"

    voice "r96.ogg"

    ray "Well then, I will tell you the evidence that will prove that Mr.Kenneth Daberth did in fact is not innocent!"

    hide zack happy opened with dissolve

    show kenneth angry opened with dissolve

    voice "ke31.mp3"

    kenneth "COME ON SHOW ME!!!"

    hide kenneth angry opened with dissolve

    voice "r97.ogg"

    ray "Major.Zack, show me all the evidences that you manage to gathered!"

    show zack happy teeth with dissolve

    # ! Yes Sir

    zack "Yes SIR!!!"

    hide zack happy teeth with dissolve

    "{i}\"Zack shows you all the evidence he gathered.\""

    voice "r98.ogg"

    ray "{color=#00a62c}(\"Haha...as always Major.Zack. Some of the things here are not even could be consider as evidence for this case. Most of them are just trash!\"){/color}"

    voice "r99.ogg"

    ray "{color=#00a62c}(\"Well okay then, Time to show the culprit the evidences!\"){/color}"

label evidence:
    
    $timeout = 10
    $timeout_label = renpy.random.choice(['ed001a', 'ed001b','ed001c'])

    voice "r100.ogg"

    menu: 
        
        ray "{color=#00a62c}(\"Let's see here, What evidence I should show to prove Mr.Kenneth Daberth is not innocent.\"){/color}"

        "{image=peel.png}\nBanana Peal":
            jump ed001a

        "{image=wrapper.png}\nCandy Wrapper":
            jump ed001b

        "{image=leaf.png}\nLeaf":
            jump ed001c

        "{image=phone.png}\nZack's Phone":
            jump ed001d

label ed001a:
    voice "r101.ogg"
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}BANANA PEEL{/color}!!!"
    show kenneth laugh with dissolve
    play sound "audio/punch.ogg"
    voice "ke32.mp3"
    kenneth "BANANA PEEL?! HAHAHA!! HOW CAN A BANANA PEEL PROVE THAT AM NOT INNOCENT EYY!!! STUPID BRONZE PLAYER!!!" with vpunch
    hide kenneth laugh with dissolve
    show elise angry three with dissolve
    voice "e28.ogg"
    elise "Hey! Are you trying to mess with me huh?! RAY!!"
    voice "r102.ogg"
    ray "No..Noo am just showing the banana peel, afterall it look kinda delicious! But too bad it looks like someone already ate it."
    show elise angrier zero with dissolve
    elise "....."
    hide elise angrier zero with dissolve
    voice "r103.ogg"
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001b:
    voice "r104.ogg"
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}CANDY WRAPPER{/color}!!!"
    show kenneth scared opened with dissolve
    voice "ke33.mp3"
    kenneth "A CANDY WRAPPER YOU SAY! How..NOOO I DIDN\'T SHOPLIFTED ANY CANDIES EARLIER OKAY!!!"
    hide kenneth scared opened with dissolve
    show elise angry one with dissolve
    voice "e29.ogg"
    elise "Hey! What the are you doing?! Show the evidence already!"
    voice "r105.ogg"
    ray "Hahaha...I am just joking this time, Now I will show you the real evidence."
    show elise angry zero
    elise "......"
    hide elise angry zero with dissolve
    voice "r106.ogg"
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001c:
    voice "r107.ogg"
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}LEAF{/color}!!!"
    show kenneth scared opened with dissolve
    voice "ke34.mp3"
    kenneth "NO!! YOUR WRONG! I DON\'T SMOKE WEE...I MEAN LEAF!!!"
    hide kenneth scared opened with dissolve
    show zack happy opened with dissolve
    voice "zack27.ogg"
    zack "AHA! General! This guy is a drug user!!!"
    voice "r108.ogg"
    ray "Hahaha...I don't think so Major.Zack."
    show zack happy teeth
    voice "zack28.ogg"
    zack "Ohh your just joking again right General, Hahahaha."
    hide zack happy teeth with dissolve
    show elise angry zero with dissolve
    elise "......"
    hide elise angry zero with dissolve
    voice "r109.ogg"
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001d:
    voice "r110.ogg"
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this! {color=#ff9900}MAJOR.ZACK'S PHONE{/color}!!!"
    show zack surprise opened with dissolve
    voice "zack29.ogg"
    zack "What! Ohhh yeah... I almost forgot I recorded some scene when this criminal is doing some bad things to our client earlier General."
    hide zack surprise opened with dissolve
    show elise angry one with dissolve
    voice "e30.ogg"
    elise "Huh?! Are you even serious, Zack. Why did you not just stop this creep already when he doing some bad things to our client."
    hide elise angry one with dissolve
    show zack talk confuse with dissolve
    voice "zack30.ogg"
    zack "Ahh! Well I think its for the best to gathered some evidence instead because even if I tell this criminal to stop he won't listen to me I think...."
    show zack happy teeth
    voice zack00n.mp3
    zack "Also am pretty sure that even I managed to stop him, he will just find another moment again to do some bad things again to our client. So I guess its better to follow the General's Order."
    hide zack talk confuse with dissolve
    show elise angry three with dissolve
    voice "e31.ogg"
    elise "HUH?! Your kidding right! Do you even call yourself a man!"
    hide elise angry three with dissolve
    show zack talk worried with dissolve
    voice "zack31.ogg"
    zack "I am really sorry! I guess I should stop him before even I don't have the strenght like a goril...." 
    play sound "audio/punch.ogg"
    voice "r111.ogg"
    ray "SILENT!! Major.Zack!" with vpunch
    voice "r112.ogg"
    ray "I....I understand what your trying to say, Major Zack. But sometimes, there are times you really need to step up to the scene before its to late, remember this, Major Zack."
    show zack happy opened
    voice "zack32.ogg"
    zack "Wow, that sounds amazing, okay copy that General! I will take a note about this."
    hide zack happy opened with dissolve
    show elise angry one with dissolve
    voice "e32.ogg"
    elise "....don't have the strenght like a goril..what are you even trying to say Zack, could you just say it again this idiot suddenly interrupted you."
    play sound "audio/punch.ogg"
    voice "r113.ogg"
    ray "THAT'S! enough for talk now Lieutenant.Elise. We still need to prove why Zack's Phone is the reason why Mr.Kenneth Daberth is guilty." with vpunch
    show elise angry zero
    elise "....."
    hide elise angry zero with dissolve
    jump section6

label section6:

    show kenneth scared opened with dissolve

    voice "ke35.mp3"

    kenneth "YEAH! YOU GUYS STOP FOOLING AROUND ALREADY! WHY IS THAT PHONE IS THE EVIDENCES EYY?!! I STILL HAVE A DATE TO ATTEND SOON!! HURRY UP!!!"

    voice "r114.ogg"

    ray "Sorry about that Mr.Kenneth Daberth I guess you have to cancel that date, though I highly doubt it."

    voice "r115.ogg"

    ray "Well the reason why Zack's Phone is the evidence that will prove you guilty is already obvious."

    voice "r116.ogg"

    ray "And I am pretty sure you already know it."

    show kenneth lie

    voice "ke36.mp3"
 
    kenneth "!!!!...NO I DON'T KNOW!!! Heheee...."

    voice "r117.ogg"

    ray "Okay, then let's ask Major.Zack."

    hide kenneth lie with dissolve

    show zack happy close with dissolve

    voice "zack33.ogg"

    zack "Need something? General."

    voice "r118.ogg"

    ray "Let me ask you, do you remember the phone call we had ealier. Do remember that you mention that you recorded the some scene right."

    show zack talk surprise

    voice "zack34.ogg"

    zack "Yes General, I recorded him lately for evidence while this criminal has been desperately {color=#ff0000}stalking{/color} and {color=#ff0000}staring{/color} the client, General."

    voice "r119.ogg"

    ray "Okay then, please play that video Major Zack."

    show zack happy opened

    voice "zack38.ogg"

    zack "YES SIR!!!"

    show zack talk confuse

    voice "zack35.ogg"

    zack "Hmm... Let's see where did I save that video file again?"

    voice "r120.ogg"

    ray "......Haha...ha...Please take your time Major Zack."

    hide zack talk confuse with dissolve

    show elise talk sad with dissolve

    voice "e33.ogg"

    elise "Ray....just like I expected, both of you guys are hopeless....."

    voice "r121.ogg"

    ray "Oh come on now Lieutenant.Elise, le....let's just wait and trust Major.Zack okay....."

    hide elise talk sad with dissolve

    voice "r122.ogg"

    ray "{color=#00a62c}(\"This is starting to make me nervous....\")"

    show kenneth scared opened with dissolve

    play sound "audio/punch.ogg"

    voice "ke37.mp3"

    kenneth "HEY HURRY UP!!!!" with vpunch

    hide kenneth scared opened with dissolve

    stop sound

    show zack happy opened with dissolve

    voice "zack36.ogg"

    zack "OH!!! Found it! Phew I though I lost it but it just got mix up to other old videos that also recorded for evidence. Hahaha, okay let me play the video now."

    hide zack happy opened with dissolve

    "{i}\"Zack play the video he recorded on his phone.\""

    # !Important ~ Add a image of Kenneth Daberth stalking and staring activities.

    show kenneth angry teeth with dissolve

    play sound "audio/punch.ogg"

    voice "ke38.mp3"

    kenneth "NOOO!! BUT HOW?! I AM REALLY PRETTY SURE NO ONE IS AROUND US." with vpunch

    stop sound

    voice "r123.ogg"

    ray "Hahahahah, as always good work Major.Zack, not even the slightless I doubt your work. {color=#00a62c}(\"Phew...thank god, He actually managed to record a scene for evidence.\"){/color}"

    hide kenneth angry teeth with dissolve

    show zack happy teeth with dissolve

    voice "zack37.ogg"

    zack "Thank you GENERAL!!!"

    hide zack happy teeth with dissolve

    voice "r124.ogg"

    ray "Well are you satisfied now Mr.Kenneth Daberth or will you still deny your actions. If that's the case then am telling you this will only become much more worse for you, Good Sir."

    voice "r125.ogg"

    ray "Hmm??"

    show kenneth serious with dissolve

    kenneth "............"

    voice "ke39.mp3"

    kenneth "Hooo...Hooyoyoyoyoyo..........."

    show kenneth scared opened

    play sound "audio/punch.ogg"

    voice "ke40.mp3"
    
    kenneth "This is BAD!!!!!! MY MOTHER WILL SPANK MY ASS AT THIS RATE IF SHE FOUND OUT WHAT I DID!!!" with vpunch

    stop sound

    hide kenneth scared opened with dissolve

    show elise smile teeth with dissolve

    voice "e34.ogg"

    elise "Hahahahaha...."

    show elise surprised

    voice "e35.ogg"

    elise "Ahh! Sorry about that....."

    hide elise surprised with dissolve

    ray ".........."

    voice "r126.ogg"

    ray "Mr.Kenneth Daberth, based on the investigation and evidence it seems the verdict is clear. I guess it's about time to wrap this thing up."

    show ann relief with dissolve

    voice "ann5.ogg"

    ann "Haaaa.....Finally....."

    hide ann relief with dissolve

    $ timeout = 7
    $ timeout_label = renpy.random.choice(['qt005a','qt005b'])

    menu verdict:

        "{i}\"Is Mr.Kenneth Daberth {color=#ff0000}Guilty{/color} or {color=#0044ff}Innocent{/color}\""

        "Guilty":
            jump qt005a
        "Innocent":
            jump qt005b

label qt005a:
    voice "r127.ogg"
    ray "Mr.Kenneth Daberth, YOU ARE FOUND GUILTY!!! The court is now adjourned."
    show kenneth surprise with dissolve
    play sound "audio/punch.ogg"
    voice "ke40.mp3"
    kenneth "NOOO!!!!!!" with vpunch  
    stop sound  
    hide kenneth surprise with dissolve
    jump section7

label qt005b:
    voice "r128.ogg"
    ray "Mr.Kenneth Daberth, congratulation you won the case. You are found innocent. The court is now adjourned."
    show kenneth scared opened with dissolve
    voice "ke41.mp3"
    kenneth "WHAT!! REALLY!!!...I thought am busted already....."
    hide kenneth scared opened with dissolve
    show elise angrier three with dissolve
    play sound "audio/punch.ogg"
    voice "e36.ogg"
    elise "RAY!!!! STOP JOKING AROUND!!! ARE YOU REALLY GONNA LET A CRIMINAL ESCAPE!!!!" with vpunch
    stop sound
    play sound "audio/punch.ogg"
    "{i}Elise smack Ray's head.{/i}" with vpunch
    stop sound
    voice "r129.ogg"
    ray "AWWW!!! I'M SORRY!! OKAY!! OKAYY!! THIS TIME I WILL NOT MESS AROUND!!!"
    voice "r130.ogg"
    ray "{color=#00a62c}(\"Okay....No more messing around this time I will tell the truth.\")"
    hide elise angrier three with dissolve
    jump verdict

label section7:

    voice "r131.ogg"

    ray "And lastly, this case is COM!!...."

    show zack surprise opened with dissolve 

    play sound "audio/punch.ogg"

    voice "zack38.ogg"

    zack "WAIT!!! General!!!!!! The suspect is escaping!!!!!!!" with vpunch

    stop sound

    hide zack surprise opened with dissolve 

    play sound "audio/footsteps.mp3"

    "{i}\"Kenneth Daberth quickly tries to escape the scene.\"{/i}"

    stop sound

    voice "r132.ogg"

    ray "Ahhh! Right when I finally able to say my favorite line!!! This man deserve a harsh punishment!!! Lieutenant Elise, requesting for back-up!"

    show elise talk confused with dissolve

    voice "e37.ogg"

    elise "Geeshh! Am already here what are you even talking about."

    show elise talk neutral

    voice "e38.ogg"

    elise "Anyway, I got this. Zack give me that {color=#ff9900}Banana Peel{/color} in your evidence pouch or whatever you called that bag is."

    hide elise talk neutral with dissolve

    show zack happy teeth with dissolve

    voice "zack39.ogg"

    zack "YES MAAM!"

    hide zack happy teeth with dissolve

    show kenneth scared teeth with dissolve

    voice "ke43.mp3"

    kenneth "I BETTER RUN FAST!!!!, IMAGINE!!! IMAGINE IT!!! LIKE AM USING THE SKILL FLASHSTEPPPP LIKE IN THE GAME of PoP!!!!"

    show kenneth laugh crazy

    voice "ke44.mp3"

    kenneth "HEEHEHEHEH!!!!!!! I CAN FEEL IT!!!! I AM RUNNING SO FAST YAHOO!!!!! I WILL ESCAPE THIS IN NO TIME!!!"

    hide kenneth laugh crazy with dissolve

    show zack talk surprise with dissolve

    voice "zack40.ogg"

    zack "Wow...his really fast!!!"

    voice "r133.ogg"

    ray "Hmm...his already about approximately 28 meters away from us."

    hide zack talk surprise with dissolve

    show elise smile teeth with dissolve

    voice "e39.ogg"

    elise "Don't worry I got this, Even if his already in the other side of the planet I can still throw this {color=#ff9900}Banana Peel{/color} right in front of his feet to lose his balance."

    voice "r134.ogg"

    ray "Hahahaha! True, I never doubt your strenght Lieutenant.Elise. Afterall, you have more strenght than a 6-footer gorilla. AHH!"

    hide elise smile teeth with dissolve

    voice "r135.ogg"

    ray "{color=#00a62c}(\".....di..did I say it out loud. I hope she did not heared me just now......\"){/color}"

    show elise angry one with dissolve

    voice "e40.ogg"

    elise "TAKE THIS!!!!!!"

    hide elise angry one with dissolve

    show kenneth defeat with dissolve

    kenneth "AWWWW MAMA DON’T HIT MEE!!!!!"

    hide kenneth defeat with dissolve

    voice "r136.ogg"

    ray "It seems the culprit is already experiencing the punishment he deserved for his actions."

    voice "r137.ogg"

    ray "I guess the time has come."

    show zack happy teeth with dissolve

    voice "zack13.ogg"

    zack "YES SIR!"

    hide zack happy teeth with dissolve

    show elise angry zero with dissolve

    elise "......."

    hide elise angry zero with dissolve

    play sound "audio/punch.ogg"

    voice "r138.ogg"

    ray "THIS CASE IS COMPLETE!!{color=#00a62c}(\"Yeah finally hahaha...\"){/color}" with vpunch

    stop sound

    show ann happy with dissolve

    voice "zack41.ogg"

    voice "ann6.ogg"

    ann "Ahh excuse meee....ahh Mr.Ray and everyone, thank you very much for helping me."

    voice "r139.ogg"

    ray "No worries, it’s our duty to help our people, right everyone?"

    hide ann happy with dissolve

    show zack happy teeth with dissolve

    voice "zack13.ogg"

    zack "YES SIR!!"

    hide zack happy teeth with dissolve

    show elise angrier zero with dissolve

    elise "......."

    elise "..........."

    elise "................"

    voice "r140.ogg"

    ray "Ah...Ahhh......Lieutenant.Elise? Somethings wrong? You seems awfully quiet.... are you perhaps already hungry?"

    show elise angrier one

    voice "e41.ogg"

    elise "Ray.... how many times do I have to tell you don't call me Lieutenant, but still you won't listen and NOW!!!..."

    # Missing

    ray "heyy....calm down...."

    show elise angrier three

    voice "e42.ogg"

    elise "AND NOW! You just compare me to a GO...GOO...GORILLA!!!!"

    voice "r141.ogg"

    ray "ohhh….ohhhhh come on Lieutenant.Elise, I am just joking you know."

    voice "r142.ogg"

    ray "Af...Afterall.....a leader must also show his humor sometimes to his subordinates right? right Major.Zack?"

    hide elise angrier three with dissolve

    show zack happy teeth with dissolve

    voice "zack13.ogg"

    zack "YES SIR!!!"

    voice "r143.ogg"

    ray "Is that the only thing you can say right now!! At least say something else, I save your sorry ass earlier you know."

    show zack happy teeth

    voice "zack41.ogg"

    zack "YES SIR!!!! Thank you very much for saving me even though I don't remember it!!!"

    hide zack happy teeth with dissolve

    show elise angrier three with dissolve

    elise "......"

    hide elise angrier three with dissolve

    show ann relief with dissolve

    voice "ann7.ogg"

    ann "Ahh excuse me.....to be honest looks like Mr.Ray also need to get punished for verbally abusing Miss.Elise."

    voice "r144.ogg"

    ray "WH..WHAT I JUST HELP YOU! YOU KNOW! ATLEAST SHOW SOME GRATITUDE!"

    show ann terrified

    voice "ann8.ogg"

    ann "sor..Sorry!!!....Please don't hit me!!!"

    hide ann terrified with dissolve

    show elise angrier three with dissolve

    voice "e43.ogg"

    elise "....RAAYY!!!!"

    hide elise angrier three with dissolve

    "{i}\"Elise slowly approach Ray intensely.\""

    show elise angrier three with dissolve

    voice "r145.ogg"

    ray "Hey calm down Lieutenant.Elise! Anyone please help or alteast somebody stop her!! CALL THE ANIMAL CONTROL DEPARTMENT!! PLEASE!!! AHHHHH!!!"

    hide elise angrier three with dissolve

    "{i}\"And on that day, all the students heard a short loud scream throughout the campus.\""

    # Missing

    ray "AH!.................................................."

    "{i}\"And that's the only beginning of the HBB Club story.\""

    scene black
    with fade

    centered "END...."

    # This ends the game.

    $ bonusScript = False

    return
