#Catch Those Presents
#Maria Kang
#Last update: January 14
#catch and drop game, where the main character is trying to catch all the presents that santa dropped
#only the left and right arrows are applicable
#THE GAME HAS A SLIPPERY EFFECT 

## If you get the no available video device error, copy and paste the below code ##

import platform, os

if platform.system() == "Windows":

    os.environ['SDL_VIDEODRIVER'] = 'windib'

### If you get the no available video device error, copy and paste the above code ###

#imports all the modules necessary for game to run 
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import random
import time

#graphics all self made

#movement with graphics
x,y = 0,0
moveX = 0

#initialize Pygame modules
pygame.init()

#sets screen size
screen = pygame.display.set_mode((600,600))

#title bar caption
pygame.display.set_caption('Catch Those Presents')

#loads the background, self made
menu = pygame.image.load("Background.png").convert()
#scales it according to the size of screen 
menu = pygame.transform.scale(menu,(600,600))

#loads the present - what user are trying to catch
present = pygame.image.load("Present.png")
#scales it
present = pygame.transform.scale(present,(53,58))

#game background 
gameBg = pygame.image.load("Game.png").convert()
gameBg = pygame.transform.scale(gameBg, (600,600))

#game over background
gOver = pygame.image.load("Game Over.png")
gOver = pygame.transform.scale(gOver, (600,600))

#character - Main
char = pygame.image.load("Character Right.png")
char = pygame.transform.scale(char,(86,122))

#character - Right
charR = pygame.image.load("Character Right.png")
charR = pygame.transform.scale(charR,(86,122))

#character - Left
charL = pygame.image.load("Character Left.png")
charL = pygame.transform.scale(charL,(86,122))

#help screen
instruction = pygame.image.load("Instructions.png")
instruction = pygame.transform.scale(instruction,(600,600))

#high scores screen
highscore = pygame.image.load("High Scores.png")
highscore = pygame.transform.scale(highscore,(600,600))

#radomly generates a x coordinate for the present to fall from 
xPos = random.randint(0,547)

#randomly generates speed of the present falling
ySpeed = random.randint(5,15)

show = "menu"
level = 1
lives = 3
total = 0
presentsDropped = 0

#accuracy function
def accuracy(presentDropped, total):
    rate = round(float(total/presentDropped) * 100,2)
    return rate
   
#font and size 
myFont = pygame.font.SysFont("Arial",20)
bFont = pygame.font.SysFont("Arial",50)
cFont = pygame.font.SysFont("Arial",50)

#allows the user input loop to run
menuReturn = False

#file input and output so users can access their scores, this is in append mode
newFile = open("High Scores.txt","a")
#closes file for now 
newFile.close()
times = 0
name = ""
point1 = 0 

#puts all the scores in a list 
scoreList = []
#finds the position in the list
high = 0
placeholder = 0

print scoreList

#removes the highest number from list 

# Event Handling: include it for now so that you can quit the program cleanly ###
running=True
try:
    while running:

        newFile = open("High Scores.txt","r")
        #puts everything in a list
        allScore = newFile.readlines()

        for score in allScore:
            #strips out newLine
            score = score.rstrip("\n")
            #adds it to list
            scoreList += [score]

        newFile.close()

        events = pygame.event.get()

        for event in events:
            print event.type
            if event.type == QUIT:
                print event
                running=False   # Stop the program, if detected quit

        #blit background to screen surface         
        screen.blit(menu,(0,0))

        pygame.display.update()

        #tracks mouse events
        for x_coord in events:
            pos = pygame.mouse.get_pos()
            button_1 = pygame.mouse.get_pressed()
            x_coord = pos[0]
            y_coord = pos[1]
            print x_coord, y_coord, pos, button_1

             #shows viewer
            if 190 < x_coord < 419 and 398 < y_coord < 463 and button_1[0] == 1:
                show = "help"

            #the coordinates has to be within the button and mouse is clicked
            if 186 < x_coord < 423 and 298 < y_coord < 371 and button_1[0] == 1:
                level = 1
                lives = 3
                total = 0
                presentsDropped = 0
                #makes sure that if the user plays the game again, they can enter new username
                menuReturn = False
                show = "play"

            if 189 < x_coord < 418 and 498 < y_coord < 564 and button_1[0] == 1:
                show = "highscores"

        while show == "highscores":

            #mouse movements - maybe put this into a function
            for x_coord in pygame.event.get():
                pos = pygame.mouse.get_pos()
                button_1 = pygame.mouse.get_pressed()
                x_coord = pos[0]
                y_coord = pos[1]
                print x_coord, y_coord, pos, button_1

            #if i hit a certain perimeter, the loop breaks and showing the menu again
            if 185 < x_coord < 413 and 350 < y_coord < 417 and button_1[0] == 1:
                show = "menu"
            

            #shows the highscore background on screen
            screen.blit(highscore,(0,0))

            for number in scoreList:
                point1 = number[number.find(" ")+1:]
                name1 = number[:number.find(":")]
                if times < int(point1):
                    times = int(point1)
                    name = name1
                
            #prints out first highest score        
            num1 = myFont.render("PLAYER TO BEAT:",11,(255,255,255))
            screen.blit(num1,(180,200))

            num2 = myFont.render(name+"      "+str(times),11,(255,255,255))
            screen.blit(num2,(230,230))


            pygame.display.update()
            
        #if they hit a certain perimeter, the page is redirected onto here 
        while show == "help":
            
            #mouse movements
            for x_coord in pygame.event.get():
                pos = pygame.mouse.get_pos()
                button_1 = pygame.mouse.get_pressed()
                x_coord = pos[0]
                y_coord = pos[1]
                print x_coord, y_coord, pos, button_1

            screen.blit(instruction,(0,0))
            pygame.display.flip()

            if 408 < x_coord < 578 and 22 < y_coord < 73 and button_1[0] == 1:
                show = "menu"
                        
        #if show equals play, the loop will keep running until otherwise
        while show == "play":
            
            #shows the game background
            screen.blit(gameBg,(0,0))

            #show black screen or make one
            #render "game over" text
            #blit text
            #tells user to enter their name to save score
            #allows user input, saves them to files
            if lives <= 0:
                
                if menuReturn == True:
                    show = "menu"

                username = ""
                 
                while menuReturn == False:

                    screen.blit(gOver,(0,0))

                    #instru = myFont.render("To save your score, please type an username, press ENTER when you're done:",1,(255,255,255))
                    #screen.blit(instru,(30,300))

                    user_Input = cFont.render(username,True,(255,255,255))
                    screen.blit(user_Input,(100,400))  

                    #tracks keyboard events in pygame after the game finishes
                    #this allows them to enter a username and see their high scores
                    for event in pygame.event.get():

                        if event.type == QUIT:
                            print event
                            running=False 
                        
                        if event.type != pygame.KEYDOWN:
                            continue

                        #if the user press returns, their username is automatically saved
                        if event.key == pygame.K_RETURN:
                            newFile = open("High Scores.txt","a")    
                            #writes on the same line
                            newFile.write(username+": "),
                            newFile.write(str(total)+"\n")
                            newFile.close()
                            menuReturn = True
        
                        if event.key == pygame.K_BACKSPACE:
                            #takes away the last letter 
                            username = username[0:-1]

                        else:
                            #username = "Anonymous"
                            #adds the ascii letters typed like a, b, etc
                             username += event.unicode.encode("ascii")
  
        
                    pygame.display.flip()   
    

            elif y < 0 or y >= 600:
                y = 0
                #the changing x coordinate is randomly generated 
                xPos = random.randint(0,530)
                #speed of the present is randomly generated
                ySpeed = random.randint(3,10)

            #Middle of Screen 
            #screen.blit(char,(257,478))
    
            #tracks keyboard movements
            for event in pygame.event.get():
                if event.type == QUIT:
                    print event
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        char = charL
                        moveX -= 6
                    elif event.key == K_RIGHT:
                        char = charR
                        moveX += 6
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        char = charL
                        #makes the ground slippery
                        moveX = -6
                    elif event.key == K_RIGHT:
                        char = charR
                        #makes the game harder
                        moveX = 6

            #moves the x
            x += moveX
            #makes sure x does not go off the screen 
            if x < -2:
                x = 0
            elif x > 514:
                x = 514

            #character is on screen
            screen.blit(char,(x,478))
            #present falls from sky
            screen.blit(present,(xPos,y))
            #falls from screen certain pixel at a time (SPEED is generated)
            y += ySpeed

            #when character hits those positions, the user gets a point 
            if (539 > y >= 477 and x <= xPos < x+ 89) or (539 > y >= 477 and x <= xPos+58 <= x+ 89):
                total += 1
                y = -1
            if y > 539:
                total += 0
                if y >= 600:
                    #player loses life 
                    lives -= 1

            #adds the total presents dropped
            presentsDropped += 1

            #levelText = myFont.render("Level "+str(level), 1, (255,255,255))
            #screen.blit(levelText,(319,10))
            #shows the score on board 
            score = myFont.render("Score: "+str(total),1,(255,255,255))
            screen.blit(score,(400,10))
            #shows lives 
            lifeLine = myFont.render("Lives: "+str(lives),1,(255,255,255))
            screen.blit(lifeLine, (500,10))

            pygame.display.flip()

        
finally:
    pygame.quit()  # Keep this IDLE friendly
