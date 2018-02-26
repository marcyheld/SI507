# How to change background color

#required
import pygame
pygame.init()

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Events")

pygame.display.update()		#only updates portion specified

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	# Filling out background color
	gameDisplay.fill(green)
	pygame.display.update()


#required
pygame.quit()
quit()				#exits python
