import pygame

# Setup Start
pygame.init()
window = pygame.display.set_mode(size=(1600, 900))
# Setup End
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            quit() # End pygame


