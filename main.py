# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#													        #
#			         Python Pixel Editor					#
#			          Developer: Carbon				        #
#													   	    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

import pygame
import random

# Colors: #

from colors import *

# Pygame Initialization: 

pygame.init()

# Editor Variables: #

editorRunning = True

drawingColor = blackColor

rows = columns = 30

# Window: #

screenWidth = 600
screenHeight = 700

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Python Pixel Editor: ')

# Tool Bar: #

toolbarHeight = screenHeight - screenWidth

# Pixel Size: #

pixelSize = screenWidth // columns

# Editor Icon: #

icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# Grid Settings: #

drawGridLines = True

# FPS Handler: #

handleFPS = pygame.time.Clock()

# Button Class: #

class Button():
	def __init__(self, x : int, y : int, width : int, height : int, color : tuple, text = None, textColor = blackColor):
		self.x = x
		self.y = y 
		self.width = width
		self.height = height 
		self.color = color 
		self.text = text
		self.textColor = textColor

	def draw(self, window : pygame.Surface):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
		pygame.draw.rect(window, blackColor, (self.x, self.y, self.width, self.height), 2)

		if(self.text):
			buttonFont = pygame.font.SysFont('System', 30)
			textSurface = buttonFont.render(self.text, 1, self.textColor)
			window.blit(textSurface, (self.x + self.width / 2 - textSurface.get_width() / 2, self.y + self.height / 2 - textSurface.get_height() / 2))

	def isClicked(self, position : tuple):
		x, y = position
		if(not (x >= self.x and x <= self.x + self.width)):
			return False

		if(not (y >= self.y and y <= self.y + self.height)):
			return False

		return True

# Buttons: #

buttons = [
	Button(10, screenHeight - toolbarHeight / 2 - 25, 20, 20, whiteColor),
	Button(35, screenHeight - toolbarHeight / 2 - 25, 20, 20, redColor),
	Button(60, screenHeight - toolbarHeight / 2 - 25, 20, 20, blueColor),
	Button(85, screenHeight - toolbarHeight / 2 - 25, 20, 20, greenColor),
	Button(110, screenHeight - toolbarHeight / 2 - 25, 20, 20, blueVioletColor),
	Button(135, screenHeight - toolbarHeight / 2 - 25, 20, 20, limeColor),
	Button(160, screenHeight - toolbarHeight / 2 - 25, 20, 20, oliveColor),
	Button(185, screenHeight - toolbarHeight / 2 - 25, 20, 20, steelBlue),
	Button(210, screenHeight - toolbarHeight / 2 - 25, 20, 20, lightYellow),
	Button(235, screenHeight - toolbarHeight / 2 - 25, 20, 20, darkBrown),
	Button(260, screenHeight - toolbarHeight / 2 - 25, 20, 20, darkPink),
	Button(285, screenHeight - toolbarHeight / 2 - 25, 20, 20, lightRed),
	Button(10, screenHeight - toolbarHeight / 2, 20, 20, cyanColor),
	Button(35, screenHeight - toolbarHeight / 2, 20, 20, yellowColor),
	Button(60, screenHeight - toolbarHeight / 2, 20, 20, brownColor),
	Button(85, screenHeight - toolbarHeight / 2, 20, 20, pinkColor),
	Button(110, screenHeight - toolbarHeight / 2, 20, 20, plumColor),
	Button(135, screenHeight - toolbarHeight / 2, 20, 20, lightBrownColor),
	Button(160, screenHeight - toolbarHeight / 2, 20, 20, lightPinkColor),
	Button(185, screenHeight - toolbarHeight / 2, 20, 20, greyColor),
	Button(210, screenHeight - toolbarHeight / 2, 20, 20, darkBlue),
	Button(235, screenHeight - toolbarHeight / 2, 20, 20, lightGreen),
	Button(260, screenHeight - toolbarHeight / 2, 20, 20, skyBlue),
	Button(285, screenHeight - toolbarHeight / 2, 20, 20, darkGrey),
	Button(510, screenHeight - toolbarHeight / 2 - 40, 80, 40, whiteColor, "Erase", blackColor),
	Button(420, screenHeight - toolbarHeight / 2 - 40, 80, 40, whiteColor, "Clear", blackColor),
	Button(420, screenHeight - toolbarHeight / 2 + 5, 170, 40, whiteColor, "Screenshot", blackColor),
	Button(330, screenHeight - toolbarHeight / 2 - 20, 80, 40, whiteColor, "Grid", blackColor)
]

# Editor Functions: #

def screenShot():
	pictureID = 0
	size = pygame.Rect(0, 0, screenWidth, screenHeight - toolbarHeight)
	subSurface = window.subsurface(size)
	screenshot = pygame.Surface((screenWidth, screenHeight - toolbarHeight))
	screenshot.blit(subSurface, (0,0))
	for i in range(10):
	    randomInt = random.randint(0, 255)
	    pictureID = randomInt
	pygame.image.save(screenshot, f"picture_{pictureID}.jpg")
	pictureID = 0

def initGrid(rows : int, columns : int, color : tuple):
	grid = []
	for i in range(rows):
		grid.append([])
		for j in range(columns):
			grid[i].append(color)

	return grid

def drawGrid(window : pygame.Surface, grid : list):
	for i, row in enumerate(grid):
		for j, pixel in enumerate(row):
			pygame.draw.rect(window, pixel, (j * pixelSize, i * pixelSize, pixelSize, pixelSize))

	if(drawGridLines):
		for i in range(rows + 1):
			pygame.draw.line(window, blackColor, (0, i * pixelSize), (screenWidth, i * pixelSize))

		for i in range(columns + 1):
			pygame.draw.line(window, blackColor, (i * pixelSize, 0), (i * pixelSize, screenHeight - toolbarHeight))

def getPosition(position : tuple):
	x, y = position
	column = x // pixelSize
	row = y // pixelSize

	if(row >= rows):
		raise IndexError

	return row, column

# Editor Mechanics: #

grid = initGrid(rows, columns, whiteColor)

# Editor Loop: #

while(editorRunning):
	handleFPS.tick(60)
	window.fill(barColor)
	drawGrid(window, grid)
	for i in range(len(buttons)):
		buttons[i].draw(window)
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			editorRunning = False

		if(pygame.mouse.get_pressed()[0]):
			position = pygame.mouse.get_pos()

			try:
				row, column = getPosition(position)
				grid[row][column] = drawingColor
			except IndexError:
				for i in range(len(buttons)):
					if(not (buttons[i].isClicked(position))):
						continue

					drawingColor = buttons[i].color
					if(buttons[i].text == "Clear"):
						grid = initGrid(rows, columns, whiteColor)
						drawingColor = blackColor

					if(buttons[i].text == "Screenshot"):
						screenShot()
						drawingColor = blackColor

					if(buttons[i].text == "Grid"):
						if(drawGridLines == True):
							drawGridLines = False
						else:
							drawGridLines = True
						drawingColor = blackColor

	pygame.display.update()
 

pygame.quit()
