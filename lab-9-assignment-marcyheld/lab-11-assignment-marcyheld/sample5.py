# How to simulate animation

#required
import pygame
pygame.init()

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Movement!")

pygame.display.update()		#only updates portion specified

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 0
y_pos = 0

gameExit = False
while not gameExit:
	gameDisplay.fill(white)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	# Detecting any keyboard input
	if event.type == pygame.KEYDOWN:
		# Specifies anctions based on keyboard arrows
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10
		if event.key == pygame.K_UP:
			y_pos -= 10
		if event.key == pygame.K_DOWN:
			y_pos += 10


	gameDisplay.fill(blue, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()



#required
pygame.quit()
quit()				#exits python
