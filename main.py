import pygame
from starter_box import Starter_box
from starter_box_1 import Starter_box_1
from board import Board
from girl import Girl
from radio import Radio

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Calisto', 60)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (1200, 800)
screen = pygame.display.set_mode(size)
title = "The Mirror Room"
click_one = "Click to start"
player_directions = "Pick a box (Click one):"
past = "Past"
present = "Present"

dialogues = ["Adeline is visiting her grandpa’s antique shop right before he is shutting it down", ", he is getting too old to continue…", "While walking around, she picks things up and examines them, wondering about their purposes and history.", "She stops before a mirror.", "Curious, she reaches out to touch the wood.", "In a flash, she is confined inside.", "Grandpa!? Where are you, and where am I!?", "Adeline! Did you touch the mirror while I wasn’t looking?!", "*sigh* It just had to be this mirror...", "Look around Addie and tell me what you see. I’ll get you out of there."
Ar: “Adeline! Did you touch the mirror while I wasn’t looking?!”
Ad: “But I only touched the frame!”
Ar: *sigh*, “It just had to be this mirror... Look around Addie and tell me what you see. I’ll get you out of there.”

Adeline is surprised to see a carbon copy of the store. The well-managed store looked more clean and less cluttered.

Ad: “Is this the store? It looks a lot newer.”
Ar: “The past. You’re in the past...”
"]

display_title = my_font.render(title, True, (249, 234, 199))
my_font = pygame.font.SysFont('Courier', 25)
display_click_one = my_font.render(click_one, True, (255, 255, 255))
my_font = pygame.font.SysFont('Bell', 50)
display_player_directions = my_font.render(player_directions, True, (255, 255, 255))
my_font = pygame.font.SysFont('Papyrus', 30)
display_past = my_font.render(past, True, (255, 255, 255))
display_present = my_font.render(present, True, (255, 255, 255))

bgstart = pygame.image.load("mirror background.jpg")
bg1 = pygame.image.load("antique backdrop 1.jpg")
text_box = pygame.image.load("text box.png")
closet = pygame.image.load("closet.png")
couch = pygame.image.load("couch.png")
clock = pygame.image.load("clock.png")
clock = pygame.transform.scale(clock, (167, 374))
shelf = pygame.image.load("shelf.png")
ladder = pygame.image.load("ladder.png")
ladder = pygame.transform.scale(ladder, (200, 300))
table = pygame.image.load("round table.png")
table = pygame.transform.scale(table, (481, 300))
table_2 = pygame.image.load("round table.png")
table_2 = pygame.transform.scale(table_2, (481, 300))
table_3 = pygame.image.load("round table.png")
table_3 = pygame.transform.scale(table_3, (481, 300))
lamp = pygame.image.load("lamp.png")
lamp = pygame.transform.scale(lamp, (250, 250))
vase = pygame.image.load("vase.png")
vase = pygame.transform.scale(vase, (250, 250))
stairs = pygame.image.load("stairs.png")
stairs = pygame.transform.flip(stairs, True, False)
bg3 = pygame.image.load("radio up close.PNG")
bg3 = pygame.transform.scale(bg3, (1400, 800))


box_1 = Starter_box_1(150, 400)
box_2 = Starter_box(700, 400)
board = Board()
g = Girl(0,0)
radio = Radio(40, 0)

change_panel = False
run = True
box_chosen = False
interaction = False
counter = 0
choice = ""
cutscene_done = False

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            change_panel = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and change_panel == True:
            counter += 1
        if counter % 2 == 0 and counter != 0:
            interaction = True
        else:
            interaction = False

        if counter == 8:
            interaction = False
            cutscene_done = True

        pos = pygame.mouse.get_pos()
        if box_1.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
            box_chosen = True
            choice = "past"
        elif box_2.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
            box_chosen = True
            choice = "present"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = "up"
        g.move_direction(direction)
    elif keys[pygame.K_a]:
        direction = "left"
        g.move_direction(direction)
    elif keys[pygame.K_s]:
        direction = "down"
        g.move_direction(direction)
    elif keys[pygame.K_d]:
        direction = "right"
        g.move_direction(direction)

    if not change_panel:      # starting screen
        screen.blit(bgstart, (-100,0))
        screen.blit(display_title, (385, 350))
        screen.blit(display_click_one, (510, 550))
    elif change_panel:       #choosing which character
        screen.fill((0, 0, 0))
        screen.blit(display_player_directions, (385, 300))
        screen.blit(display_past, (220, 500))
        screen.blit(display_present, (770, 500))
        screen.blit(box_1.image, box_1.rect)
        screen.blit(box_2.image, box_2.rect)

    if box_chosen:       #dialogue screen
        screen.blit(bg1, (0, 0))
        counter = 0
        if interaction:
            screen.blit(text_box, (150, 130))
            counter = counter + 1

    if choice == "past" and interaction == True:  #Grand daugther POV
        board.draw_board(screen)
        screen.blit(closet, (610, -100))
        screen.blit(clock, (1000, -10))
        screen.blit(couch, (20, -10))
        screen.blit(radio.image, radio.rect)
        screen.blit(shelf, (300, -80))
        screen.blit(ladder, (400, 40))
        screen.blit(stairs, (-250, 400))
        screen.blit(g.image, g.rect)
        screen.blit(table, (0, 200))
        screen.blit(table_2, (280, 500))
        screen.blit(table_3, (750, 350))
        screen.blit(vase, (870, 220))
        screen.blit(lamp, (400, 360))
        pygame.display.update()

    pos = pygame.mouse.get_pos()
    if radio.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(bg3, (-120,0))

    elif counter == 8 and choice == "present":    #Granpa POV
        board.draw_board(screen)


    pygame.display.update()
