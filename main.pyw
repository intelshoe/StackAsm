import pygame
import os
import time

pygame.display.set_caption("StackAsm")

btn_total = 6

#application width and height
w = 800
h = 800
screen = pygame.display.set_mode((w, h))

# set background variables
bg = pygame.image.load(os.path.join("assets\\bg", "forest.jpg"))

# set button images and scale
buttons = []
for x in range(btn_total): 
	buttons.append(pygame.image.load(os.path.join("assets\\buttons", f"{x}.png")))
	buttons[x] = pygame.transform.scale(buttons[x], (80, 80))
	buttons[x].convert()

focus = []
imgX = []
imgY = []
startY = []
i = 0
for x in range(btn_total):
	focus.append(None)
	imgX.append(0)
	imgY.append(i)
	startY.append(i)
	i += 84


def move_img(img, index):
	global focus, imgX, imgY, startY
	if event.type == pygame.MOUSEBUTTONDOWN:
		# imgX, imgY = pygame.mouse.get_pos()
		if img.get_rect().move(imgX[index], imgY[index]).collidepoint(pygame.mouse.get_pos()):
			focus[index] = 'image'
		else:
			focus[index] = None
	if focus[index] == "image":
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			imgY[index] -= .5
		if keys[pygame.K_s]:
			imgY[index] += .5
		if keys[pygame.K_a]:
			imgX[index] -= .5
		if keys[pygame.K_d]:
			imgX[index] += .5
		if keys[pygame.K_r]:
			imgX[index] = 0
			imgY[index] = startY[index]
	return (imgX[index], imgY[index])


run = True
clock = pygame.time.Clock()
clock.tick(60)
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		

	screen.blit(bg, (0,0))

	for x in range(btn_total):
		screen.blit(buttons[x], move_img(buttons[x], x))

	pygame.display.update()
pygame.quit()
	
