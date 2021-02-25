from abc import ABC, abstractmethod
import math
import pygame
import time
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class GameObj(ABC):
	def __init__(self, x, y):
		self.x = x
		"""
		The x coordinate of the center of the object
		"""

		self.y = y
		"""
		The y coordinate of the center of the object
		"""

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def draw(self):
		pass


class Robot(GameObj, ABC):
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

	def __init__(self, x, y):
		super().__init__()

		self.hp = 100
		"""
		The current health of the robot
		"""

	def update(self):
		angle = self.calcDirection()

		# update x and y coordinates
		# we use cos and sin to convert the angle into a vector
		self.x += math.cos(angle) * Robot.SPEED * deltaTime
		self.y += math.sin(angle) * Robot.SPEED * deltaTime

		# decrease hp of robots within attack radius
		for robot in robots:
			if abs(self.x - robot.x) ** 2 + abs(self.y - robot.y) ** 2 < Robot.ATTACK_RADIUS_SQUARED:
				robot.hp -= 10

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


class TestRobot(Robot):
	def calcDirection(self):
		return random.uniform(0, 2 * math.pi)

	def draw(self):
		pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 50)


def update():
	for robot in robots:
		robot.update()


def draw():
	# Background draw
	screen.blit(background, (0, 0))

	# calling the draw function of each robot
	for robot in robots:
		robot.draw()

	pygame.display.flip()


robots: list[GameObj] = []
"""
A list of all the robots on the screen.
"""

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
"""
The Pygame `Surface` that represents the screen
"""

deltaTime = 0
"""
The time it took to perform the last frame. Multiply by this value to get smooth movement.
"""

pygame.display.set_caption("ProgSoc Robot Code Wars")
background = pygame.image.load("background.jpg")

pygame.init()

# test
for i in range(5):
	newRobot = TestRobot(
		random.uniform(0, SCREEN_WIDTH),
		random.uniform(0, SCREEN_HEIGHT)
	)
	robots.append(newRobot)

running = True

while running:
	initialTime = time.time()

	# handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			print("Quitting Game")

	update()
	draw()

	# calculate change in time
	deltaTime = time.time() - initialTime
