"""Главные настройки игры."""

import time
import pygame


class SettingsGame():
	def __init__(self):

		# Создание констант ширины и высоты экрана.
		self.WIDTH = 500
		self.HEIGHT = 500

		# Создание константы список для хранения всех добавленых спрайтов.
		self.ALL_SPRITES = pygame.sprite.Group()


	def create_and_output_display(self):
		"""Создание и вывод окна."""

		# Создание окна и вывод созданного окна.
		display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

		return display


	def game_colors(self, color_name):
		"""Выводит словарь с цветами {'color_name': 'RGB'} в формате RGB."""

		# Создаем словарь с цветами и затем выводим его.
		dict_colors = {
			'black': (0, 0, 0),
			'white': (255, 255, 255),
			'red': (255, 0, 0),
			'green': (0, 255, 0),
			'blue': (0, 0, 255),
		}

		# Перед проверкой превращаем введеные данные пользователя в нижний регистр и заранее убираем все лишние пропуски.
		color_name = color_name.lower().strip()

		# Разбираем словарь и выводим нужный нам цвет.
		for color_names, color_values in dict_colors.items():
			if color_name == color_names:
				return color_values

		return "Цвет не найден."


	def add_sprites(self, sprite):
		"""Добавление спрайтов в список спрайтов. Псоле добавления в этот список, спрайты будут атвоматически выведены на экран."""

		self.ALL_SPRITES.add(sprite)


	def update_sprites(self):
		"""Обновление спрайтов."""

		self.ALL_SPRITES.update()


	def rendering_all_sprites(self):
		"""Отрисовка всех спрайтов."""

		self.ALL_SPRITES.draw(self.create_and_output_display())