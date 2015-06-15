import pygame

class interface:

	def __init__(self,clarity,fullscreen):
		pygame.init()
		pygame.mouse.set_visible(False)
		self.width = info.current_w
		self.high = info.current_h
		if fullscreen:
			self.pantalla = pygame.display.set_mode((self.width,self.high),pygame.FULLSCREEN)
		else:
			self.pantalla = pygame.display.set_mode((self.width,self.high))
		self.pantalla.set_alpha(clarity)

