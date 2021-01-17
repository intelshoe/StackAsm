import pygame
import sys

pygame.init()

background_position=[0,0]
screen = pygame.display.set_mode((800, 800))
bg = pygame.image.load("forest.jpg")
button = pygame.image.load("easy.png")
running = True

while running:
	# Check for input
	for event in pygame.event.get():
		# close program if x clicked
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			

	# Update game elements

	# Call function to parse Assembly input
	# renders blocks and text as needed

	# Draw and show game surface
	screen.blit(bg, background_position)
	pygame.display.update()

pygame.quit()