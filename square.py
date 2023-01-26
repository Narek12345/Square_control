"""Создание спрайта квадрата."""

import pygame

from settings import SettingsGame


# Создание экземпляра класса SettingsGame.
sett_game = SettingsGame()


class Square(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(sett_game.game_colors("green"))
		self.rect = self.image.get_rect()
		self.rect.center = (sett_game.WIDTH / 2, sett_game.HEIGHT / 2)


	def movement_to_right(self):
		"""Движение вправо."""
		self.rect.x += 5


	def movement_to_left(self):
		"""Движение влево."""
		self.rect.x -= 5


	def movement_to_up(self):
		"""Движение вверх."""
		self.rect.y -= 5


	def movement_to_down(self):
		"""Движение вниз."""
		self.rect.y += 5