import pygame

pygame.init() 

Display = pygame.display.set_mode((600,300))

pygame.display.set_caption("Bar Graph")
pygame.display.update()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# You will be visualizing this data.
# (Label, Color of the bar, Length of the bar)
data = [('Apple',red,15), ('Banana',yellow,45), ('Melon',green,28)]


# Design your own Class
# The class should be initialized with the label, color, and length of each item in the 'data' list.
# The class should have a function(or multiple functions) to draw a bar graph.
class Bar:
	def __init__ (self, name, color, num, y_coord):
		self.name = name
		self.color = color
		self.length = num
		self.y = y_coord
		# display parameter is same for all 3 bars
		# for making rectangle: pygame.draw.rect(Surface, color, Rect, width=0)
		# "Rect" param == [x-coord start, y-coord start, rect width, rect height]
	def drawGraph(self, display):
		pygame.draw.rect(display, self.color, [100, self.y, self.length * 10, 60])

loopCond = True
while loopCond:
	Display.fill(white)
	bar_y = 20
	text_y = 45

	for item in data:
		fruitBar = Bar(item[0], item[1], item[2], bar_y)
		fruitBar.drawGraph(Display)
		bar_y += 80

		f = pygame.font.Font (None, 25) # select text font and font size
		text = f.render(fruitBar.name, False, black) # (text contents, anti-alias ???, color)
		Display.blit(text, (20, text_y)) # put the text on the screen!
		text_y += 80

	# Write the codes to draw a graph based on 'data' list.

	pygame.display.update()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loopCond = False


pygame.quit()
quit()
