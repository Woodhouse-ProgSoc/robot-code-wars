from abc import ABC, abstractmethod
import math
import pygame
import time


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class Robot(ABC):
	"""
	The base class for all the robots
	"""

	SPEED = 100
	"""
	Number of pixels all robots move per second
	"""

	ATTACK_RADIUS_SQUARED = 2500
	"""
	The square of the attack radius in pixels. It is squared so that we don't have to do a square root operation every frame.
	"""

	ATTACK_RATE = 10
	"""
	Number of hp lost per second when the robot is within the attack radius of another robot
	"""

	def __init__(self):
		self.hp = 100
		self.x = 0
		self.y = 0

	def update(self):
		angle = self.calcDirection()

		# update x and y coordinates
		# we use cos and sin to convert the angle into a vector
		self.x += math.cos(angle) * Robot.SPEED * deltaTime
		self.y += math.sin(angle) * Robot.SPEED * deltaTime

		# decrease hp of robots within attack radius
		for robot in robots:
			if abs(self.x - robot.x) ** 2 + abs(self.y - robot.y) ** 2 < Robot.ATTACK_RADIUS_SQUARED:
				robot.hp -= Robot.ATTACK_RATE * deltaTime

	@abstractmethod
	def calcDirection(self) -> float:
		"""
		This is called each frame and calculates the direction in which the robot will move.
		:return: The angle in radians (0 is to the right and it increases anticlockwise)
		"""

		pass

	@abstractmethod
	def draw(self) -> None:
		"""
		Called each frame to draw the robot onto the screen.
		"""

		pass


def update():
	pass


def draw():
	pass


robots = []
"""
A list of all the robots on the screen.
"""

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
"""
The Pygame `Surface` that represents the screen
"""

pygame.display.set_caption("ProgSoc Robot Code")
pygame.init()

running = True
while running:
	initialTime = time.time()

	# handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	update()
	draw()

	# show current frame on the screen
	pygame.display.flip()

	# calculate change in time
	deltaTime = time.time() - initialTime
	"""
	The time it took to perform the last frame. Multiply by this value to get smooth movement.
	"""
