# init python:
#     def checkIndex():




screen newspaper():
    vbox:
        image "images/paper1.png"



screen titleYui():
    
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=50}Story #1{/size}\n\n\n{size=80}A New School Year{/size}{/color}{/b}"

screen jeepTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}A Stalking Problem{/size}{/color}{/b}"

screen stalkerTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}Confrontation{/size}{/color}{/b}"

screen trainTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}Taking the Morning Train{/size}{/color}{/b}"

screen schoolTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}A Prestigious School{/size}{/color}{/b}"

screen lostTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}You Got Lost?{/size}{/color}{/b}"

screen pervTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}Troubled Days{/size}{/color}{/b}"

screen arrestTransition():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5 
            text "{b}{color=#ffffff}{size=80}Fighting On!{/size}{/color}{/b}"



screen showNotesButton():
    modal False
    frame:
        yalign 0.01
        xalign 0.01
        imagebutton:
            xmaximum 200
            ymaximum 200
            idle "book.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Show("notebookPage"),Hide("showNotesButton")]


screen showNotebook():
    modal False
    
    $ notebookOpen = True 
    $ renpy.show_screen("notebookPage")
    # imagebutton:
    #     yalign 0.01
    #     xalign 0.01
    #     xmaximum 200
    #     ymaximum 200
    #     idle "book.png"
    #     activate_sound "audio/sfx/newspaper.wav"            
    #     action Hide("showNotesButton")
    #     if notebookOpen:
    #         action [Hide("showNotebook",dissolve),Hide("notebookPage"),Show("showNotesButton")] 
            
    #     else: 
    #         action Show("showNotebook")
    
            #show screen
        
        
    
        
        

screen notebookPage():
    modal True
    $ addIndex = notebookIndex + 1
    $ subIndex = notebookIndex - 1




    if yuiStoryProgress == 1 and notebookIndex == 0:
        pass 

    elif yuiStoryProgress == 2 and notebookIndex == 1:
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "leftarrow.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Hide("notebookPage"),SetVariable("notebookIndex", subIndex),Show("notebookPage")]
        
    elif yuiStoryProgress == 2 and notebookIndex == 0:
        # imagebutton:
        #     xalign 0.0
        #     yalign 0.5
        #     idle ""
        #     activate_sound "audio/sfx/newspaper.wav"
        #     action [Hide("notebookPage"),SetVariable("notebookIndex", subIndex),Show("notebookPage")] 
        # imagebutton:
        #     xalign 0.9999
        #     yalign 0.5
        #     idle ""
        #     activate_sound "audio/sfx/newspaper.wav"
        #     action [Hide("notebookPage"),SetVariable("notebookIndex", addIndex),Show("notebookPage")]
            #show screen
        imagebutton:
            xalign 0.9999
            yalign 0.5
            idle "rightarrow.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Hide("notebookPage"),SetVariable("notebookIndex", addIndex),Show("notebookPage")]

    elif yuiStoryProgress == 3 and notebookIndex == 3:
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "leftarrow.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Hide("notebookPage"),SetVariable("notebookIndex", subIndex),Show("notebookPage")] 
    elif yuiStoryProgress == 3 and notebookIndex == 0:
        imagebutton:
            xalign 0.9999
            yalign 0.5
            idle "rightarrow.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Hide("notebookPage"),SetVariable("notebookIndex", addIndex),Show("notebookPage")]

       
    else:
        imagebutton:
            xalign 0.9999
            yalign 0.5
            idle "rightarrow.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Hide("notebookPage"),SetVariable("notebookIndex", addIndex),Show("notebookPage")]
            #show screen
            
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "leftarrow.png"
            activate_sound "audio/sfx/newspaper.wav"
            action [Hide("notebookPage"),SetVariable("notebookIndex", subIndex),Show("notebookPage")]
    
    imagebutton:
        yalign 0.01
        xalign 0.01
        xmaximum 200
        ymaximum 200
        idle "book.png"
        activate_sound "audio/sfx/newspaper.wav"            
        action [Hide("notebookPage", dissolve),Show("showNotesButton")]
            
        
    vbox:
        xalign 0.5
        yalign 0.5
        if notebookIndex == 0:
            image "images/notebook.jpg"
            at transform:

                    align (0.5, 0.5) alpha 0.0
                    linear 0.5 alpha 1.0
                    pause 2
        elif notebookIndex == 1:
            image "images/notebook1.jpg"
            at transform:

                    align (0.5, 0.5) alpha 0.0
                    linear 0.5 alpha 1.0
                    pause 2
        elif notebookIndex == 2:
            image "images/notebook2.jpg"
            at transform:

                    align (0.5, 0.5) alpha 0.0
                    linear 0.5 alpha 1.0
                    pause 2
        elif notebookIndex == 3:
            image "images/notebook3.jpg"
            at transform:

                    align (0.5, 0.5) alpha 0.0
                    linear 0.5 alpha 1.0
                    pause 2



            

screen displayHBBPoints():
    modal False
    frame:
        xmaximum 300
        ymaximum 100
        xalign 0.999
        yalign 0.003
        vbox:
            text "{color=#22ff00}HBB Points{/color}"
            text "[hbbpoints]" xalign 0.5
            at transform:

                align (0.5, 0.5) alpha 0.0
                linear 0.5 alpha 1.0
                pause 2

screen displayScore():
    modal False
    frame:
        xmaximum 300
        ymaximum 100
        xalign 0.0
        yalign 0.003
        vbox:
            text "{color=#22ff00}Quiz Score{/color}"
            text "[quizPoints]" xalign 0.5
            at transform:

                align (0.5, 0.5) alpha 0.0
                linear 0.5 alpha 1.0
                pause 2
                
        


screen newNote():

    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 400
        ymaximum 300
        
        vbox: 
            text "New notes has been added to notebook!\n" xalign 0.5
            textbutton "OK" action Hide("newNote") xalign 0.5 yalign 0.5 xmaximum 400 activate_sound "audio/sfx/confirm.ogg"

screen testScreen():    
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1200
        ymaximum 800
        viewport:
            mousewheel True
            scrollbars 'vertical'
            vbox:
                xfill True
                spacing 20
                
                text "\n\n{color=#ff3d3d}{u}Republic Act No. 11313{/u}{/color} also known as \"{color=#ff3d3d}Safe Spaces Act{/color}\"." xalign 0.5
                text ""
                text "Date Approved: April 17, 2019" xalign 0.5
                text "\n\nThe {color=#ff3d3d}{u}Safe Spaces Act{/u}{/color} is an act defining gender-based sexual harassment in streets, public spaces, online, workplaces, and educational or training institutions."xalign 0.5 justify True
                
                if yuiStoryProgress >= 2:  #List of Violations
                     
                    text "\n      {color=#ff3d3d}List of Violations{/color} (from SEC.5 of Safe Spaces Act):\n\na) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic,and sexist slurs;\n\nb) Persistent uninvited comments or gestures on a person's appearance;\n\nc) Relentless requests for personal details;\n\nd) Statement of sexual comments and suggestions;\n\ne) Public masturbation or flashing of private parts, groping, making offensive body gestures at someone, and other similar lewd sexual actions;\n\nf) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. This may include cursing, leering and intrusive gazing, and taunting;\n\ng) Persistent telling of sexual jokes, use of sexual names;\n\nh) Stalking." xalign 0.5 justify True line_spacing 10

                if yuiStoryProgress >= 3:  #Specific Acts and Penalties
                    
                    text "\n\n{color=#ff3d3d}Specific Acts and Penalties{/color} for Gender-Based Sexual Harassment in Streets and Public Spaces. (from SEC. 12 of Safe Spaces Act)\n\na) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs, persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination, the use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs, the persistent telling of sexual jokes, use of sexual names, comments and demands, and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety.\n\n{color=#ff3d3d}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP.\n\n{color=#ff3d3d}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)\n\n{color=#ff3d3d}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)" xalign 0.5 justify True line_spacing 10

                    text "\n\n\nb) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening or intimidating the offended party including flashing of private parts, publicmasturbation, groping, and similar lewd sexual actions.\n\n{color=#ff3d3d}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP.\n\n{color=#ff3d3d}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)\n\n{color=#ff3d3d}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)" xalign 0.5 justify True line_spacing 10

                    text "\n\n\nc) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person; or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b).\n\n{color=#ff3d3d}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP.\n\n{color=#ff3d3d}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)\n\n{color=#ff3d3d}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)" xalign 0.5 justify True line_spacing 10
                    
                    

                
                text "\n\n-- End of Notes --\n" xalign 0.5 
                                
                textbutton _("{color=#40ff00}Close Notebook{/color}"):
                    xalign 0.5
                    yalign 0.5
                    
                    action [Hide("testScreen"), Show("showNotesButton", dissolve)]