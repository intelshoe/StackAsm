import pygame
import os
import time

btn_total = 6

# application window size
w = 800
h = 800
screen = pygame.display.set_mode((w, h))

# sets window icon and caption
sa_icon = pygame.image.load("sa_icon.jpg")
sa_icon = pygame.transform.scale(sa_icon, (32, 32))
sa_icon.convert()
pygame.display.set_icon(sa_icon)
pygame.display.set_caption("StackAsm")

# set background variables
bg = pygame.image.load(os.path.join("assets\\bg", "forest.jpg"))

# set button images and scale
buttons = []
for x in range(btn_total): 
	buttons.append(pygame.image.load(os.path.join("assets\\buttons", f"{x}.png")))
	buttons[x] = pygame.transform.scale(buttons[x], (80, 80))
	buttons[x].convert()
# set button start position variables
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

# moves the buttons if clicked
def move_img(img, index):
	global focus, imgX, imgY, startY
	if event.type == pygame.MOUSEBUTTONDOWN:
		if img.get_rect().move(imgX[index], imgY[index]).collidepoint(pygame.mouse.get_pos()):
			focus[index] = 'image'
		else:
			focus[index] = None
	# controls keys for moving buttons
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
		# put button to start if R key pressed
		if keys[pygame.K_r]:
			imgX[index] = 0
			imgY[index] = startY[index]
	return (imgX[index], imgY[index])

# actual app loop
run = True
clock = pygame.time.Clock()
clock.tick(60)
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False  # quits app if X pressed

	# print buttons and background to screen
	screen.blit(bg, (0,0)) # bg
	for x in range(btn_total):
		screen.blit(buttons[x], move_img(buttons[x], x))
	pygame.display.update()

# quit if X is clicked
pygame.quit()
	