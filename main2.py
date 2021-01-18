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

#setup img1 position
imgX = 800 * 0.45
imgY = 800 * 0.4
mouseStartX = mouseStartY = mouseEndX = mouseEndY = 0
#setup img2 position
img2X = 800 * 0.45
img2Y = 800 * 0.4
mouse2StartX = mouse2StartY = mouse2EndX = mouse2EndY = 0

focus = None
running = True
MAX_FPS = 60
clock = pygame.time.Clock()

while running:
	# Check for input
	for event in pygame.event.get():
		# close program if x clicked
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# imgX, imgY = pygame.mouse.get_pos()
			if img.get_rect().move(imgX, imgY).collidepoint(pygame.mouse.get_pos()):
				focus = 'image'
				mouseStartX, mouseStartY = pygame.mouse.get_pos()
			elif img2.get_rect().move(img2X, img2Y).collidepoint(pygame.mouse.get_pos()):
				focus = 'image2'
				mouse2StartX, mouse2StartY = pygame.mouse.get_pos()
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
		elif focus == 'image2' and event.type == pygame.MOUSEBUTTONUP:
			mouse2EndX, mouse2EndY = pygame.mouse.get_pos()
			delta2MouseX = mouse2EndX - mouse2StartX
			delta2MouseY = mouse2EndY - mouse2StartY
			img2X += delta2MouseX
			img2Y += delta2MouseY	
		if focus == "image2":
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				img2Y -= 3
			if keys[pygame.K_s]:
				img2Y += 3
			if keys[pygame.K_a]:
				img2X -= 3
			if keys[pygame.K_d]:
				img2X += 3	

	screen.blit(bg, background_position)
	screen.blit(img, (imgX, imgY))
	screen.blit(img2, (img2X, img2Y))
	pygame.display.update()
	# pause for frames
	clock.tick(MAX_FPS)



pygame.quit()