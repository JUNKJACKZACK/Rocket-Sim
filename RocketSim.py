import pygame
import os

WIDTH, HEIGHT = 900,1200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Sim")

WHITE = 255, 255, 255

FPS = 60

ROCKET_IMAGE = pygame.image.load(os.path.join('Assets', 'rocket_shuttle.png'))
ROCKET_TEST = pygame.transform.scale(ROCKET_IMAGE, (150, 150))

ROCKET_START_POS = 400, 1500

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(ROCKET_TEST, (draw_rocket.x, draw_rocket.y))
    pygame.display.update()



def main(): 
    
    draw_rocket = pygame.Rect(400, 1500, 150, 150)
    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
                
    pygame.quit()
    
if __name__ == "__main__":
    main()
    