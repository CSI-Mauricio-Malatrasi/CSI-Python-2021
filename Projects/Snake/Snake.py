import pygame #imports pygame
pygame.init()   #starts game

#Colors RGB, Red Green Blue
white = (255, 255, 255) #white color
black=(0,0,0)  #blue color
red=(255,0,0)   #red color

dis=pygame.display.set_mode((800,600))  #Dimensions
pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game

game_over=False #Tells you the game isn't over

x1 = 300
y1 = 300
 
x1_change = 0       #Stores the change in the snake
y1_change = 0       #Stores the change in the snake

clock = pygame.time.Clock()

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

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])  #Draws the colors imported

    pygame.display.update() #Updates the game

    clock.tick(30)  #Makes a clock

pygame.quit()   #quits the game
quit()  #quits everything
