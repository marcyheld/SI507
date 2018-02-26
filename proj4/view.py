import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# a class to display a horizontal bar chart in pygame
class BarChart:

	def __init__(self, rect=pygame.Rect(0,0,600,400), values=[], ticks=10, 
		plot_area_width_ratio=0.8, plot_area_height_ratio=0.8, bar_color=GREEN,
		max_val=0):

		self.rect = rect

		self.ticks = ticks

		self.label_area_width_ratio = 1 - plot_area_width_ratio
		self.scale_area_height_ratio = 1 - plot_area_height_ratio

		self.plot_area_width_ratio = plot_area_width_ratio * .8
		self.plot_area_height_ratio = plot_area_height_ratio

		self.bar_color = bar_color

		# find if any values are less than 1, this means we are dealing with percentages
		# this max_val gets passed to set_values() method at bottom of constructor
		for val in values:
			if val[1] < 1:
				max_val = 1

		self.scale_area = pygame.Rect(
            rect.x + rect.width * self.label_area_width_ratio,
            rect.y + rect.height * self.plot_area_height_ratio,
            rect.width * self.plot_area_width_ratio,
            rect.height * self.plot_area_height_ratio)

		self.label_area = pygame.Rect(
			rect.x,
			rect.y,
			(rect.width * self.label_area_width_ratio),
			(rect.height * self.plot_area_height_ratio))

		self.plot_area = pygame.Rect(
			rect.x + self.label_area.width,
			rect.y,
			(rect.width * self.plot_area_width_ratio),
			(rect.height * self.plot_area_height_ratio))

		self.set_values(values, max_val)

	def set_values(self, values, max_val):
		self.values = values
		self.max_val = max_val

		for v in values:
			if v[1] > max_val:
				max_val = v[1]
		self.max_val = max_val

	def get_bar_height(self):
		return self.plot_area.height / len(self.values)

	def draw_labels(self, surface):
		bar_num = 0
		for v in self.values:
			label_text = v[0]

			font = pygame.font.Font(None, 24)
			label_view = font.render(label_text, False, WHITE)

			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.y + self.get_bar_height() * bar_num + self.get_bar_height() / 2

			label_pos.x = self.rect.x + 10
			surface.blit(label_view, label_pos)

			bar_num += 1

	def draw_bars(self, surface):
		bar_num = 0 

		for v in self.values:
			if v[1] < 1: # changed from <= to <
				bar_length = (self.plot_area.width * v[1]) / (self.max_val / 100)

			else:
				bar_length = self.plot_area.width * v[1] / self.max_val

			b = Bar(self.bar_color, bar_length, self.plot_area.height / len(self.values))
			y_pos = self.plot_area.y + bar_num * b.height
			bar_num += 1
			b.draw(surface, self.plot_area.x, y_pos)

	def draw_scale(self, surface):
		scale_label_spacing = self.scale_area.width / self.max_val

		if self.max_val == 1:
			self.max_val = 100

		inc = self.max_val / (self.ticks - 1) # how we increase the value of a tick mark each time

		count = 0
		values_to_print_unrounded = []

		for i in range(self.ticks):
			values_to_print_unrounded.append(count)
			count += inc

		rounded_values_to_print = []

		for item in values_to_print_unrounded:
			rounded_values_to_print.append(int(item))

		if rounded_values_to_print[-1] != self.max_val:
			rounded_values_to_print[-1] = self.max_val

		spacing_count = 1
		for i in range(int(self.max_val) + 2):

			if i in rounded_values_to_print:

				font = pygame.font.Font(None, 24)
				scale_label_view = font.render(str(i), False, WHITE)
				scale_label_view = pygame.transform.rotate(scale_label_view, 90)
				scale_label_pos = scale_label_view.get_rect()
				scale_label_pos.y = self.scale_area.y + 10
				scale_label_pos.x = self.scale_area.x - 18 + (i * scale_label_spacing)
				surface.blit(scale_label_view, scale_label_pos)

				spacing_count += 5


	def draw(self, surface):
		self.draw_bars(surface)
		self.draw_labels(surface)
		self.draw_scale(surface)

class Bar:
    def __init__(self, color, length, height, padding=0.1):
        self.length = length
        self.color = color
        self.height = height
        self.padding = padding

    def draw(self, surface, x, y):
        padding_height = self.height * self.padding
        adjusted_height = self.height - 2 * padding_height
        pygame.draw.rect(surface, self.color, [x, y + padding_height, self.length, adjusted_height])

# SELF-TESTING MAIN
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((1000,700))

	pygame.display.set_caption("Bar Chart Test")
	pygame.display.update()

	data =	[
	 		("apples", 6), 
	 		("bananas", 7), 
 			("grapes", 4),
  			("pineapple", 1), # becaue thi
  			("cherries", 15)
        	]   

	# display using default values			
	bc = BarChart(values=data)

	data2 = [
			('Jenny', 80),
			('Stanley', 90),
			('Timothy', 92)
			]

	# override all of the defaults
	bc2 = BarChart(
		rect=pygame.Rect(0,400,800,150), 
		values=data2, 
		ticks=5, 
		plot_area_width_ratio=0.85, 
		plot_area_height_ratio=0.9, 
		bar_color=RED,
		max_val=100
		)

	# display loop
	done = False
	while not done:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		bc.draw(screen)
		bc2.draw(screen)
		pygame.display.update()	



