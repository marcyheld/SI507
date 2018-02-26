import pygame
from barchart import BarChart
from button import Button
import fruitmodel

class DataChangeButton(Button):

	def __init__(self, text, rect, chart):
		Button.__init__(self, text, rect)
		self.chart = chart
		self.sorted = False

	def on_click(self, event):
		# we wil just toggle between sorted and unsorted data
		if (self.sorted):
			data = fruitmodel.get_data()
			self.sorted = False

		else:
			data = fruitmodel.get_sorted_data()
			self.sorted = True

		self.chart.set_values(data)

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Bar Chart Viewer")
pygame.display.update()

data1 = fruitmodel.get_data()

screen_rect = screen.get_rect()
bc1_rect = pygame.Rect(screen_rect.x, screen_rect.y, 
  screen_rect.width, screen_rect.height) # make it the full height again

bc1 = BarChart(bc1_rect, data1)

button = DataChangeButton("Change", pygame.Rect(10, screen_rect.height - 70, 150, 60), bc1)

# display loop
done = False
while not done:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			button.handle_event(event)

	bc1.draw(screen)
	button.draw(screen)
	pygame.display.update()

pygame.quit()

