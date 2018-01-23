#A Thunder game
import pygame
import random

WIDTH = 480
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Init and Create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Thunder")
clock = pygame.time.Clock()

#key classes:

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((50, 40))
		#self.image.fill(GREEN)
		self.image = pygame.image.load('img/spaceShip.png')
		self.image = pygame.transform.rotozoom(self.image, 180, 0.5)	
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 10
		self.speedx = 0
	
	def update(self):		
		self.speedx = 0
	
		pressedKeys = pygame.key.get_pressed()
		if pressedKeys[pygame.K_RIGHT] == 1:
			self.speedx = 5
		if pressedKeys[pygame.K_LEFT] == 1:
			self.speedx = -5
		'''	
		if pressedKeys[pygame.K_SPACE] == 1:
			self.shoot()
		'''		
		self.rect.x += self.speedx
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
	
	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		spriteGroup.add(bullet)
		bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10, 20))
		#self.image.fill(YELLOW)
		self.image = pygame.image.load('img/spaceMissile.png')
		
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y
		self.speedy = -10
	
	def update(self):		
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()
			
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((30, 40))
		#self.image.fill(RED)
		self.image = pygame.image.load('img/spaceMeteor.png')
		self.image = pygame.transform.scale(self.image, (50, 40))	

		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 8)
		self.speedx = random.randrange(-2, 2)
	
	def update(self):		
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)
				

spriteGroup = pygame.sprite.Group()

player = Player()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
for i in range(8):
	enemy = Enemy()
	spriteGroup.add(enemy)
	enemies.add(enemy)

spriteGroup.add(player)

#Game Loop
running = True
while running:

	clock.tick(FPS)

	#1. Process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()
	
	#2. Update
	spriteGroup.update()
	
	# Check collision
	
	hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
	for hit in hits:
		enemy = Enemy()
		spriteGroup.add(enemy)
		enemies.add(enemy)
	
	hits = pygame.sprite.spritecollide(player, enemies, False)
	if hits:
		running = False
	
	#3. Draw/Render
	screen.fill(BLACK)
	spriteGroup.draw(screen)
	
	#Double buffering
	pygame.display.flip()	
	
pygame.quit()
exit()