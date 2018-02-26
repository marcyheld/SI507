import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)


class Bar:
	def __init__(self, color, length, height, padding=0.1):
		self.length = length
		self.color = color
		self.height = height
		self.padding = padding

	def draw(self, surface, x, y):
		padding_height = self.height * self.padding
		adjusted_height = self.height - 2 * padding_height
		pygame.draw.rect(surface, self.color, 
		  [x, y + padding_height, self.length, adjusted_height])


# a class to display a horizontal bar chart in pygame
class BarChart:

	# rect: a pygame.rect encoding size and position
	def __init__(self, rect, values=[]):
		self.rect = rect
		self.background = BLACK
		self.label_color = WHITE

		# constant ratios for portions of the display
		self.label_area_width_ratio = 0.2
		self.scale_area_height_ratio = 0.2
		self.plot_area_width_ratio = 1.0 - self.label_area_width_ratio
		self.plot_area_height_ratio = 1.0 - self.scale_area_height_ratio

		self.scale_area = pygame.Rect(
			rect.x + rect.width * self.label_area_width_ratio,
			rect.y + rect.height * self.plot_area_height_ratio,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.scale_area_height_ratio
			)

		self.label_area = pygame.Rect(
			rect.x,
			rect.y,
			rect.width * self.label_area_width_ratio,
			rect.height * self.plot_area_height_ratio
			)

		self.plot_area = pygame.Rect(
			rect.x + self.label_area.width,
			rect.y,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.plot_area_height_ratio
			)

		self.set_values(values)

	def set_values(self, values):
		self.values = values

		# figure out max value
		max_val = 0
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

			font = pygame.font.Font(None, 36)
			label_view = font.render(label_text, False, WHITE)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.y + \
			  self.get_bar_height() * bar_num + \
			  self.get_bar_height() / 2 
			label_pos.x = self.rect.x + 10
			surface.blit(label_view, label_pos)
			bar_num += 1
						
	def draw_scale(self, surface):
		scale_label_spacing = self.scale_area.width / self.max_val

		for i in range(self.max_val):
			font = pygame.font.Font(None, 36)
			scale_label_view = font.render(str(i), False, WHITE)
			scale_label_pos = scale_label_view.get_rect()
			scale_label_pos.y = self.scale_area.y + 10
			scale_label_pos.x = self.scale_area.x + \
			  i * scale_label_spacing
			surface.blit(scale_label_view, scale_label_pos)

	def draw_bars(self, surface):                
		bar_num = 0
		colors = [YELLOW, CYAN, MAGENTA, RED, BLUE, GREEN, WHITE]
		for v in self.values:
			bar_length = self.plot_area.width * v[1] / self.max_val
			b = Bar(colors[bar_num % len(colors)], 
			  bar_length, 
			  self.plot_area.height / len(self.values))
			y_pos = self.plot_area.y + bar_num * b.height
			bar_num += 1
			b.draw(surface, self.plot_area.x, y_pos)
						
	# and update the BarChart.draw() method        
	def draw(self, surface):
		self.draw_bars(surface)                
		self.draw_labels(surface)
		self.draw_scale(surface)


