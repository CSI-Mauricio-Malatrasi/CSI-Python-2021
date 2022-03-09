import pygame #imports pygame
pygame.init()   #starts game
dis=pygame.display.set_mode((400,300))  #Dimensions

pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game

#Colors RGB, Red Green Blue
blue=(0,0,255)  #blue color
red=(255,0,0)   #red color

game_over=False #Tells you the game isn't over
while not game_over:    #Start loops
    for event in pygame.event.get(): 
       if event.type==pygame.QUIT:
            game_over=True  #If the game quits, game over = true
    pygame.draw.rect(dis,blue,[200,150,10,10])  #Draws the colors imported
    pygame.display.update() #Updates the game
pygame.quit()   #quits the game
quit()  #quits everything