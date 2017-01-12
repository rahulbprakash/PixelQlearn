import pygame
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption('wall pong')
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)
    
    #pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
