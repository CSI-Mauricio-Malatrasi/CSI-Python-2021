import pygame #imports pygame
pygame.init()   #starts game
dis=pygame.display.set_mode((400,300))  #Dimensions
pygame.display.update() #updates the game
pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game
game_over=False #Tells you the game isn't over
while not game_over:    #Start loops
    for event in pygame.event.get(): 
       if event.type==pygame.QUIT:
            game_over=True  #If the game quits, game over = true

pygame.quit()   #quits the game
quit()  #quits everything