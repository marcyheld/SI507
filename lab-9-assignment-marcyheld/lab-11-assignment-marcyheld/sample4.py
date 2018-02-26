# How to draw shapes

#required
import pygame
pygame.init()

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Drawing Shapes!")

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
	gameDisplay.fill(white)

	# Drawing rectangles to the Game Display window [x, y, width, height]
												# x and y of top left corner !
	pygame.draw.rect(gameDisplay, black, [400,300, 10, 100])
	pygame.draw.rect(gameDisplay, red, [100,100, 50, 50])

	# Filling out blue color to a rectangle object (not to the background)
	gameDisplay.fill(blue, rect=[200,200, 20,20])
	gameDisplay.fill(blue, rect=[50,50, 20,20])

	# Drawing a circle to the Game Display window
	pygame.draw.circle(gameDisplay, red, (50,100), 20, 0)

	# Drawing a line to the Game Display window
	pygame.draw.lines(gameDisplay, red, False, [(100,100), (150,200), (200,100)], 1)

	# Updating all objects in the display
	pygame.display.update()


#required
pygame.quit()
quit()				#exits python
