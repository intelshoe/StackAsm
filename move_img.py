import pygame

def move_img(img):
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
	ruturn imgX, imgY	