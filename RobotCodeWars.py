from abc import ABC, abstractmethod
import math
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

robots = []
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("ProgSoc Robot Code")
red = (255, 0, 0)
screen.fill(red)

pygame.init()


class Robot(ABC):
	SPEED = 100
	ATTACK_RADIUS_SQUARED = 2500
	ATTACK_RATE = 10

	def __init__(self):
		self.health = 100
		self.x = 0
		self.y = 0

	def update(self):
		angle = self.calcDirection()

		self.x += math.cos(angle) * Robot.SPEED
		self.y += math.sin(angle) * Robot.SPEED

		for robot in robots:
			if abs(self.x - robot.x) ** 2 + abs(self.y - robot.y) ** 2 < Robot.ATTACK_RADIUS_SQUARED:
				robot.health -= 10

	@abstractmethod
	def calcDirection(self):
		pass

	@abstractmethod
	def draw(self):
		pass


running = True

while running:
	screen.fill(red)

	initialTime = time.time()

	# handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			print("Quitting Game")

	update()
	draw()

	pygame.display.flip()

	deltaTime = time.time() - initialTime

