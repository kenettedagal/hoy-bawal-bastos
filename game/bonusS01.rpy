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

$ bonus_script = True

# The game starts here.          
label bonusS01:
    
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
    
    "{color=#00a62c}{cps=10}{color=#ff0000}Date:{/color} September.17,2020 \n{color=#ff0000}Location:{/color} School (\"Inside a certain clubroom.\") {/cps}{/color}" (callback=type_writer) 

    play sound "audio/next.wav" volume 0.2

    play music "audio/canon.ogg" fadeout 1.0 fadein 1.0 volume 0.3

    scene bg philippines
    with fade
    
    ray "{color=#00a62c}{i}\"A long, long time ago in a beautiful and peaceful country called Philippines....\"{/color}"

    scene bg duterte
    with fade

    ray "{color=#00a62c}{i}\"There was a president named Rodrigo Duterte has been approven a certain law on {color=#ff0000}April 17,2019{/color}....{/color}\""

    scene bg law
    with fade 

    ray "{color=#00a62c}{i}\"And that law is called {color=#ff0000}Republic Act 11313{/color} or also known as {color=#ff0000}Safe Space Act{/color}.{/color}\""

    show bg equality
    with fade

    ray "{color=#00a62c}{i}\"The law stated that both men and women must have equality, security and safety not only in private areas.....\"{/color}"

    show bg safety
    with fade

    ray "{color=#00a62c}{i}\"but also on the streets, public spaces, online, workplaces, educational and training institutions.....\"{/color}"

    scene bg clubroom
    with fade

    play music "audio/Time for Rest.ogg" fadein 0.5 volume 0.3

    ray "Hmm....very intriguing, no matter how many times I read this, it really always enlighten me."

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

    elise "Hey Ray, sorry am late...."

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt001a', 'qt001b','qt001c'])

    show elise surprised

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
        ray "Your late!"
        show elise talk sad with dissolve
        elise "Yeah...just like I said I'm really sorry."
        show elise angry one
        elise "Also! you don't need to shout geeeshh...."
        ray "Well, I hope you remember the rules and the punishment to anyone whose late."
        jump section2

label qt001b:
        ray "Don't worry, I'm just only reading this to past time."
        show elise smile teeth
        elise "Okay...whatever you say, weirdo hahaha."
        ray "......."
        jump section2

label qt001c:
        ray "Well, this is a reminder to myself."
        show elise smile teeth
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

    zack "GENERAL!!!! The client’s accusation is real!!! I also already gathered some {color=#ff9900}evidences{/color} and {color=#ff9900}recorded the scene{/color}!!!!!!!" with vpunch

    zack "Go to the backside of the gym now!!! Hurry!!! before he do something bad to the client!!!"

    ray "I see, as always good work Major.Zack."

    zack "Ohh really thanks General hahaha!...wait...Please! just hurry up General."

    ray "Don't worry, we will arrive in the scene in no time."

    zack "YES SIR! See you soon."

    "{i}\"Ray stop the phone call.\"{\i}"

    hide phonecall
    hide phonecalla 
    with dissolve

    ray "Lieutenant.Elise! Get ready, we got a case to complete."

    show elise smile closed with dissolve

    elise "Okay! Just give me a sec."

    show elise angry one

    elise "Also! Like I told you don't call me Lieutenant! Geesh!"

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

    ray "How's the scene? Major.Zack."

    show zack happy close with dissolve

    zack "Finally both of you are here! Anyway look overthere!!"

    "{i}Ray and Elise look at the direction his pointing."

    play music "audio/suspense.ogg" fadein 0.5 fadeout 0.5 volume 0.5

    scene black
    with fade

    scene kenneth crime
    with fade

    $ renpy.pause(1.0, hard=True)

    voice "audio/kennethLine001.mp3"

    kenneth "Hehehe, Oh come on baby why are you playing so hard to get hehehe..."

    play sound "audio/breathe.mp3"

    "{i}\"Kenneth's breathe heavily through his mouth.\""

    stop sound

    ann "Noo!! Please just get away from me! Stop following me!!"

    voice "audio/kennethLine002.mp3"

    kenneth "Hehehe…Ohh come on, don’t you understand! How much I am really obsess to you. Hehehe..."

    voice "audio/kennethLine003.mp3"

    kenneth "I already giving you a lot of hints of how much I love you by {color=#ff0000}staring{/color} at you romantically."

    ann "Please anyone help me!!...."

    play music "audio/Time for Rest.ogg" fadein 0.5 fadeout 0.5 volume 0.5

    scene bg gym
    with fade

    ray "Hmmm….. it seems this man is really desperate."

    show zack happy opened with dissolve

    zack "Yeah he is also very creepy, we better give him the right punishment General."

    hide zack happy opened with dissolve

    show elise angry zero with dissolve

    elise "You two! What are you doing?!"

    show elise angry one 

    elise "Just step up to the scene already before this become more worst than it already is!"

    ray "A wise decision, Lieutenant.Elise. I commended you for thinking that."

    show elise angry one

    elise "Geesh!! Just do something already!!"

    play sound "audio/punch.ogg"

    "{i}\"Elise smack Ray's head." with vpunch

    stop sound

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
    ray "Hold it right there! belligerent scum!"
    jump section3

label qt002b:
    "{i}Ray approach the scene politely."
    ray "Hold it right there! crimi...GOOD SIR!"
    jump section3 

label section3:

    voice "audio/kennethLine004.mp3"

    show kenneth surprise with dissolve

    kenneth "Huhhh?!! How long have you been guys standing there!"

    ray "Hahaha....It seems you are not expecting anyone, Mr.Kenneth Dabert."

    voice "audio/kennethLine005.mp3"

    show kenneth scared opened

    kenneth "Huhhh?!! How do you know my name! Don...Don't tell me you guys are the student council officers!"

    ray "Hmm... Sorry to disappoint but no you are wrong about that."

    voice "audio/kennethLine006.mp3"

    show kenneth angry opened

    kenneth "Th-then just tell me who are you guys!!!"

    voice "audio/kennethLine007.mp3"

    show kenneth scared teeth

    kenneth "Also ho...how did you find us here! I am pretty sure no one is following us when we get here."

    ray "Hahaha!! As always, that’s Major.Zack for you. Despite being a airhead, he knowns the right ways to secretly sneak up to his target."

    ray "That’s why I always give you those assignments to secretly investigates potential suspects."

    hide kenneth scared teeth with dissolve
 
    show zack happy teeth with dissolve

    zack "Hahaha, thanks general."

    hide zack happy teeth with dissolve

    show elise talk confused with dissolve

    elise "Why are you even thanking that idiot, he just call you an airhead you know."

    hide elise talk confused with dissolve

    voice "audio/kennethLine008.mp3"

    show kenneth scared opened with dissolve

    kenneth "Sus-suspect!!! You sound like your saying I did something illegal eyy."

    voice "audio/kennethLine009.mp3"

    show kenneth angry teeth

    kenneth "Anyway just tell me! Who are you guys, suddenly treating me as a suspect. What a bunch of bronze players."

    ray "Well my humble apologies for our rudeness, Mr.Kenneth Dabert. I guess before we proceed on this case we should introduce ourselves first."

    ray "Well then Major.Zack, you may now proceed this introduction first."

    hide kenneth angry teeth with dissolve

    show zack talk asking with dissolve

    zack "Oh I need to introduce myself right?"

    show zack happy opened zorder 3

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

    ray "{i}{color=#00a62c}(\"Zack Ainsteak aka Major.Zack, from class 3-C. Despite being a airhead like I mention earlier.\"){/color}"

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

    ray "Thank you for that wonderful and yet simple introduction Major.Zack, Just like as I expected from you."

    show zack happy teeth

    zack "Hehehe thanks General."

    ray "Now Lieutenant.Elise, the stage is all yours."

    hide zack happy teeth with dissolve

    show elise angry zero with dissolve

    elise "Okay...fine..Also! How many times do I have to tell you stop calling me Lieutenant!"

    show elise angry one blushed
    elise "It’s really embarrassing you know... especially when there are other people around us!"

    show elise surprised

    elise "Ohh! Sorry about that!!... Okay let me introduce myself."

    show elise talk neutral zorder 3
    
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

    ray "{i}{color=#00a62c}(\"Elise Fonillia aka Lieutenant.Elise, from class 3-B.\"){/color}"

    ray "{i}{color=#00a62c}(\"Like many other people say “Don't judge a book by its cover” and that applies to Lieutenant.Elise.\"){/color}"

    ray "{i}{color=#00a62c}(\"She maybe look like a normal highschool student but don’t get fool by that.\"){/color}"

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

    ray "Thank you for that wonderful and elegant introductions Lieutenant.Elise."

    ray "Well then ladies and gentlemens, as for the next introduction will be next is....."

    show elise angry zero

    elise "....."

    hide elise angry zero with dissolve

    show zack happy opened with dissolve

    zack "Go General! Yahoo!!!"

    hide zack happy opened with dissolve

    # ! Ray image (optional)

    ray "The last but not the least.....The tactician, the strategist, the mastermind, and also the leader of the {color=#ff0000}HBB Club{/color}!!......"

    play sound "audio/punch.ogg"

    ray "It is I! General.Ray Zealsphere,from class 3-A! at your service!!...." with vpunch

    stop sound

    show zack happy opened with dissolve

    zack "OOHH YEAHH!! WUHH HOOO!!! GOO GENERAL!"

    hide zack happy opened with dissolve

    show elise angry zero with dissolve

    elise "How stupid...."

    ray "Come on don’t say that Lieutenant.Elise, I may be your General but I am still a human who has a sensitive feelings that can be easily shatter like a wine of glass."

    hide elise angry zero with dissolve

    voice "audio/kennethLine010.mp3"

    show kenneth laugh

    play sound "audio/punch.ogg"

    kenneth "HEHEHEHE!!! What the hell!!! HEHEHEHE!!!!..." with vpunch

    stop sound

    voice "audio/kennethLine011.mp3"

    show kenneth laugh

    kenneth "You guys are not the student council afterall!!! To be honest I almost got scared....but That's not a problem anymore! Hehehe!!!"

    ray "Hahahaha how foolish of you, we maybe not the student council officers of this school but we still have the right authorities to bring justice to your actions!!"

    ray "Also this student council that you afraid of... let just say that we the {color=#ff0000}HBB Club{/color} might have some connection to them."

    ray "So in case you want to say hello to them,  just ask.\nI could call them anytime you want, Mr.Kenneth Daberth."

    voice "audio/kennethLine012.mp3"

    show kenneth lie

    kenneth "Wha..What do you mean?! In the first place I did not do anything wrong!! Hehehe....that's right!"

    hide kenneth lie with dissolve

    show ann talking 

    play sound "audio/punch.ogg"

    ann "That's not true!!! Mr.Ray please help me!!! Everything I said yesterday with you guys is true." with vpunch

    stop sound

    ray "Don’t worry, dear client, we hear your humble words that’s why we're here to bring the truth and justice!"

    ray "Major.Zack! Bring me the document files!"

    hide ann talking with dissolve

    show zack happy teeth with dissolve

    zack "YES SIR!!!"

    play sound "audio/page.mp3"

    "{i}\"Zack's gave Ray a certain document file.\""

    stop sound

    ray "Hmmm I see, very intriguing I must say."

    voice "audio/kennethLine013.mp3"

    hide zack happy teeth with dissolve

    show kenneth scared teeth with dissolve

    kenneth "Wh-what is that document for huh?! Tell me, is it something to do with me right now HUH?!!!!"

    ray "Hold your horses Mr.Kenneth Dabert. Don't worry I will read this document out loud for you."

    play sound "audio/page.mp3"

    "\"Ray start reading the document.\""

    stop sound

    ray "Hmmm I see, Mr.Kenneth Daberth, from class 2-C. Yesterday at 5:27 PM, you got a accusation from this humble lady, she stated here that you been {color=#ff0000}staring{/color} and {color=#ff0000}stalking{/color} her lately."

    voice "audio/kennethLine014.mp3"

    show kenneth lie

    kenneth "Ah..Ahh well so what!!! It’s not like I did something illegal! Hehehe...."

    ray "Well sorry to disappoint you, but you did something illegal and violated a law."

    voice "audio/kennethLine015.mp3"

    show kenneth angry opened

    kenneth "Huu..Huh?! What are you even saying and what kind of law did I even violated in the first place!"

    ray "Mr.Kenneth Daberth, are you perhaps familiar to a law called Republic Act No......"

    ray "......Ahhh..........."

    ray "................................"

    voice "audio/kennethLine016.mp3"

    show kenneth angry teeth

    kenneth "Huh?! why are you suddenly become silent!!! Just tell me already!!!!"

    hide kenneth angry teeth with dissolve

    show elise surprised with dissolve

    elise "Hey Ray, don't tell me you just forgot the law that you almost always reading everyday!"

    ray "No! your mistaken Lieutenant.Elise, Am just trying to ahhh.... mediate! that right! To relax my mind."

    show elise angry three

    elise "Really I hope your not lying Ray... or else..."

    "Elise's clenched her fist intensely."

    ray "Hahaha....do...don't worry, I am done mediating now. I will now tell to Mr.Kenneth Daberth about what kind of law he violated."

    hide elise angry three with dissolve

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt003a','qt003b','qt003d'])

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
        ray "The name of the law that you violated is Re-semiprivate Act 12345!"
        show elise angry three with dissolve
        elise "Wait! Ray...are you serious, I told you that if your lying...."
        "{i}\"Elise's starting to raise her first.\""
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        show elise angry zero
        elise "......."
        hide elise angry zero with dissolve
        jump firstQuestion

label qt003b:
        ray "The name of the law that you violated is Reprivate Act 22244!"
        show elise angry three with dissolve
        elise "Wait! Ray...what you even saying, I told you if your lying...."
        "{i}\"Elise's starting to raise her first.\""
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        show elise angry zero
        elise "......."
        hide elise angry zero with dissolve
        jump firstQuestion

label qt003c:
        ray "The name of the law that you violated is {color=#ff0000}Republic Act 11313!{/color}"
        show elise smile teeth with dissolve
        elise "Haaa so your actually just messing around. Geeshh I almost planning to hit you in the face real hard if your actually lying."
        ray "{i}{color=#00a62c}(\".......well thank god I finally remember it.\"){/color}"
        hide elise smile teeth with dissolve
        jump section4

label qt003d:
        ray "The name of the law that you violated is Rebuild Act 11202!"
        show elise angry three with dissolve
        elise "Wait! Ray...are you even for real! I still remember the law that your trying to say, I told you if you lying...."
        "{i}\"Elise's starting to raise her first.\""
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        ray "{color=#00a62c}(\"Geesh...if you know the answer just say it.... No as the leader I should be the one to say this.\"){/color}"
        show elise angry zero
        elise "......."
        hide elise angry zero with dissolve
        jump firstQuestion

label section4:

    voice "audio/kennethLine017.mp3"

    show kenneth angry opened with dissolve

    kenneth "Republic Act 11369...ahh! Damn!! What does that law even mean!! Are you sure your not making this up!!"

    hide kenneth angry opened with dissolve

    show elise talk neutral with dissolve

    elise "Come on Ray, be more specific."
    
    hide elise talk neutral with dissolve

    show zack happy opened

    zack "You got this General!"

    hide zack happy opened with dissolve

    ray "O..Okay calm down everyone, I got this."

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt004a','qt004b','qt004d'])

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
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Place Act!"
    show zack talk confuse with dissolve
    zack "Really? I am pretty sure it sounds more like something to do with stars in the galaxy, General."
    ray "Ohh?! Am just joking! Hahaha!"
    hide zack talk confuse with dissolve
    show elise angry zero with dissolve
    elise "....."
    hide elise angry zero with dissolve
    show kenneth angry opened with dissolve
    kenneth "Just tell me already!!!" with vpunch
    hide kenneth angry opened
    jump secondQuestion

label qt004b:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Guard Act!"
    show zack talk confuse with dissolve
    zack "Safe Guard Act? Sounds like something I used to wash my hands after collecting some evidence, General."
    ray "Ohh?! Am just joking! Hahaha!"
    hide zack talk confuse with dissolve
    show elise angry zero with dissolve
    elise "....."
    hide elise angry zero with dissolve
    show kenneth angry opened with dissolve
    kenneth "Just tell me already!!!" with vpunch
    hide kenneth angry opened with dissolve
    jump secondQuestion

label qt004c:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Space Act!"
    show zack happy opened with dissolve
    zack "Yeah! That's right, {color=#ff0000}Safe Space Act{/color}! I really like the name of this law."
    ray "I also agree, Major.Zack."
    hide zack happy opened with dissolve
    jump section5

label qt004d:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Security Act!"
    show zack talk confuse with dissolve
    zack "Safe Security Act? Hmmm? General I feel like that's not the right name as far as I remember."
    ray "{color=#00a62c}(\"What! That's wrong! Am pretty sure that's the right name. I guess am the airhead, not Major.Zack.\"){/color}"
    ray "Am just joking! Hahaha!"
    hide zack talk confuse with dissolve
    show elise angry zero with dissolve
    elise "....."
    hide elise angry zero with dissolve
    show kenneth angry opened with dissolve
    kenneth "Just tell me already!!!" with vpunch
    hide kenneth angry opened with dissolve
    jump secondQuestion

label section5:

    show kenneth confuse with dissolve

    kenneth "Safe Space Act?"

    ray "It seems your not familiar about what is Safe Space Act, Mr.Kenneth Daberth."

    show kenneth angry opened

    kenneth "Hell if I know!"

    ray "Then if you please, let me enlighten you about what is this {color=#ff0000}Safe Space Act{/color} that am I speaking of."

    show kenneth lie

    kenneth "Hmph! Sure! Why not! It’s not like I..I di....did something wrong in the first place!! hehehe....."

    ray "Ohh am not sure about. Now then let me start to explain this to you, Good Sir."

    ray "{color=#ff0000}Republic Act 11313{/color} or also known as {color=#ff0000}Safe Space Act{/color}, is a law that has been approved by our president on {color=#ff0000}April 17,2019{/color}."

    ray "Well, according to this law it stated that {color=#ff0000}intrusive leering{/color} and {color=#ff0000}stalking{/color} is a violation to humans rights."

    show kenneth surprise
    
    kenneth "Wh...What the hell!!.. I had no idea...."

    ray "Now then, let me tell you the potential consequences that a guilty party have to face for anyone who violated this law."

    show kenneth scared teeth

    kenneth "...Co..Come ON! tell me! Afterall I didn't do anything wrong!"

    ray "Well, for the {color=#ff0000}first offenders{/color}, violating this law could punish you by a 1000 pesos fine."

    show kenneth surprise

    kenneth "What?! you serious bruh?! I can buy a lot of skins in-game with that money!"

    ray "Also a community service of twelve hours inclusive of attendance to a Gender Sensitivity Seminar to be conducted by the PNP in coordination with the LGU and the PCW."

    show kenneth scared opened

    kenneth "What?! community service! like I have time for that!"

    ray "Ohh, Also don't get me wrong this punishment I mentions is just for doing violation acts like {color=#ff0000}intrusive learing{/color}..."

    ray "...while the case of doing things like {color=#ff0000}stalking{/color} to someone has more hasher punishment compare to this one like I mention ealier."

    show kenneth scared teeth

    kenneth "!!!!!"

    ray "Hmmm.... it seems you finally have some grasp about what is this law called Safe Space Act."

    ray "Also as I reminder I only mention the punishment for the first offenders, Mr.Kenneth Daberth."

    ray "I wonder what will happen more if you violated this law more, well I only guarantine you that it will be of course become much more worse."

    show kenneth serious

    kenneth "........."

    kenneth "................"

    kenneth "......................."

    ray "Hmmm? Mr.Kenneth Daberth, are you feeling well right now? It seems you need medical assistance right now."

    show kenneth serious laugh

    kenneth ".....heheh...hehhehe....heheheh.....HEHEHEHEHE!!!!!"

    show kenneth laugh crazy

    kenneth "HEHEHEHE!!! WHERE IS YOUR EVIDENCE THAT I DID THOSE THINGS TO THIS UGLY WOMAN????!!!"

    hide kenneth laugh crazy with dissolve

    show ann terrified with dissolve

    ann "!!!!" with vpunch

    hide ann terrified with dissolve

    show kenneth laugh crazy with dissolve

    kenneth "THIS UGLY WOMAN ACCUSATION IS NOT ENOUGH TO PROVE THAT I REALLY DID THOSE THINGS TO HER!!"

    ray "Well, that’s true Mr.Kenneth Daberth."

    show kenneth laugh crazy

    kenneth "GOOD! This is stupid am leaving! Hehehehe...\n{color=#00a62c}(\"GG EZ...hehe...I guess I should go home and play a one match of PoP to forget what happen here. Hehe...\""

    hide kenneth laugh crazy with dissolve

    "{i}Kenneth Daberth nervously leave the scene slowly.{/i}"

    show zack talk surprise with dissolve

    zack "Ahh! His leaving General..."

    hide zack talk surprise with dissolve

    play sound "audio/punch.ogg"

    ray "Hold up! Mr.Kenneth Daberth! You may have the right to remain silent but we have the EVIDENCE! that can prove to you that your not innocent!" with vpunch

    ray "So are you quite sure you wanna leave right now, or else maybe tomorrow the Student Council might have give you a visit."

    show kenneth angry teeth with dissolve

    kenneth "!!!!" with vpunch

    hide kenneth angry teeth with dissolve

    show zack surprise opened with dissolve

    zack "Wait really!!! We have the evidence General?!!!"

    hide zack surprise opened with dissolve

    show elise angry zero with dissolve

    elise "......"

    hide elise angry zero with dissolve

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

    zack "Oh yeah your right General! I finally remember, I did in fact gathered some evidences earlier...."

    show zack talk confuse

    zack "...but....General....."

    ray "But what? Major.Zack."

    show zack talk confuse

    zack "Well General....its true that I did in fact collected some evidences earlier which is currently right now inside my evidence pouch archive....."

    ray "Hahaha, That's good to know Major.Zack, you are really doing your job properly. I respect that."

    show zack talk worried

    zack "Haha.. Thanks General, but the my problem right now is that I don't know which evidence you want me to present right now."

    ray "It’s fine Major.Zack, that’s one of your flaws but I understand. So don’t be nervous right now, but instead be rest assured because I got you covered."

    ray "Afterall, if your job is to spy and find evidences. Then my job is to used those information you gathered to show them and reveal to them the truth and justice."

    show zack happy opened

    zack "Wow, that's awesome General!"

    hide zack happy opened with dissolve

    show elise talk confused with dissolve

    elise "Haaaa....You guys are really hopeless....Ray are you really sure that Zack really do have the evidence for this case?"

    ray "Hoo? Don't worry Lieutenant.Elise, soon you will get your moment to shine."

    show elise angry one

    elise "Haa?!!...That's not what am worried for, idiot."

    hide elise angry one with dissolve

    show kenneth angry teeth with dissolve

    play sound "audio/punch.ogg"

    kenneth "HEY!! YOU GUYS STOP FOOLING AROUND!! JUST SHOW ME THAT EVIDENCE YOUR TALKING ABOUT!!" with vpunch

    hide kenneth angry teeth with dissolve

    show zack happy opened with dissolve

    zack "General! Hurry! What evidence you want me to present?!"

    ray "Well then, I will tell you the evidence that will prove that Mr.Kenneth Daberth did in fact is not innocent!"

    hide zack happy opened with dissolve

    show kenneth angry opened with dissolve

    kenneth "COME ON SHOW ME!!!"

    hide kenneth angry opened with dissolve

    ray "Major.Zack, show me all the evidences that you manage to gathered!"

    show zack happy teeth with dissolve

    zack "Yes SIR!!!"

    hide zack happy teeth with dissolve

    "{i}\"Zack shows you all the evidence he gathered.\""

    ray "{color=#00a62c}(\"Haha...as always Major.Zack. Some of the things here are not even could be consider as evidence for this case. Most of them are just trash!\"){/color}"

    ray "{color=#00a62c}(\"Well okay then, Time to show the culprit the evidences!\"){/color}"

label evidence:
    
    $timeout = 10
    $timeout_label = renpy.random.choice(['ed001a', 'ed001b','ed001c'])

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
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}BANANA PEEL{/color}!!!"
    show kenneth laugh with dissolve
    play sound "audio/punch.ogg"
    kenneth "BANANA PEEL?! HAHAHA!! HOW CAN A BANANA PEEL PROVE THAT AM NOT INNOCENT EYY!!! STUPID BRONZE PLAYER!!!" with vpunch
    hide kenneth laugh with dissolve
    show elise angry three with dissolve
    elise "Hey! Are you trying to mess with me huh?! RAY!!"
    ray "No..Noo am just showing the banana peel, afterall it look kinda delicious! But too bad it looks like someone already ate it."
    show elise angrier zero with dissolve
    elise "....."
    hide elise angrier zero with dissolve
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001b:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}CANDY WRAPPER{/color}!!!"
    show kenneth scared opened with dissolve
    kenneth "A CANDY WRAPPER YOU SAY! How..NOOO I DIDN\'T SHOPLIFTED ANY CANDIES EARLIER OKAY!!!"
    hide kenneth scared opened with dissolve
    show elise angry one with dissolve
    elise "Hey! What the are you doing?! Show the evidence already!"
    ray "Hahaha...I am just joking this time, Now I will show you the real evidence."
    show elise angry zero
    elise "......"
    hide elise angry zero with dissolve
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001c:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}LEAF{/color}!!!"
    show kenneth scared opened with dissolve
    kenneth "NO!! YOUR WRONG! I DON\'T SMOKE WEE...I MEAN LEAF!!!"
    hide kenneth scared opened with dissolve
    show zack happy opened with dissolve
    zack "AHA! General! This guy is a drug user!!!"
    ray "Hahaha...I don't think so Major.Zack."
    show zack happy teeth
    zack "Ohh your just joking again right General, Hahahaha."
    hide zack happy teeth with dissolve
    show elise angry zero with dissolve
    elise "......"
    hide elise angry zero with dissolve
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001d:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this! {color=#ff9900}MAJOR.ZACK'S PHONE{/color}!!!"
    show zack surprise opened with dissolve
    zack "What! Ohhh yeah... I almost forgot I recorded some scene when this criminal is doing some bad things to our client earlier General."
    hide zack surprise opened with dissolve
    show elise angry one with dissolve
    elise "Huh?! Are you even serious, Zack. Why did you not just stop this creep already when he doing some bad things to our client."
    hide elise angry one with dissolve
    show zack talk confuse with dissolve
    zack "Ahh! Well I think its for the best to gathered some evidence instead because even if I tell this criminal to stop he won't listen to me I think...."
    show zack happy teeth
    zack "Also am pretty sure that even I managed to stop him, he will just find another moment again to do some bad things again to our client. So I guess its better to follow the General's Order."
    hide zack talk confuse with dissolve
    show elise angry three with dissolve
    elise "HUH?! Your kidding right! Do you even call yourself a man!"
    hide elise angry three with dissolve
    show zack talk worried with dissolve
    zack "I am really sorry! I guess I should stop him before even I don't have the strenght like a goril...." 
    play sound "audio/punch.ogg"
    ray "SILENT!! Major.Zack!" with vpunch
    ray "I....I understand what your trying to say, Major Zack. But sometimes, there are times you really need to step up to the scene before its to late, remember this, Major Zack."
    show zack happy opened
    zack "Wow, that sounds amazing, okay copy that General! I will take a note about this."
    hide zack happy opened with dissolve
    show elise angry one with dissolve
    elise "....don't have the strenght like a goril..what are you even trying to say Zack, could you just say it again this idiot suddenly interrupted you."
    play sound "audio/punch.ogg"
    ray "THAT'S! enough for talk now Lieutenant.Elise. We still need to prove why Zack's Phone is the reason why Mr.Kenneth Daberth is guilty." with vpunch
    show elise angry zero
    elise "....."
    hide elise angry zero with dissolve
    jump section6

label section6:

    show kenneth scared opened with dissolve

    kenneth "YEAH! YOU GUYS STOP FOOLING AROUND ALREADY! WHY IS THAT PHONE IS THE EVIDENCES EYY?!! I STILL HAVE A DATE TO ATTEND SOON!! HURRY UP!!!"

    ray "Sorry about that Mr.Kenneth Daberth I guess you have to cancel that date, though I highly doubt it."

    ray "Well the reason why Zack's Phone is the evidence that will prove you guilty is already obvious."

    ray "And I am pretty sure you already know it."

    show kenneth lie
 
    kenneth "!!!!...NO I DON'T KNOW!!! Heheee...."

    ray "Okay, then let's ask Major.Zack."

    hide kenneth lie with dissolve

    show zack happy close with dissolve

    zack "Need something? General."

    ray "Let me ask you, do you remember the phone call we had ealier. Do remember that you mention that you recorded the some scene right."

    show zack talk surprise

    zack "Yes General, I recorded him lately for evidence while this criminal has been desperately {color=#ff0000}stalking{/color} and {color=#ff0000}staring{/color} the client, General."

    ray "Okay then, please play that video Major Zack."

    show zack happy opened

    zack "YES SIR!!!"

    show zack talk confuse

    zack "Hmm... Let's see where did I save that video file again?"

    ray "......Haha...ha...Please take your time Major Zack."

    hide zack talk confuse with dissolve

    show elise talk sad with dissolve

    elise "Ray....just like I expected, both of you guys are hopeless....."

    ray "Oh come on now Lieutenant.Elise, le....let's just wait and trust Major.Zack okay....."

    hide elise talk sad with dissolve

    ray "{color=#00a62c}(\"This is starting to make me nervous....\")"

    show kenneth scared opened with dissolve

    play sound "audio/punch.ogg"

    kenneth "HEY HURRY UP!!!!" with vpunch

    hide kenneth scared opened with dissolve

    stop sound

    show zack happy opened with dissolve

    zack "OH!!! Found it! Phew I though I lost it but it just got mix up to other old videos that also recorded for evidence. Hahaha, okay let me play the video now."

    hide zack happy opened with dissolve

    "{i}\"Zack play the video he recorded on his phone.\""

    # !Important ~ Add a image of Kenneth Daberth stalking and staring activities.

    show kenneth angry teeth with dissolve

    play sound "audio/punch.ogg"

    kenneth "NOOO!! BUT HOW?! I AM REALLY PRETTY SURE NO ONE IS AROUND US." with vpunch

    stop sound

    ray "Hahahahah, as always good work Major.Zack, not even the slightless I doubt your work. {color=#00a62c}(\"Phew...thank god, He actually managed to record a scene for evidence.\"){/color}"

    hide kenneth angry teeth with dissolve

    show zack happy teeth with dissolve

    zack "Thank you GENERAL!!!"

    hide zack happy teeth with dissolve

    ray "Well are you satisfied now Mr.Kenneth Daberth or will you still deny your actions. If that's the case then am telling you this will only become much more worse for you, Good Sir."

    ray "Hmm??"

    show kenneth serious with dissolve

    kenneth "............"

    kenneth "Hooo...Hooyoyoyoyoyo..........."

    show kenneth scared opened

    play sound "audio/punch.ogg"
    
    kenneth "This is BAD!!!!!! MY MOTHER WILL SPANK MY ASS AT THIS RATE IF SHE FOUND OUT WHAT I DID!!!" with vpunch

    stop sound

    hide kenneth scared opened with dissolve

    show elise smile teeth with dissolve

    elise "Hahahahaha...."

    show elise surprised

    elise "Ahh! Sorry about that....."

    hide elise surprised with dissolve

    ray ".........."

    ray "Mr.Kenneth Daberth, based on the investigation and evidence it seems the verdict is clear. I guess it's about time to wrap this thing up."

    show ann relief with dissolve

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
    ray "Mr.Kenneth Daberth, YOU ARE FOUND GUILTY!!! The court is now adjourned."
    show kenneth surprise with dissolve
    play sound "audio/punch.ogg"
    kenneth "NOOO!!!!!!" with vpunch  
    stop sound  
    hide kenneth surprise with dissolve
    jump section7

label qt005b:
    ray "Mr.Kenneth Daberth, congratulation you won the case. You are found innocent. The court is now adjourned."
    show kenneth scared opened with dissolve
    kenneth "WHAT!! REALLY!!!...I thought am busted already....."
    hide kenneth scared opened with dissolve
    show elise angrier three with dissolve
    play sound "audio/punch.ogg"
    elise "RAY!!!! STOP JOKING AROUND!!! ARE YOU REALLY GONNA LET A CRIMINAL ESCAPE!!!!" with vpunch
    stop sound
    play sound "audio/punch.ogg"
    "{i}Elise smack Ray's head.{/i}" with vpunch
    stop sound
    ray "AWWW!!! I'M SORRY!! OKAY!! OKAYY!! THIS TIME I WILL NOT MESS AROUND!!!"
    ray "{color=#00a62c}(\"Okay....No more messing around this time I will tell the truth.\")"
    hide elise angrier three with dissolve
    jump verdict

label section7:

    ray "And lastly, this case is COM!!...."

    show zack surprise opened with dissolve 

    play sound "audio/punch.ogg"

    zack "WAIT!!! General!!!!!! The suspect is escaping!!!!!!!" with vpunch

    stop sound

    hide zack surprise opened with dissolve 

    play sound "audio/footsteps.mp3"

    "{i}\"Kenneth Daberth quickly tries to escape the scene.\"{/i}"

    stop sound

    ray "Ahhh! Right when I finally able to say my favorite line!!! This man deserve a harsh punishment!!! Lieutenant Elise, requesting for back-up!"

    show elise talk confused with dissolve

    elise "Geeshh! Am already here what are you even talking about."

    show elise talk neutral

    elise "Anyway, I got this. Zack give me that {color=#ff9900}Banana Peel{/color} in your evidence pouch or whatever you called that bag is."

    hide elise talk neutral with dissolve

    show zack happy teeth with dissolve

    zack "YES MAAM!"

    hide zack happy teeth with dissolve

    show kenneth scared teeth with dissolve

    kenneth "I BETTER RUN FAST!!!!, IMAGINE!!! IMAGINE IT!!! LIKE AM USING THE SKILL FLASHSTEPPPP LIKE IN THE GAME of PoP!!!!"

    show kenneth laugh crazy

    kenneth "HEEHEHEHEH!!!!!!! I CAN FEEL IT!!!! I AM RUNNING SO FAST YAHOO!!!!! I WILL ESCAPE THIS IN NO TIME!!!"

    hide kenneth laugh crazy with dissolve

    show zack talk surprise with dissolve

    zack "Wow...his really fast!!!"

    ray "Hmm...his already about approximately 28 meters away from us."

    hide zack talk surprise with dissolve

    show elise smile teeth with dissolve

    elise "Don't worry I got this, Even if his already in the other side of the planet I can still throw this {color=#ff9900}Banana Peel{/color} right in front of his feet to lose his balance."

    ray "Hahahaha! True, I never doubt your strenght Lieutenant.Elise. Afterall, you have more strenght than a 6-footer gorilla. AHH!"

    hide elise smile teeth with dissolve

    ray "{color=#00a62c}(\".....di..did I say it out loud. I hope she did not heared me just now......\"){/color}"

    show elise angry one with dissolve

    elise "TAKE THIS!!!!!!"

    hide elise angry one with dissolve

    show kenneth defeat with dissolve

    kenneth "AWWWW MAMA DON’T HIT MEE!!!!!"

    hide kenneth defeat with dissolve

    ray "It seems the culprit is already experiencing the punishment he deserved for his actions."

    ray "I guess the time has come."

    show zack happy teeth with dissolve

    zack "YES SIR!"

    hide zack happy teeth with dissolve

    show elise angry zero with dissolve

    elise "......."

    hide elise angry zero with dissolve

    play sound "audio/punch.ogg"

    ray "THIS CASE IS COMPLETE!!{color=#00a62c}(\"Yeah finally hahaha...\"){/color}" with vpunch

    stop sound

    show ann happy with dissolve

    ann "Ahh excuse meee....ahh Mr.Ray and everyone, thank you very much for helping me."

    ray "No worries, it’s our duty to help our people, right everyone?"

    hide ann happy with dissolve

    show zack happy teeth with dissolve

    zack "YES SIR!!"

    hide zack happy teeth with dissolve

    show elise angrier zero with dissolve

    elise "......."

    elise "..........."

    elise "................"

    ray "Ah...Ahhh......Lieutenant.Elise? Somethings wrong? You seems awfully quiet.... are you perhaps already hungry?"

    show elise angrier one

    elise "Ray.... how many times do I have to tell you don't call me Lieutenant, but still you won't listen and NOW!!!..."

    ray "heyy....calm down...."

    show elise angrier three

    elise "AND NOW! You just compare me to a GO...GOO...GORILLA!!!!"

    ray "ohhh….ohhhhh come on Lieutenant.Elise, I am just joking you know."

    ray "Af...Afterall.....a leader must also show his humor sometimes to his subordinates right? right Major.Zack?"

    hide elise angrier three with dissolve

    show zack happy teeth with dissolve

    zack "YES SIR!!!"

    ray "Is that the only thing you can say right now!! At least say something else, I save your sorry ass earlier you know."

    show zack happy teeth

    zack "YES SIR!!!! Thank you very much for saving me even though I don't remember it!!!"

    hide zack happy teeth with dissolve

    show elise angrier three with dissolve

    elise "......"

    hide elise angrier three with dissolve

    show ann relief with dissolve

    ann "Ahh excuse me.....to be honest looks like Mr.Ray also need to get punished for verbally abusing Miss.Elise."

    ray "WH..WHAT I JUST HELP YOU! YOU KNOW! ATLEAST SHOW SOME GRATITUDE!"

    show ann terrified

    ann "sor..Sorry!!!....Please don't hit me!!!"

    hide ann terrified with dissolve

    show elise angrier three with dissolve

    elise "....RAAYY!!!!"

    hide elise angrier three with dissolve

    "{i}\"Elise slowly approach Ray intensely.\""

    show elise angrier three with dissolve

    ray "Hey calm down Lieutenant.Elise! Anyone please help or alteast somebody stop her!! CALL THE ANIMAL CONTROL DEPARTMENT!! PLEASE!!! AHHHHH!!!"

    hide elise angrier three with dissolve

    "{i}\"And on that day, all the students heard a short loud scream throughout the campus.\""

    ray "AH!.................................................."

    "{i}\"And that's the only beginning of the HBB Club story.\""

    scene black
    with fade

    centered "END...."

    # This ends the game.

    $ bonusScript = False

    return
