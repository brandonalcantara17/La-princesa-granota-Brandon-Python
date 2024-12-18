import pygame
import random
import sys
pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
MAX_FROG_COUNT = 100

prince_image = pygame.image.load('images/princep.png')
frog_image = pygame.image.load('images/granota.png')
background_image = pygame.image.load('images/background.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
PRINCE_SIZE = prince_image.get_rect().size
FROG_SIZE = frog_image.get_rect().size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("La princesa granota")

class Prince:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

    def draw(self):
        screen.blit(prince_image, (self.x, self.y))

    def move(self, dx, dy):
        self.x = max(0, min(SCREEN_WIDTH - PRINCE_SIZE[0], self.x + dx))
        self.y = max(0, min(SCREEN_HEIGHT - PRINCE_SIZE[1], self.y + dy))

class Frog:
    def __init__(self, x, y, is_princess=False):
        self.x = x
        self.y = y
        self.is_princess = is_princess

    def draw(self):
        screen.blit(frog_image, (self.x, self.y))

    def move_random(self):
        self.x = random.randint(0, SCREEN_WIDTH - FROG_SIZE[0])
        self.y = random.randint(0, SCREEN_HEIGHT - FROG_SIZE[1])

def main():
    prince = Prince()
    frogs = [Frog(random.randint(0, SCREEN_WIDTH - FROG_SIZE[0]), random.randint(0, SCREEN_HEIGHT - FROG_SIZE[1]), i == 0) 
             for i in range(5)]

    clock = pygame.time.Clock()

    while True:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            prince.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            prince.move(5, 0)
        if keys[pygame.K_UP]:
            prince.move(0, -5)
        if keys[pygame.K_DOWN]:
            prince.move(0, 5)

        for frog in frogs:
            frog.draw()
            if (prince.x < frog.x + FROG_SIZE[0] and prince.x + PRINCE_SIZE[0] > frog.x and
               prince.y < frog.y + FROG_SIZE[1] and prince.y + PRINCE_SIZE[1] > frog.y):
                if frog.is_princess:
                    print("trobat")
                    pygame.quit()
                    sys.exit()
                else:
                    print("no es la princesa, torna a intentar")
                    prince.x, prince.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
                    for f in frogs:
                        f.move_random()
                    if len(frogs) < MAX_FROG_COUNT:
                        frogs.append(Frog(random.randint(0, SCREEN_WIDTH - FROG_SIZE[0]), random.randint(0, SCREEN_HEIGHT - FROG_SIZE[1])))

        prince.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()