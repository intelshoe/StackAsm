import pygame
import os
import time
from button import Button

pygame.display.set_caption("StackAsm")


#application width and height
w = 800
h = 800
screen = pygame.display.set_mode((w, h))

# set background variables
bg = pygame.image.load(os.path.join("assets\\bg", "forest.jpg"))

# set button images and scale
buttons = []
for x in range(6): 
	b = pygame.image.load(os.path.join("assets\\buttons", f"{x}.png"))
	b = pygame.transform.scale(b, (80, 80))
	b.convert()
	buttons.append(b)

#setup button position and vars for moving
imgX = 0
imgY = 0
mouseStartX = mouseStartY = mouseEndX = mouseEndY = 0
focus = None
button_pos = []
y = 0

for x in range(6):
	button_pos.append([imgX, imgY])
	imgY += 84


run = True
clock = pygame.time.Clock()
while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
					run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if buttons[0].get_rect().move(imgX, imgY).collidepoint(pygame.mouse.get_pos()):
					focus = 'image'
					mouseStartX, mouseStartY = pygame.mouse.get_pos()
			else:
				focus = None
		if focus == 'image' and event.type == pygame.MOUSEBUTTONUP:
			mouseEndX, mouseEndY = pygame.mouse.get_pos()
			deltaMouseX = mouseEndX - mouseStartX
			deltaMouseY = mouseEndY - mouseStartY
			imgX += deltaMouseX
			imgY += deltaMouseY
			button_pos[0] = ([imgX, imgY])
		elif focus == "image":
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				imgY -= 3
			if keys[pygame.K_s]:
				imgY += 3
			if keys[pygame.K_a]:
				imgX -= 3
			if keys[pygame.K_d]:
				imgX += 3
			button_pos[x] = (imgX, imgY)

		

	screen.blit(bg, (0,0))
	for x in range (6):
		screen.blit(buttons[x], button_pos[x])
	
	pygame.display.update()
pygame.quit()
	
