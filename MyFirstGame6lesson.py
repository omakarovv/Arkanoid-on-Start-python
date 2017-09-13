#!/usr/bin/env python3
import pygame
import random
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("The beginning of Arkanoid")

bg = pygame.image.load("images/background.jpg")
fireball = pygame.image.load("animation/fireball.gif")
barrier = pygame.image.load("images/barrier.jpg")

square = pygame.Surface((10, 10))
#barrier = pygame.Surface((50,10))
square.fill((0, 255, 0))
#barrier.fill((245,232,232))

x = random.randint(0, 400)
y = random.randint(200, 250)

square_go_right = True
square_go_down = True
done = True
moveto = 195
delay = 5

while done:
    keyinput = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    window.blit(bg, (0, 0))
    window.blit(fireball, (x, y))

    if keyinput[pygame.K_LEFT]:
        moveto -= 2
        if moveto < 0:
            moveto = 0

    elif keyinput[pygame.K_RIGHT]:
        moveto += 2
        if moveto > 350:
           moveto = 350

    if square_go_down == True:
        y += 1
        moveto_2 = moveto + 50
        square_1 = x
        square_2 = x + 10
        if y < 385 and y > 380 and square_2 >= moveto and square_1 <= moveto_2:
            square_go_down = False
    else:
        y -= 1
        if y < 0:
            square_go_down = True

    if y > 390:
        x = random.randint(0, 400)
        y = random.randint(200, 250)

    if square_go_right == True:
        x += 1
        if x > 390:
            square_go_right = False
    else:
        x -= 1
        if x < 0:
            square_go_right = True

    if keyinput[pygame.K_LEFT] and square_go_right == True and y < 385 and y > 380 and square_2 >= moveto and square_1 <= moveto_2:
        square_go_right = False

    if keyinput[pygame.K_RIGHT] and square_go_right == False and y < 385 and y > 380 and square_2 >= moveto and square_1 <= moveto_2:
        square_go_right = True


    window.blit(barrier, (moveto, 390))
    pygame.display.flip()
    pygame.time.delay(delay)

    if keyinput[pygame.K_DOWN]:
        delay += 1
    elif keyinput[pygame.K_UP]:
        delay -= 1
    pygame.time.delay(delay)