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

class Button:
		
	def __init__(self, text, rect):
		self.text = text
		self.rect = rect

	def draw(self, surface):
		pygame.draw.rect(surface, GRAY, self.rect)

		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			(x, y) = pygame.mouse.get_pos()
			if x >= self.rect.x and \
				x <= self.rect.x + self.rect.width and \
				y >= self.rect.y and \
				y <= self.rect.y + self.rect.height:
				
				self.on_click(event)

	def on_click(self, event):
		print("button clicked")


