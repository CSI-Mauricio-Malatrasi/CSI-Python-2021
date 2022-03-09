import pygame #imports pygame
pygame.init()   #starts game
dis=pygame.display.set_mode((400,300))  #Dimensions
pygame.display.update() #updates the game
pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game
game_over=False #Tells you the game isn't over
while not game_over:    #Start loops
    for event in pygame.event.get(): 
        print(event)   #prints out all the actions that take place on the screen

pygame.quit()   #quits the game
quit()  #quits everything