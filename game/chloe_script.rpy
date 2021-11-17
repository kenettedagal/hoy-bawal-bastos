 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main Character
define me = Character('Menard')
define c = Character('Chloe')
define tr = Character('Tristan')

# Side Character
define d = Character('Driver')
define o = Character('Old Man')
define pm = Character('Police Man')
define sg = Character('School Guard')

label chloe:

    $ yuiStoryProgress = 3
    show screen showNotesButton

    $ hbbpoints = 0
    show screen displayHBBPoints

    image polices station = im.Scale("images/police station.jpg", 1920, 1080)
    image school2 = im.Scale("images/school gate2.png", 1920, 1080)

scene bg train morning
play music "audio/music/Careless-Summer_Looping.mp3"

"You and Chloe waiting to arrive Tristan in the train station"
"After a minute Tristan arrive at the train station"

show tristan smile close at left with dissolve
tr "Sorry I’m late Guys!"
hide tristan
show chloe happy  with dissolve
c "it’s okay, let’s ride the train now"
hide chloe
show you shout at right with dissolve
me "hurry up were going to be late."

label train:
scene bg train

"Inside of the Train"
show tristan smile at left with dissolve
tr "Hays, the train are all ready crowded…"
hide tristan
show chloe smile at right with dissolve
c "there’s  no available set, we should wait for another train.."
hide chloe
show you happy at left with dissolve
me "but it's been an hour before the another train come, "
show you happy at left with dissolve
me "and were going to be late if were going to wait for the another train.."
hide you
show chloe smile at right with dissolve
c "your right…"
scene bg train

"After a minute an old guy, ride the bus but it’s still no vacant set, the old guy stand behind to Chloe"
show old man smile at left with dissolve
o "........"
show chloe scared at right with dissolve
c "hmmm (someone touch my butt…)"


"but the old guy look away when Chloe look to him and the old guy touche again Chloe’s butt"
show old man smile at left with dissolve
show chloe cry at right with dissolve
hide chloe
c "Tristan,[me], the old guy behind us touch my butt again...."

menu:

    "[me] and [tr] punch the old guy.":
        jump beat
        $ hbbpoints -=1
        show screen displayHBBPoints

        #block of code to run
    "you and tristan call the attention of the bus driver.":
        jump efas
        $ hbbpoints +=2
        show screen displayHBBPoints
        #block of code to run

label beat:
    play music "audio/music/Fight.ogg"
    show you angry with dissolve
    show tristan angry at right with dissolve
"You and Tristan have black eye from the punch of the old guy"
pause
play music "audio/music/Relax.ogg"
label efas:
    hide old man
    show you angry at left with dissolve
    me "excuse everyone the old guy touch my friend butt"
    hide you
    show tristan angry at right with dissolve
    tr "please call the driver or any crew of the train..."
    show driver yan at left with dissolve
    d "yes sir.."
    hide driver
    show you angry at left with dissolve
    me "this old man are pervert"
    me "he touch my friend butt"

"The driver help you to drop the old guy in the police station to report the incidence."

label pstaion:

scene polices station

"the three of you will report on what happen in the train to the police station"

show police_man at left with dissolve
pm "so what happen in the train?"
hide police_man
show you angry at right with dissolve
me "the old man touch my friend butt!!"
show old man smile at left with dissolve
hide old man
o "...sorry"
show police_man at left with dissolve
pm "kid calm down"
pm "i got you kid.."
pm "i have question to you guys, okay..."

menu:

    pm "are you guys know about the bawal bastos law?"
    "no....":
        $ hbbpoints +=1
        show screen displayHBBPoints
        jump explanation
        #block of code to run
    "yes....":
        $ hbbpoints +=3
        show screen displayHBBPoints
        jump youAnsweer
        #block of code to run

label explanation:
    show police_man at left with dissolve
    pm "it is Republic Act No. 11313 or also known as Safe Space Act"
    pm "AN ACT DEFINING GENDER-BASED SEXUAL HARASSMENT IN STREETS, PUBLIC SPACES, ONLINE, WORKPLACES,"
    pm "AND EDUCATIONAL OR TRAINING INSTITUTIONS, PROVIDING PROTECTIVE MEASURES AND PRESCRIBING PENALTIES THEREFOR"

    jump hurry
label youAnsweer:
    hide police_man
    show you happy at left with dissolve
    me "ahh it is a the Republic Act No. 11313 or also known as Safe Space Act"
    me "AN ACT DEFINING GENDER-BASED SEXUAL HARASSMENT IN STREETS, PUBLIC SPACES, ONLINE, WORKPLACES,"
    me "AND EDUCATIONAL OR TRAINING INSTITUTIONS, PROVIDING PROTECTIVE MEASURES AND PRESCRIBING PENALTIES THEREFOR"
    hide you
    show police_man at left with dissolve
    pm "your right yuong man.."
    pm "Safe Space Act are the right law for what happen in the train"
    hide police_man
    show tristan smile at right with dissolve
    tr "how do you know about this law?"
    hide tristan
    show you happy at left with dissolve
    me "i love reading book and news...."
    jump yieee
label hurry:
    hide police_man
    show you smile at left with dissolve
    me "ahh thank you for new information sir..."
    show chloe smile at right with dissolve
    c "now i know my rights now..."
    c "also everyone rights.."
    jump yieee
label yieee:

    show tristan smile close at left with dissolve
tr "ohh okay, but thank to you [me] now i know this law..."
tr "but guys hehe..."
tr "guys...."
tr "guys..."
tr "guys we need to hurry were going to be late…"
hide tristan

show police_man at right with dissolve
pm "Guys here the copy of the report on what happen today you can pass this to the school so you three can still enter to the school…"
hide police_man
show you happy at left with dissolve
me "Thank you sir.."
hide you
show chloe happy at right with dissolve
c "Thank you so much sir…"
hide chloe
show police_man at left with dissolve
pm "welcome..."

label school:

scene school2
"after a minute you three arrive in the school"
show school guard at right with dissolve
sg "why are you late?"
show tristan smile at left with dissolve
tr "we get involved in trouble in the train hehe.."
show school guard at right with dissolve
sg "oh I see.. before i let you in i have question.."
show you smile at left with dissolve
me "what if we did not answer correctly your question?"
show school guard at right with dissolve
sg "i still let you in hehe..."
sg "this is the question..."
menu:

    sg "what is the other term of bawal bastos law?"

    "Space safe act":
        "wrong answer"
        $  firstTryWrong = True
        jump ewww
        #block of code to run
    "safe safe act":
        "wrong answer"
        $ firstTryWrong = True
        jump ewww
        #block of code to run
    "safe space act":
        "correct!.."
        $ hbbpoints +=5
        show screen displayHBBPoints


        jump ewww
label ewww:
show school guard at right with dissolve
sg "okay you can come in now"
sg "and don't forget to tell your teachers on what happen so you tree are excuse.."
show you smile at left with dissolve
me "Yes sir.."
