import pygame
from starter_box import Starter_box
from starter_box_1 import Starter_box_1
from board import Board
from girl import Girl
from radio import Radio
from man import Man

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

dialogues = ["Adeline is visiting her grandpa’s antique shop right before", "he is shutting it down. He is getting too old to continue…", "While walking around, she picks things up and examines them,", "wondering about their purposes and history.", "She stops before a mirror.", "Curious, she reaches out to touch the wood.", "In a flash, she is confined inside.", "Grandpa!? Where are you, and where am I!?", "Adeline! Did you touch the mirror while I wasn’t looking?!", "*sigh* It just had to be this mirror...", "Look around Addie and tell me what you see. I’ll get you out of", "there.", "Adeline is surprised to see a carbon copy of the store.", "The well-managed store looked more clean and less cluttered.", "Is this the store? It looks a lot older.", "The past. You’re in the past..."]

display_title = my_font.render(title, True, (249, 234, 199))
my_font = pygame.font.SysFont('Courier', 25)
display_click_one = my_font.render(click_one, True, (255, 255, 255))
my_font = pygame.font.SysFont('Bell', 50)
display_player_directions = my_font.render(player_directions, True, (255, 255, 255))
my_font = pygame.font.SysFont('Papyrus', 30)
display_past = my_font.render(past, True, (255, 255, 255))
display_present = my_font.render(present, True, (255, 255, 255))

radio_code = my_font.render("", True, (0, 0, 0))
radio_code_2 = my_font.render("", True, (0, 0, 0))
radio_code_3 = my_font.render("", True, (0, 0, 0))
radio_code_4 = my_font.render("", True, (0, 0, 0))

text = ""
display_dialogue = my_font.render(text, True, (0, 0, 0))

text_box = pygame.image.load("image files/text box.png")
closet = pygame.image.load("image files/closet.png")
couch = pygame.image.load("image files/couch.png")
clock = pygame.image.load("image files/clock.png")
clock = pygame.transform.scale(clock, (167, 374))
shelf = pygame.image.load("image files/shelf.png")
ladder = pygame.image.load("image files/ladder.png")
ladder = pygame.transform.scale(ladder, (200, 300))
table = pygame.image.load("image files/round table.png")
table = pygame.transform.scale(table, (481, 300))
table_2 = pygame.image.load("image files/round table.png")
table_2 = pygame.transform.scale(table_2, (481, 300))
table_3 = pygame.image.load("image files/round table.png")
table_3 = pygame.transform.scale(table_3, (481, 300))
lamp = pygame.image.load("image files/lamp.png")
lamp = pygame.transform.scale(lamp, (250, 250))
vase = pygame.image.load("image files/vase.png")
vase = pygame.transform.scale(vase, (250, 250))
stairs = pygame.image.load("image files/stairs.png")
stairs = pygame.transform.flip(stairs, True, False)
wallboard = pygame.image.load("image files/board.png")

bgstart = pygame.image.load("image files/mirror background.jpg")
bg1 = pygame.image.load("image files/antique backdrop 1.jpg")
bg3 = pygame.image.load("image files/radio up close.PNG")
bg3 = pygame.transform.scale(bg3, (1400, 800))

box_1 = Starter_box_1(150, 400)
box_2 = Starter_box(700, 400)
board = Board()
g = Girl(0, 0)
m = Man(0, 0)
radio = Radio(40, 0)

change_panel = False
run = True
box_chosen = False
interaction = False
counter = 0
choice = ""
cutscene_done = False
dialogue_screen = False
text = ""
i = 0
radio_screen = False
radio_numbers = []

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            change_panel = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            interaction = True
        else:
            interaction = False

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

    if keys[pygame.K_w]:
        direction = "up"
        m.move_direction(direction)
    elif keys[pygame.K_a]:
        direction = "left"
        m.move_direction(direction)
    elif keys[pygame.K_s]:
        direction = "down"
        m.move_direction(direction)
    elif keys[pygame.K_d]:
        direction = "right"
        m.move_direction(direction)

        # starting screen
    pos = pygame.mouse.get_pos()
    screen.blit(bgstart, (-100, 0))
    screen.blit(display_title, (385, 350))
    screen.blit(display_click_one, (510, 550))
    if event.type == pygame.MOUSEBUTTONDOWN and not (box_1.rect.collidepoint(pos)) and not (box_2.rect.collidepoint(pos)):
        change_panel = True

    if change_panel:  # choosing which character
        if box_1.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            box_chosen = True
            choice = "past"
            dialogue_screen = True
        elif box_2.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            box_chosen = True
            choice = "present"
            dialogue_screen = True

        screen.fill((0, 0, 0))
        screen.blit(display_player_directions, (385, 300))
        screen.blit(display_past, (220, 500))
        screen.blit(display_present, (770, 500))
        screen.blit(box_1.image, box_1.rect)
        screen.blit(box_2.image, box_2.rect)

    # i = 0

    if box_chosen and dialogue_screen == True:  # dialogue screen
        if i <= len(dialogues):
            dialogue_screen = True
        elif i > len(dialogues):
            dialogue_screen = False
        screen.blit(bg1, (0, 0))
        screen.blit(text_box, (150, 130))
        my_font = pygame.font.SysFont('Courier', 25)
        if i == 2:
            display_dialogue = my_font.render(dialogues[i - 2], True, (0, 0, 0))
            screen.blit(display_dialogue, (180, 600))
            display_dialogue_two = my_font.render(dialogues[i - 1], True, (0, 0, 0))
            screen.blit(display_dialogue_two, (180, 650))
            i = i + 1
            interaction = False
        elif i == 3 or i == 11:
            display_dialogue = my_font.render(dialogues[i - 1], True, (0, 0, 0))
            screen.blit(display_dialogue, (180, 600))
            display_dialogue_two = my_font.render(dialogues[i], True, (0, 0, 0))
            screen.blit(display_dialogue_two, (180, 650))
            if interaction == True:
                i = i + 2
                interaction = False
        if i == 8 or i == 14:
            my_font = pygame.font.SysFont('Courier', 30)
            display_ad = my_font.render("Adeline", True, (255, 255, 255))
            screen.blit(display_ad, (350, 540))
        if i > 7 and i < 15 and i != 8 and i != 14:
            my_font = pygame.font.SysFont('Courier', 30)
            display_ar = my_font.render("Arthur", True, (255, 255, 255))
            screen.blit(display_ar, (350, 540))
        elif i <= (len(dialogues)):
            display_dialogue = my_font.render(dialogues[i - 1], True, (0, 0, 0))
            screen.blit(display_dialogue, (180, 600))
        if i <= (len(dialogues)) and interaction == True:
            i = i + 1
            interaction = False

    if choice == "past" and dialogue_screen == False:  #Grand daughter POV
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

        for event in pygame.event.get():                    #Taking in keyboard and mouse controls
            pos = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
        if radio.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:               #Radio close up off screen
            radio_screen = True
        if radio_screen == True and keys[pygame.K_ESCAPE]:      #Radio close up on screen
            radio_screen = False
        elif radio_screen == True:
            screen.blit(bg3, (-120, 0))
            my_font = pygame.font.SysFont('Courier', 80)
            for i in range (4):  #NEEDS FIXING
                if keys[pygame.K_0]:                    #Keyboard commands for the code!
                    radio_numbers.append("0")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_1]:
                    radio_numbers.append("1")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_2]:
                    radio_numbers.append("2")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_3]:
                    radio_numbers.append("3")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_4]:
                    radio_numbers.append("4")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_5]:
                    radio_numbers.append("5")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_6]:
                    radio_numbers.append("6")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_7]:
                    radio_numbers.append("7")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_1]:
                    radio_numbers.append("8")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
                elif keys[pygame.K_1]:
                    radio_numbers.append("9")
                    if i == 0:
                        radio_code = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 1:
                        radio_code_2 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 2:
                        radio_code_3 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    elif i == 3:
                        radio_code_4 = my_font.render(radio_numbers[i], True, (0, 0, 0))
                    i = i + 1
            screen.blit(radio_code, (495, 355))
            screen.blit(radio_code_2, (550, 355))
            screen.blit(radio_code_3, (603, 355))
            screen.blit(radio_code_4, (655, 355))

        pygame.display.update()

    elif choice == "present" and dialogue_screen == False:    #Grandpa POV
        board.draw_board(screen)
        screen.blit(wallboard, (250, 0))
        screen.blit(stairs, (-250, 400))
        screen.blit(clock, (25, -10))
        screen.blit(couch, (750, 250))
        screen.blit(m.image, m.rect)
        screen.blit(table, (725,400))


    pygame.display.update()
