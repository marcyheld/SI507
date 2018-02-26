import pygame
import view
import model

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

partySelection = "dem"
sort_ascendingSelection = False
rawSelection = False
maxValGlobal = 10000000

pygame.init()

screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()

data = model.get_data(party=partySelection, raw=rawSelection, sort_ascending=sort_ascendingSelection)
bc = view.BarChart(screen.get_rect(), values=data, ticks=5, plot_area_width_ratio = 0.95, max_val=10000000)


class Button:

	def __init__(self, text, rect):
		self.text = text
		self.rect = rect
		self.color = GRAY

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			(x,y) = pygame.mouse.get_pos()
			if x >= self.rect.x and \
				x <= self.rect.x + self.rect.width and \
				y >= self.rect.y and \
				y <= self.rect.y + self.rect.height:

				self.on_click(event)

	def on_click(self, event):
		print ("button clicked")


class DataChangeParty(Button):

	def __init__(self, party, rect, chart):
		Button.__init__(self, text=party, rect=rect)
		self.chart = chart
		self.party = party

	def on_click(self, event):
		global partySelection
		partySelection = self.party
		data = model.get_data(party=partySelection, raw=rawSelection, sort_ascending=sort_ascendingSelection)
		self.chart.set_values(data, self.chart.max_val)

	def draw(self, surface):
		global partySelection
		if partySelection == self.party:
			color = RED
		else:
			color = GRAY
		pygame.draw.rect(surface, color, self.rect)

		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)


class DataChangeAsc(Button):

	def __init__(self, text, rect, chart, sort_asc):
		Button.__init__(self, text, rect)
		self.chart = chart
		self.sort_asc = sort_asc

	def on_click(self, event):
		global sort_ascendingSelection
		sort_ascendingSelection = self.sort_asc
		data = model.get_data(party=partySelection, raw=rawSelection, sort_ascending=sort_ascendingSelection)
		self.chart.set_values(data, self.chart.max_val)

	def draw(self, surface):
		global sort_ascendingSelection
		if sort_ascendingSelection == self.sort_asc:
			color = RED
		else:
			color = GRAY

		pygame.draw.rect(surface, color, self.rect)

		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)

class DataChangeRaw (Button):

	def __init__(self, text, rect, chart, raw):
		Button.__init__(self, text, rect)
		self.chart = chart
		self.raw = raw

	def on_click(self, event):
		global rawSelection
		rawSelection = self.raw

		if rawSelection == True:
			maxValNow = maxValGlobal
		else:
			maxValNow = 100

		data = model.get_data(party=partySelection, raw=rawSelection, sort_ascending=sort_ascendingSelection)
		self.chart.set_values(data, maxValNow)

	def draw(self, surface):
		global rawSelection
		if rawSelection == self.raw:
			color = RED
		else:
			color = GRAY

		pygame.draw.rect(surface, color, self.rect)

		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)
		
dem_button = DataChangeParty("dem", pygame.Rect((screen_rect.width - 200), 30, 100, 40), bc)
gop_button = DataChangeParty("gop", pygame.Rect((screen_rect.width - 200), 70, 100, 40), bc)

up_button = DataChangeAsc("up", pygame.Rect((screen_rect.width - 200), 130, 100, 40), bc, True)
down_button = DataChangeAsc("down", pygame.Rect((screen_rect.width - 200), 170, 100, 40), bc, False)

raw_button = DataChangeRaw("raw", pygame.Rect((screen_rect.width - 200), 230, 100, 40), bc, True)
per_button = DataChangeRaw("%", pygame.Rect((screen_rect.width - 200), 270, 100, 40), bc, False)

# display loop
done = False
while not done:
	screen.fill(view.BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			gop_button.handle_event(event)
			dem_button.handle_event(event)
			up_button.handle_event(event)
			down_button.handle_event(event)
			raw_button.handle_event(event)
			per_button.handle_event(event)

	bc.draw(screen)
	dem_button.draw(screen)
	gop_button.draw(screen)
	up_button.draw(screen)
	down_button.draw(screen)
	raw_button.draw(screen)
	per_button.draw(screen)

	pygame.display.update()	


