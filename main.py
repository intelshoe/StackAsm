import pygame

pygame.init()

background_position=[0,0]
screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("StackAsm")
bg = pygame.image.load("forest.jpg")
img = pygame.image.load("easy.jpg")
img = pygame.transform.scale(img, (80, 80))
img2 = pygame.image.load("easy.jpg")
img2 = pygame.transform.scale(img, (80, 80))

img_list = [img, img2]


#setup button1 position
imgX = 800 * 0.45
imgY = 800 * 0.4
mouseStartX = mouseStartY = mouseEndX = mouseEndY = 0


focus = None
running = True
MAX_FPS = 60
clock = pygame.time.Clock()


def move_img(img):
	global focus, imgX, imgY, mouseStartX, mouseStartY, mouseEndX, mouseEndY
	if event.type == pygame.MOUSEBUTTONDOWN:
		# imgX, imgY = pygame.mouse.get_pos()
		if img.get_rect().move(imgX, imgY).collidepoint(pygame.mouse.get_pos()):
			focus = 'image'
			mouseStartX, mouseStartY = pygame.mouse.get_pos()
		else:
			focus = None
	elif focus == 'image' and event.type == pygame.MOUSEBUTTONUP:
		mouseEndX, mouseEndY = pygame.mouse.get_pos()
		deltaMouseX = mouseEndX - mouseStartX
		deltaMouseY = mouseEndY - mouseStartY
		imgX += deltaMouseX
		imgY += deltaMouseY	
	if focus == "image":
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			imgY -= 3
		if keys[pygame.K_s]:
			imgY += 3
		if keys[pygame.K_a]:
			imgX -= 3
		if keys[pygame.K_d]:
			imgX += 3
	return [imgX,imgY]	


while running:
	# Check for input
	for event in pygame.event.get():
		# close program if x clicked
		if event.type == pygame.QUIT:
			running = False


	screen.blit(img, move_img(img))
	screen.blit(img2, move_img(img2))
	screen.blit(bg, background_position)
	pygame.display.update()
	# pause for frames
	clock.tick(MAX_FPS)


pygame.quit()