import pygame

import model #imports model.py file in this directory!!
			 # all import statements are importing a file or folder that
			 # exists somewhere !!! That this program has access to!
import view

pygame.init()

surface = pygame.display.set_mode((800,600))
font = pygame.font.Font(None, 20)

pygame.display.set_caption("Scatterplot")

data = model.get_data('data.csv')
scatter = view.ScatterPlot(data, surface, font)

loop = True
while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False

	scatter.draw()
	pygame.display.update()

pygame.quit()
quit()
