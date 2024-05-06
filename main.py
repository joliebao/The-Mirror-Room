import pygame

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Garamond', 60)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (1200, 800)
screen = pygame.display.set_mode(size)
title = "The Mirror Room"
display_title = my_font.render(title, True, (255,255,255))

bg = pygame.image.load("antique backdrop 1.jpg")

change_panel = False
run = True
# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            change_panel = True

    if change_panel == False:
        screen.fill((0, 0, 0))
        screen.blit(display_title, (385, 350))
    elif change_panel == True:
        screen.blit(bg, (0,0))
    pygame.display.update()
