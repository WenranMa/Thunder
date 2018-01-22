import pygame

WIDTH = 480
HEIGHT = 800
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Init and Create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Thunder")
clock = pygame.time.Clock()

#Game Loop
running = True
while running:

	clock.tick(FPS)

	#1. Process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	
	#2. Update
	
	#3. Draw/Render
	screen.fill(BLACK)
	
	#Double buffering
	pygame.display.flip()	
	

pygame.quit()
exit()