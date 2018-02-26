# Change Frame seconds and make movements smoothly

#required
import pygame
pygame.init()

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Frame per seconds")

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
x_delta = 0
y_delta = 0

clock = pygame.time.Clock()

def redraw():
	gameDisplay.fill(white)
	gameDisplay.fill(blue, rect=[50,50, 20,20])
	pygame.draw.circle(gameDisplay, red, (50,100), 20, 0)
	pygame.draw.lines(gameDisplay, red, False, [(100,100), (150,200), (200,100)], 1)

	# Creating a string object.
	f = pygame.font.Font(None, 25)
	# Rendering this string object.
	t = f.render('Sample Text', False, black)
	# Displaying this text on the window.
	gameDisplay.blit(t, (400,300))


gameExit = False
while not gameExit:
	# Drawing objects and filling out background color
	redraw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		x_delta=0
		y_delta=0
		# Changing delta value to move the object automatically
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10

	# Keep changing x and y position based on the delta value until you put another keyboard input
	x_pos += x_delta
	y_pos += y_delta

	gameDisplay.fill(blue, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()

	# Setting frame seconds. You can change the number to make the game faster or slower.
	clock.tick(10)


#required
pygame.quit()
quit()				#exits python
