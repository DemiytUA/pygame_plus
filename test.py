import time
import pygame
from pygame_plus import scripts #import pygame+

pygame.init()

# Визначте кольори
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
GREY2 = (150, 150, 150)
GREEN = (150, 200, 10)
BLACK = (0, 0, 0)

# Встановіть розмір екрану
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame+ Example")
clock = pygame.time.Clock()

# buttons
default_image = pygame.image.load("test/s1.png")
hover_image = pygame.image.load("test/s2.png")
click_image = pygame.image.load("test/s3.png")

font = pygame.font.Font(None, 40)
text = font.render('Prees "E"', True, GREY2)



x = 20
y = 20
speed = 5

obj_x = 700
obj_y = 300



width = 50
height = 50
obj_width = 25
obj_height = 25





wx1, wx2 = (100, 500)
wy1, wy2 = (300, 500)
wall_pos = ((wx1, wy1), (wx1, wy2), (wx2, wy2), (wx2, wy1))
wspos = scripts.pluspos(wall_pos, 20)

def start_game():
    global game
    game = True
    time.sleep(0.2)

# button
button = scripts.Button(280, 180, default_image, hover_image, click_image, action=start_game)#create button

running = True
game = False
dialog = False

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Button update
    button.update(events)


    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    if game:

        interaction = scripts.next_to(x, y, obj_x, obj_y, 50) # interaction with objects(returns True/False

        sobj = scripts.n_obj(x, y, (width, height), speed, wall_pos) #block move(returns side)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if sobj == 'u':
                pass
            else:
                y = max(0, y - speed)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if sobj == 'd':
                pass
            else:
                y = min(HEIGHT - height, y + speed)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            side_lrn = 'l'
            if sobj == 'l':
                pass
            else:
                x = max(0, x - speed)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            side_lrn = 'r'
            if sobj == 'r':
                pass
            else:
                x = min(WIDTH - width, x + speed)

        if interaction:
            screen.blit(text, (330, 20))
            if keys[pygame.K_e]:
                dialog = True


        darkened_p = scripts.ffeg(x, y, wall_pos)
        darkened_pos = scripts.darkened_pos(x, y, wall_pos, WIDTH, HEIGHT) #dark polygon(returns positions)



        pygame.draw.rect(screen, GREY, (obj_x, obj_y, obj_width, obj_height)) # draw object
        player = pygame.draw.rect(screen, GREEN, (x, y, width, height)) # draw player
        pygame.draw.polygon(screen, BLACK, darkened_pos) # draw dark
        wall = pygame.draw.polygon(screen, GREY, wall_pos)#draw wall

        if dialog:
            text = font.render('Press "SPACE"', True, GREY2)
            #                       text             font  text color   background color   x   y width_height   screen  pygame
            scripts.dialog_text(['It`s text', '=)'], font, (200, 200, 200), (50, 50, 50), 400, 50, 350, 150, screen,    pygame)

            if keys[pygame.K_SPACE]:
                time.sleep(1)
                scripts.darkened_screen(WIDTH, HEIGHT, pygame, screen) #dimming the screen
                text = font.render('Prees "E"', True, GREY2)
                dialog = False


    else:
        # Button draw
        button.draw(screen)

    clock.tick(100)
    FPS = scripts.FPS(clock)
    pygame.display.set_caption(f"FPS: {int(FPS)}")
    pygame.display.flip()

pygame.quit()



'''    other:
obj_pos = ((50, 50), (50, 200), (100, 200), (100, 50))
test_x = 200
test_y = 50


pluspos:
 new_pos = scripts.pluspos(obj_pos, 50)
 # Returns the position of the resized object. In this case returns [[0, 0], [0, 250], [150, 250], [150, 0]]

iside_in:
 is_inside_in = scripts.inside_in((test_x, test_y), obj_pos)
 #returns True/False

'''