import pygame
import parse_asm

pygame.init()

screen = pygame.display.set_mode((800, 800))
bg = pygame.image.load("forest.jpg")
running = True

while running:
	# Check for input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Update game elements

	# Call function to parse Assembly input
	# renders blocks and text as needed

	# Draw and show game surface
	screen.blit(bg, bg.get_rect())
	pygame.display.update()

pygame.quit()
