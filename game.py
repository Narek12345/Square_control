"""Главный файл самой игры."""

import time
import pygame

from square import Square
from settings import SettingsGame


# Создаем экземпляр спрайта Square.
square = Square()
# Создаем экземпляр класса SettngsGame.
sett_game = SettingsGame()


class Game():
	def __init__(self):
		"""Подготовка к запуску игры."""

		# Создание окна.
		self.display = sett_game.create_and_output_display()
		# Изменение цвета окна.
		self.display.fill(sett_game.game_colors("white"))

		# Создание FPS.
		self.FPS = 20
		self.fps_clock = pygame.time.Clock()

		# Добавление спрайтов в игру.
		sett_game.add_sprites(square)
		# Обновление доблавний спрайтов в игру.
		sett_game.update_sprites()

		# Запуск игры.
		self.start_game()


	def start_game(self):
		"""Запуск игры."""

		# Переменные для контроля игры.
		run_game = True

		def stop_game_func(self):
			"""Стоп игра."""
			# Стоп игра.
			while stop_game:
				# Контроль FPS.
				self.fps_clock.tick(self.FPS)

		# Запуск главного цикла игры.
		while run_game:
			# Контроль FPS.
			self.fps_clock.tick(self.FPS)

			# Разбор событий.
			for event in pygame.event.get():
				# Проверка на выход из игры.
				if event.type == pygame.QUIT:
					run_game = False

				# Проверка на нажатия клавиш.
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						square.movement_to_right()
					elif event.key == pygame.K_LEFT:
						square.movement_to_left()
					elif event.key == pygame.K_UP:
						square.movement_to_up()
					elif event.key == pygame.K_DOWN:
						square.movement_to_down()


			# Добавление спрайтов в игру.
			sett_game.add_sprites(square)
			# Обновление доблавний спрайтов в игру.
			sett_game.update_sprites()

			sett_game.rendering_all_sprites()

			# Обновляем экран.
			pygame.display.update()



game = Game()