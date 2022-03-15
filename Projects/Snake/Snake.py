import pygame #imports pygame
import time     #imports time
import random   #imports random

pygame.init()   #starts game

#Colors RGB, Red Green Blue
white = (255, 255, 255) #white color
black=(0,0,0)  #blue color
red=(255,0,0)   #red color
blue=(0,0,255)

dis_width = 800     #width
dis_height  = 600   #height

dis=pygame.display.set_mode((dis_width, dis_height))  #Dimensions
pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game

clock = pygame.time.Clock()     #Clock for the game

snake_block=10      #Shows the snake
snake_speed=30      #speed of the snake

font_style = pygame.font.SysFont(None, 30)  #Font size for the game


def message(msg,color):         #Defines message
    mesg = font_style.render(msg, True, color) 
    dis.blit(mesg, [dis_width/3, dis_height/3])


def gameLoop():     #Creates a function
    game_over=False #Tells you the game isn't over
    game_close=False #Tells the game to not close unless you press Q

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0       #Stores the change in the snake in x
    y1_change = 0       #Stores the change in the snake in y

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #Imports the food in a random manner in x
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #Imports the food in a random manner in y
    
    while not game_over:    #Start loops
        
        while game_close == True:
            dis.fill(white) #full white background
            message("You Lost! Press Q-Quit or C-Play Again", red)  #Shows you a message and lets you try again or quit
            pygame.display.update() #Updates the game

            for event in pygame.event.get():    #Makes "Q" for quitting the game and "C" to try again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                game_over=True  #If the game quits, game over = true
            if event.type == pygame.KEYDOWN: #Makes the movement of the snake
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:     #Makes it so if you do those things, it makes game_over true.
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)    #full white background
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])   #Draws the food
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])    #Draws the colors imported
        pygame.display.update() #Updates the game

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)  #Makes a clock

    pygame.quit()   #quits the game
    quit()  #quits everything


gameLoop()