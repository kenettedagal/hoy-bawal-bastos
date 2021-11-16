# The script of the game goes in this file.
# Main Character


# Side Character
define natalie = Character("Natalie",color='#d684ad')
define bob = Character("Bob",color='#a6e0a1')
define sg = Character("Strange guy",color='#bbdda8')
define gd = Character("Guard",color='#866bb8')
define tsci = Character("Teacher Johnny",color='#e0d397')
define m = Character("Me",color='#00ffea')
define mc = Character("Mark")
define u = Character("Unknown guy")

default badending1 = False
default mending = True
default gending = False

# Script starts here.
label Act_2_School:

stop music


scene black

play sound "audio/sfx/doorcreak.wav"

centered ""

stop sound

scene bg classroom_01_day
$hbbpoints +=5
show screen displayHBBPoints

m "Oh, no one's here yet. I guess I'm too early."

play sound "audio/sfx/yawn.wav" fadeout 1.0

m "I should take a quick nap."

stop sound
scene black

#play sound "audio/hey"
show unknown worried with dissolve
u "Wake up,hey wake up. Class will be starting in a minute."
#hbb points lagay
menu ask1:

        "Continue sleeping":

                $ subtractPoints()
                jump class1
        "Wake up":

                $ hbbpoints += 3
                show screen displayHBBPoints
                jump class2



label class1:
        
        scene bg classroom_01_day

        
        m "............."
        show johnny angry
        tsci "The class has already started, if you want to sleep feel free to leave this room."
        
        show johnny poker
        m "I'm sorry miss it won't happen again."
        hide johnny poker
        scene black
        centered "Few Hours later."

        pause 1.0

jump lunchbreak

label class2:

        scene bg classroom_01_day
                
        m "Ah the class is starting."

        show johnny poker
        tsci "Good morning everyone, we will begin our class but first of all let's get your attendance."
        hide johnny poker
        scene black
        centered "Few Hours later."

        pause 1.0

jump lunchbreak

label lunchbreak:

scene classroom lunch1

play sound "audio/sfx/bell.mp3"

show johnny happy
tsci "Ok class dismiss,don't forget your activity for the next meeting."


tsci "Also remember to cooperate with your members."


scene bg cafeteria

play music "audio/music/Careless-Summer_Looping.mp3" fadein 3.0


show bob talk with dissolve
bob "Ah my head hurts, I can't keep up with the lessons."

scene black
show bob happy with dissolve
mc "This is [bob]. My friend in my first year here"

mc "He's an athlete person being pursuaded by multiple sports club"

mc "But the guy is lazy and not serious most of the time"

mc "Well... he's still a good and reliable person"

scene bg cafeteria

show kurtney talk opened at left with dissolve
kk "That's what you always say when your studying."

show bob talk at right with dissolve
bob "But the given group activity is kinda hard."

show kurtney happy teeth at left with dissolve
kk "Yes,it will be hard for the group your joining."

show bob shock at right with dissolve
bob "What do you mean by that.I won't burden to my group."
bob "Right?"

menu ask2:

        "Hmmm..."
        "Agree":
        #block of code to run

                $ hbbpoints += 4
                show screen displayHBBPoints
                m "Yes, I'm glad that your part of my group."
                show bob talk at right with dissolve
                bob "See? I told you."
                show kurtney angry talk at left with dissolve
                kk "What your part of Bob's group!? Dude I want to be in your group."
                
                jump Act2

        "Neutral":
        #block of code to run
                $ subtractPoints()
                show screen displayHBBPoints
                m "Well your neither the best nor the worst."
                show bob sad at right with dissolve
                bob "Why do I feel like your insulting me."
                show kurtney talk opened at left with dissolve
                kk "It's because your lazy and only do financial support."
                show bob talk at right with dissolve
                bob "I also do moral support those two are enough."
                show kurtney angry talk at left with dissolve
                kk "No, it's still not enough."

                jump Act2
    
label Act2:

hide kurtney angry talk
show natalie talk at left with dissolve
natalie "H-hello your [mc] right?"

m "Yes I am,what is it?"

show bob happy at right with dissolve
bob "Ho,Hello there cutie."

show natalie talk at left with dissolve
natalie "Oo-oh he-hello."

show bob talk at right with dissolve
bob "You're new here? Come join here eat with us."

play sound "audio/sfx/punch.wav"

show bob shock at right with dissolve
bob "Aw, what's wrong your with you?"

hide natalie talk
show kurtney angry talk at left with dissolve
kk "Stop hitting with all the girls in the school,dude!"

show bob talk at right with dissolve
bob "I'm just asking her to join us."

m "Don't mind them, Is there something you want?"

hide kurtney angry talk
show natalie talk at left with dissolve
natalie "Ummm..."

bob "Speak up don't be shy."

natalie "A-aabout t-the..."

hide natalie talk
show kurtney talk opened at left with dissolve
kk "Hey are you ok?"

hide kurtney talk opened
show natalie talk at left with dissolve
natalie "Y-yyees"

show bob happy at right with dissolve
bob "Ah! just give the letter he'll read it."

play sound "audio/sfx/punch.wav"
"BONK!" with vpunch
show bob shock at right with dissolve
bob "Aw! could you please stop hitting mc?"

hide natalie talk
show kurtney angry talk at left with dissolve
kk "Seriously?"

show bob sad at right with dissolve
bob "I'm just kidding man."

hide kurtney angry talk
show natalie talk at left with dissolve
natalie "Aa-about the group..."

show bob talk at right with dissolve
bob "Oh if you want us to be your friends, sure no problem."

m "Yes, he's right feel free to talk to us."

hide natalie talk
show kurtney talk opened at left with dissolve
kk "I think she's trying to tell that she's part of your group activity."

hide kurtney talk opened
show natalie talk at left with dissolve
natalie "Yes..."

hide natalie talk
show kurtney talk opened at left with dissolve
kk "She's the tranferee."

show bob shock at right with dissolve
bob "[natalie]? Oh the new girl in our class!"

m "Now that I think about it"

scene black

show natalie happy at center with dissolve
"[natalie] a new female student in our class. A tranferee in the middle of prelims."
"I don't know anything about her,well... guess she's a shy person."

scene bg cafeteria

show natalie talk at left with dissolve
show bob poker at right with dissolve

m "About the group activity. Why don't be talk about it after school?"
show bob talk at right with dissolve
bob "Right, we can go to the foodcourt in the mall."
show  natalie talk at left with dissolve
natalie "O-ook."
m "It's decided then see you later!"

stop music

label Act_2_School_Chapter2:

scene school gate

m "It seems I'm the first one here."


natalie "....."

m "Looks to the side"

show natalie poker with dissolve

m "Oh, you're here."

show natalie talk with dissolve
natalie "So-sorry for being late."

m "You're not late and were still waiting for [bob]."

show natalie poker with dissolve
natalie "....."

m "....."

m "(This is bad. It might get awkward here until [bob] comes, what should I do?)"

menu ask3:
        
        "Talk to her":
                #block of code to run
                $ hbbpoints += 4
                jump Act_2_School_1
        "Keep Silent":
                #block of code to run
                jump Act_2_School_2

label Act_2_School_1:        

scene school gate

m "The weather is nice today."

show natalie talk at left with dissolve
natalie "Yes and the wearther report says to be sunny and not expect to rain."

m "It seems you watch a lot of weather forecast."

show natalie happy at left with dissolve
natalie "I do like seeing the weather forecast."

m "Is there something you like other than that?"

show natalie talk at left with dissolve
natalie "I like to read books and p-play some video games."

m "Oh really?! That's awesome, is there something you recommend to read?"

show bob talk at right with dissolve
bob "Heyoo, Sorry for being late the match took longer than I expected."

m "Ok now that everyones here.Are we ready to go?"

show bob happy at right with dissolve
bob "Yep, I'm ready."

show natalie at left with dissolve
natalie "I'm good to go."

jump Act_3_Mall


label Act_2_School_2:

$ subtractPoints()

scene school gate

"You waited [bob] in silence"

show bob talk at right with dissolve
bob "Heyoo, Sorry for being late the match took longer than I expected."

m "Ok now that everyones here.Are we ready to go?"

show bob happy at right with dissolve
bob "Yep, I'm ready."

show natalie poker at left with dissolve
natalie "....."

scene black

pause 1.0


jump Act_3_Mall


label Act_3_Mall:


scene mallwalk_d

show bob talk
bob "We're here. Are we going to buy materials or we eat first?"

menu:

        "Buy materials":
                #block of code to run
                jump Act_3_Mall1
        "Eat first":
                #block of code to run
                jump Act_3_Mall2

label Act_3_Mall1:


scene mallwalk_d

m "We should buy materials first."

bob "Ok let's go to the store."

centered "You guys bought the things you need."

jump Act_3_Mall3

label Act_3_Mall2:


scene mallwalk_d

m "We shoud go and eat first."

bob "Ok let's go and eat then"


jump Act_3_Mall3


label Act_3_Mall3:

scene cafe_memoria_inside_01_afternoon with dissolve

m "Now that we are ready, shall we start?"

show bob talk at right with dissolve
bob "Sure."

show natalie talk at left with dissolve
natalie "Ok."

hide bob talk
hide natalie talk

scene black

"A couple of minutes later."

scene cafe_memoria_inside_01_afternoon
m "We should take a quick break."

show bob happy at right with dissolve
bob "Finally."

show natalie talk at left with dissolve
natalie "Excuse me, I gotta fo to the bathroom."
hide natalie talk

show bob talk at right with dissolve
bob "[mc], you should buy some snacks."

m "Why don't you buy some."

show bob sad at right with dissolve
bob "I'm kinda tired, please take this one also buy my favorite snack."

m "Okay man."

hide bob sad

scene mall_d

"As you are done buying the snacks,you saw natalie talking to someone you don't know."


show natalie talk at left with dissolve
natalie "Sorry I'm with someone."

show strangeguy happy at right with dissolve
sg "Don't be shy we're just gonna some chat."


menu ask4:
        
        "Help":
                #block of code to run
                
                jump Act_3_Mall4
        "Keep Watching":
                #block of code to run
                jump Act_4_Mall2

label Act_3_Mall4:

$hbbpoints += 4

scene mallwalk_d

m "[natalie] I'm done buying let's go.Is there a problem?"

show strangeguy poker at right with dissolve
sg "Tsk..."
hide strangeguy poker

show natalie talk at left with dissolve
natalie "Thank you."

m "No problem. Do you know that guy?"

show natalie talk at left with dissolve
natalie "I don't know he suddenly approach me."

m "Really? We should go back [bob] is waiting."

scene black with dissolve

scene cafe_memoria_inside_01_afternoon with dissolve

show bob talk at right with dissolve
bob "What took you so long?"

m "I stumbled with [natalie] and some guy is trying to hit her."

show bob shock at right with dissolve
bob "[natalie] are you okay?"

show natalie talk at left with dissolve
natalie "I'm okay."

show bob happy at right with dissolve
bob "Good thing he didn't continue bothering you. Anyways you got our snacks?"

m "Here I got you. Now we should continue finishing this."

jump Act_4_Mall

label Act_4_Mall:

scene cafe_memoria_inside_01_afternoon with dissolve

"You saw the [u] looking at [natalie] in another seat."

show natalie talk at left with dissolve
natalie "He's here."

show bob shock at right with dissolve
bob "Who?"

m "The [u] that was talking to [natalie] earlier."

show bob angry at right with dissolve
bob "Maybe I should confront him."

show natalie talk at left with dissolve
natalie "No it's ok maybe he's just eating here."

show bob sad at right with dissolve
bob "Ok."

hide natalie talk
hide bob sad

scene black with dissolve

"Couple of minutes later."

scene cafe_memoria_inside_01_afternoon with dissolve

show bob happy at right with dissolve
bob "Done at last."

m "Thank you guys for the cooperation!"

show natalie happy at left with dissolve
natalie "Thank you too."

show bob talk at right with dissolve
bob "Don't mention it. Were suppose to do this together."

show natalie talk at left with dissolve
natalie "I have to go now before it gets dark."

m "Okay we should head out now it's getting night time."

show bob happy at right with dissolve
bob "[natalie] we'll escort you to your ride."

show natalie happy at left with dissolve
natalie "Thank you!"

hide bob happy
hide natalie happy

scene mall_e

show bob talk at right with dissolve
bob "Wait up I need to go in the toilet."

hide bob talk

"You saw again the [u]."

m "Mister is there a problem?"

show strangeguy poker with dissolve
sg "No, there is no problem. I just want to ask the cute girl's name."
hide strangeguy poker

show natalie poker with dissolve
natalie "....."
hide natalie poker

m "I don't think she wants to share that info so can you please leave?"

show strangeguy angry with dissolve
sg "What? I didn't ask you, I'm asking the cute girl."
hide strangeguy angry

m "Mister I don't think she.."

show natalie talk with dissolve
natalie "It's okay [mc].M-my name is [natalie]"
hide natalie talk

show strangeguy happy with dissolve
sg "That's a beautiful name, we should hang out sometime so give me your number."
hide strangeguy happy

show natalie talk with dissolve
natalie "Sorry but I just met you so I can't give it to you."
hide natalie talk

show strangeguy happy with dissolve
sg "Ey girl don't need to be hard to get, we all know you'll come with me in the bed."

menu ask5:

        "Warn him":
                #block of code to run
                jump Act_4_Mall1
        "Idle":
                #block of code to run
                jump Act_4_Mall2

        "Punch":
                #block of code to run
                jump Act_5_Mall2

label Act_4_Mall1:

scene mall_e

m "Mister please don't not bother her anymore.She doesn't want to talk to you."

show strangeguy poker with dissolve
sg "Kid I'm not talking to you and I'm not harming her."

m "She's uncomfortable this is my last warning ,mister."

show strangeguy angry with dissolve
sg "For the last time I'm not talking to you go away kid."


m "Mister are you aware that you can be taken to custody for this."

show strangeguy poker
sg "What law?"

m "The safe spaces act."

show strangeguy angry
sg "What spaceship are you talking about?Go away and shoo."
hide strangeguy angry

show natalie poker at left with dissolve
show strangeguy happy at right with moveinright
"The [sg] walk [natalie] closer."
hide natalie poker
hide strangeguy happy


#show hand
natalie "kyaah!"

menu:
        "I should do something."
        "Call the guard":
                #block of code to run
                jump Act_5_Mall1
        "Punch him":
                #block of code to run
                jump Act_5_Mall2

label Act_5_Mall1:


m "Guards! guards!"

show police neutral with dissolve
gd "What's the problem kid?"

m "This guy is harrassing my friend over here."

gd "Is this true sir?"
hide police neutral

show strangeguy poker with dissolve
sg "Nope this nerd is just making a random accusations."

m "No I'm not, You can talk with my friend here."
hide strangeguy poker

show police neutral with dissolve
gd "Is your friend telling the truth?"
hide police neutral

show natalie sad with dissolve
natalie "Ummm.."

m "[natalie] don't be scared, I got you cover this guy won't come for you anymore."

show natalie talk with dissolve
natalie "My friend told the truth."
hide natalie talk

show strangeguy shock with dissolve
sg "What? Now you guys are just pulling some pranks."
hide strangeguy shock

show police neutral with dissolve
gd "Ok ok, let's talk this calmly. Miss can you elaborate what happened? "
hide police neutral

show natalie poker with dissolve
natalie "Ok."
hide natalie poker

"Natalie explained everything happened."

jump Mall_End


label Act_5_Mall2:
        
play sound "audio/sfx/punch.wav"

show strangeguy shock with dissolve
sg "Ouch!What's wrong with you?"


mc "You better leave!"

play sound "audio/sfx/punch.wav"

sg "Aw!guards! guards!"
hide strangeguy shock

show police neutral with dissolve
gd "Hey what's the problem here?"
hide police neutral

show strangeguy angry with dissolve
sg "There's a psycho here help me!"

mc "What? you're the maniac here."
hide strangeguy angry

show police neutral with dissolve
gd "Sir you need to come with me."
hide police neutral

scene black

play sound "audio/sfx/fail.ogg"
# You Failed bg

menu:
        "Try Again":
                #block of code to run
                jump Act_2_School
        "Exit":
                #block of code to run
                return

label Act_4_Mall2:

play sound "audio/sfx/walking.ogg"
sg "(Approaches [natalie])"
show strangeguy happy at right with moveinright
sg "Come with me if you don't want your friend be hurt."

show natalie sad at left with dissolve
natalie "O-ok."

hide strangeguy happy
hide natalie sad

m "......"

scene black

play sound "audio/sfx/fail.ogg"
#You Failed bg

menu:
        "Try Again":
                #block of code to run
                jump Act_2_School
        "Exit":
                #block of code to run
                return

label Mall_EndB:
        $ badending1 = True
        
        centered "A couple of minutes of talk."

        centered "In the end you failed to show the strange guy true colors to the guard and allow,"

        centered "The Strange person persuade the guard!"
                # new achievement "worst decision"
        show strangeguy happy
        sg "Kiddo I don't think you know how the world works,see you."
        
        menu:

                "Ah this guy pisses me off"
                        
                "Punch him":
                #block of code to run
                        jump Act_5_Mall2
                        
                "Punch him":
                #block of code to run
                        jump Act_5_Mall2

label Mall_EndM:
        $ mending = True

        centered "A few minutes later."
        
        centered "With the attempts of the strange guy to twist the story but you succesfully denied them."
        
        show police neutral with dissolve
        gd "I see that's what happened."

        show police angry
        gd "Mister please stay away from this people."
        hide police angry

        show strangeguy shock with dissolve
        sg "Man, I'm just wanna talk."

        show strangeguy angry with dissolve
        sg "Hey geek boy!If I see you once more you better run."

        m "Sir I think you should take him."

        show stalker happy with dissolve
        sg "What you gonna do dweeb!?"

        m "Sir are you hearing this? He's violating the law."

        show strangeguy poker with dissolve
        sg "Again with your space law. I'm a citizen here not an alien."

        menu:
                "It's Safe spaces act":
                        #block of code to run
                        jump Mall_EndM1 
                "It's Save space act":
                        #block of code to run
                        jump Mall_EndM1
                "It's the law of space":
                        #block of code to run
                        jump Mall_EndM1
                "No you're an alien!":
                        #block of code to run
                        jump Mall_EndM1
label Mall_EndM1:

        m "You should leave."

        show police neutral
        gd "Sir from what I am seeing the kid is right."
        hide police neutral

        show strangeguy shock
        sg "What!?"

        show police angry with dissolve
        gd "Please leave or I'll arrest you."
        hide police angry

        show strangeguy poker with dissolve
        sg "Ok, ok I'll leave."
        hide strangeguy poker


        m "Ah at last that guy is gone."

        show natalie happy at left with dissolve
        natalie "Thank you [mc]."

        m "No problem remember your my friend, I got your back."

        natalie "Mmhmm."

        show bob talk at right with dissolve
        bob "Sorry the line in the bathroom is long did I miss something?"

        m "Ah we can talk about it while we walk."
        hide natalie happy
        hide bob talk

        scene black
        #bg The end
        pause 2.0


return



label Mall_EndG:
        
        centered "A few minutes later."
        
        centered "Special ending underconstruction"



return
