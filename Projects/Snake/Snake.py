import pygame #imports pygame
import time     #imports time
pygame.init()   #starts game

#Colors RGB, Red Green Blue
white = (255, 255, 255) #white color
black=(0,0,0)  #blue color
red=(255,0,0)   #red color

dis_width = 800     #width
dis_height  = 600   #height
dis=pygame.display.set_mode((800,600))  #Dimensions
pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game

game_over=False #Tells you the game isn't over

x1 = dis_width/2
y1 = dis_height/2

snake_block=10      #Shows the snake
 
x1_change = 0       #Stores the change in the snake
y1_change = 0       #Stores the change in the snake

clock = pygame.time.Clock()     #Clock for the game
snake_speed=30      #speed of the snake

font_style = pygame.font.SysFont(None, 50)  #Font size for the game

def message(msg,color):         #Defines message
    mesg = font_style.render(msg, True, color) 
    dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:    #Start loops
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
    dis.fill(white)     #full white background
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])  #Draws the colors imported

    pygame.display.update() #Updates the game

    clock.tick(snake_speed)  #Makes a clock

message("You lost",red)     #Displays "You lost" in red in the middle of the screen
pygame.display.update()
time.sleep(2)

pygame.quit()   #quits the game
quit()  #quits everything
