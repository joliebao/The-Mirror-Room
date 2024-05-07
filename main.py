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
display_title = my_font.render(title, True, (249,234,199))

bg1 = pygame.image.load("antique backdrop 1.jpg")
text_box = pygame.image.load("text box.png")

change_panel = False
run = True
interaction = False
counter = 0

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            change_panel = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            counter += 1
            print (counter)
        if counter % 2 == 0:
            interaction = False
        else:
            interaction = True

    if not change_panel:      # starting screen
        screen.fill((75, 43, 10))
        screen.blit(display_title, (385, 350))
    elif change_panel:
        screen.blit(bg1, (0, 0))

    if interaction == True:
        screen.blit(text_box, (150, 130))

    pygame.display.update()
