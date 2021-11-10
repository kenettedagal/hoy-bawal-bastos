# The script of the game goes in this file.
# Main Character


# Side Character
define natalie = Character("Natalie")
define bob = Character("Bob")
define sg = Character("Strange guy")
define gd = Character("Guard")
define tsci = Character("Teacher Johnny")
define mc = Character("Me")
define u = Character("Strange guy")


# Script starts here.
label Act_2_School:
        

        scene bg classroom_01_day
        #play sound "audio/eclsrom.ogg"
        mc "Oh, no one's here yet. I guess I'm too early."

        "I should take a quick nap."

        scene black

        #play sound "audio/hey"
        show unknown worried with dissolve
        u "Wake up,hey wake up. Class will be starting in a minute."
        #hbb points lagay
        menu:

                "Continue sleeping":

                        jump class1
                "Wake up":
                        jump class2



label class1:
        
        scene bg classroom_01_day

        
        mc "............."
        show johnny angry
        tsci "The class has already started, if you want to sleep feel free to leave this room."
        
        show johnny poker
        mc "I'm sorry miss it won't happen again."

        jump lunchbreak

label class2:

        scene bg classroom_01_day
        
        show johnny poker
        tsci "Good morning everyone, we will begin our class but first of all let's get your attendance."

        jump lunchbreak

label lunchbreak:

        scene classroom lunch1

        $ play_sound(bell)

        tsci "Ok class dismiss,don't forget your activity for the next meeting."
        tsci "Also remember to cooperate with your members."

        scene bg cafeteria

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

        menu:

                "Hmmm..."
                "Agree":
                #block of code to run

                        mc "Yes, I'm glad that your part of my group."
                        show bob talk at right with dissolve
                        bob "See? I told you."
                        show kurtney angry talk at left with dissolve
                        kk "What your part of Bob's group!? Dude I want to be in your group."

                        jump Act2

                "Neutral":
                #block of code to run
                        mc "Well your neither the best nor the worst."
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

        mc "Yes I am,what is it?"

        show bob happy at right with dissolve
        bob "Ho,Hello there cutie"

        show natalie talk at left with dissolve
        natalie "Oo-oh he-hello."

        show bob talk at right with dissolve
        bob "You're new here? Come join here eat with us."

        #punch sound effect

        show bob shock at right with dissolve
        bob "Aw, what's wrong your with you?"

        hide natalie talk
        show kurtney angry talk at left with dissolve
        kk "Stop hitting with all the girls in the school,dude!"

        show bob talk at right with dissolve
        bob "I'm just asking her to join us."

        mc "Don't mind them is there something you want?"

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

        #punch sound effect
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

        mc "Yes, he's right feel free to talk to us."

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

        mc "Now that I think about it"

        scene black

        show natalie happy at center with dissolve
        "[natalie] a new female student in our class. A tranferee in the middle of prelims."
        "I don't know anything about her,well... guess she's a shy person."

        scene bg cafeteria

        show natalie talk at left with dissolve
        show bob poker at right with dissolve

        mc "About the group activity. Why don't be talk about it after school?"
        show bob talk at right with dissolve
        bob "Right, we can go to the foodcourt in the mall."
        show  natalie talk at left with dissolve
        natalie "O-ook."
        mc "It's decided then see you later!"

label Act_2_School_Chapter2:

        scene school gate

        mc "It seems I'm the first one here."

        natalie "....."

        mc "Looks to the side"

        show natalie poker with moveinleft

        mc "Oh, you're here."

        natalie "So-sorry for being late."

        mc "You're not late and were still waiting for [bob]."

        natalie "....."

        mc "....."

        mc "(This is bad. It might get awkward here until [bob] comes, what should I do?)"

        menu:
                
                "Talk to her":
                        #block of code to run
                        jump Act_2_School_1
                "Keep Silent":
                        #block of code to run
                        jump Act_2_School_2
label Act_2_School_1:        

        scene school gate

        mc "The weather is nice today."

        natalie "Yes and the wearther report says to be sunny and not expect to rain."

        mc "It seems you watch a lot of weather forecast."

        natalie "I do like seeing the weather forecast."

        mc "Is there something you like other than that?"

        natalie "I like to read books and p-play some video games."

        mc "Oh really?! That's awesome, is there something you recommend to read?"

        bob "Heyoo, Sorry for being late the match took longer than I expected."

        mc "Ok now that everyones here.Are we ready to go?"

        bob "Yep, I'm ready."

        natalie "I'm good to go."

        jump Act_3_Mall


label Act_2_School_2:

        scene school gate

        "You waited [bob] in silence"

        mc "Oh really?! That's awesome, is there something you recommend to read?"

        bob "Heyoo, Sorry for being late the match took longer than I expected."

        mc "Ok now that everyones here.Are we ready to go?"

        bob "Yep, I'm ready."

        natalie "....."


        jump Act_3_Mall


        label Act_3_Mall:

        #bg mall entrance

        bob "Were here.Are we going to buy materials or we eat first?"

        menu:

                "Buy materials":
                        #block of code to run
                        jump Act_3_Mall1
                "Eat first":
                        #block of code to run
                        jump Act_3_Mall2

label Act_3_Mall1:




label Act_3_Mall2:






label Act_3_Mall3:

#foodcourt bg

mc "Now that we are ready, shall we start?"

bob "Sure."

natalie "Ok."

"A couple of minutes later."

mc "We should take a quick break."

bob "Finally."

natalie "Excuse me, I gotta fo to the bathroom."

bob "[mc], you should buy some snacks."

mc "Why don't you buy some."

bob "I'm kinda tired, please take this one also buy my favorite snack."

mc "Okay man."

#foodcourt bg

"As you are done buying the snacks,you saw natalie talking to someone you don't know."

natalie "Sorry I'm with someone."

u "Don't be shy we're just gonna some chat"

menu:
        
        "Help":
                #block of code to run
                jump Act_3_Mall4
        "Keep watching":
                #block of code to run
                jump Act_3_Mall5

label Act_3_Mall4:

mc "[natalie] I'm done buying let's go.Is there a problem?"

u "Tsk..."

natalie "Thank you."

mc "No problem. Do you know that guy?"

natalie "I don't know he suddenly approach me."

mc "Really? We should go back [bob] is waiting."

#foodcourt seat bg

bob "What took you so long?"

mc "I stumbled with [natalie] and some guy is trying to hit her"

bob "[natalie] are you okay?"

natalie "I'm okay."

bob "Good thing he didn't continue bothering you. Anyways you got our snacks?"

mc "Here I got you. Now we should continue finishing this."

jump Act_4_Mall

label Act_3_Mall5:


label Act_4_Mall:

#foodcourt bg

"You saw the [u] looking at [natalie] in another seat."

natalie "He's here."

bob "Who?"

mc "The [u] that was talking to [natalie] earlier."

bob "Maybe I should confront him."

natalie "No it's ok maybe he's just eating here."

bob "Ok."

"Couple of minutes later."

bob "Done at last."

mc "Thank you guys for the cooperation!"

natalie "Thank you too."

bob "Don't mention it. Were suppose to do this together."

natalie "I have to go now before it gets dark."

mc "Okay we should head out now it's getting night time."

bob "[natalie] we'll escort you to your ride."

natalie "Thank you!"

# mall

bob "Wait up I need to go in the toilet."

"You saw again the [u]."

mc "Mister is there a problem?"

u "No there is no problem. I just want to ask the cute girl's name."

natalie "....."

mc "I don't think she wants to share that info so can you please leave?"

u "What? I didn't ask you, I'm asking the cute girl."

natalie "M-my name is [natalie]"

u "That's a beautiful name, we should hang out sometime so give me your number."

natalie "Sorry but I just met you so I can't give it to you."

u "Ey girl don't need to be hard to get, we all know you'll come with me in the bed."

menu :

        "Warn him":
                #block of code to run
                jump Act_4_Mall1
        "Keep Listening":
                #block of code to run
                jump Act_4_Mall2


label Act_4_Mall1:





label Act_4_Mall2:

return