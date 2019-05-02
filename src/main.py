

import random
import math
import os
import pygame
from given.text_to_screen import Fonts
from given.text_to_screen import Colors
from given.text_to_screen import draw_text_to_screen
from src.file_in_out import *

VERSION = "0.4"

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('../img', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image
    except pygame.error:
        print('Cannot load image:', fullname)


def calcnewpos(rect, vector):
    (angle, z) = vector
    (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
    return rect.move(dx, dy)


class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    start = 0
    play = 1
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('ball.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0
        self.rect.center = self.area.center
        self.state = Ball.start

    def set_location(self, loc):
        self.rect.topleft = loc

    def set_paddle(self, paddle):
        self.player1 = paddle

    def set_bricks(self, bricks):
        self.bricks = bricks

    def update(self):
        newpos = calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        if self.state == Ball.start:
            self.rect.midbottom = self.player1.rect.midtop
            angle = math.pi / 2

        else:

            if not self.area.contains(newpos):
                tl = not self.area.collidepoint(newpos.topleft)
                tr = not self.area.collidepoint(newpos.topright)
                bl = not self.area.collidepoint(newpos.bottomleft)
                br = not self.area.collidepoint(newpos.bottomright)
                if (tr and tl) or (br and bl):
                    angle = -angle
                if (tl and bl) or (tr and br):
                    angle = math.pi - angle

            else:
                # Deflate the rectangles so you can't catch a ball behind the bat
                self.player1.rect.inflate(-3, -3)

                # Do ball and bat collide?
                # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
                # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
                # bat, the ball reverses, and is still inside the bat, so bounces around inside.
                # This way, the ball can always escape and bounce away cleanly
                x_1 = self.rect.centerx
                x_2 = self.player1.rect.centerx
                delta_x = (x_1- x_2) / 80
                theta = delta_x - (math.pi/2)
                if self.rect.colliderect(self.player1.rect) == 1 and not self.hit:
                    angle = theta
                    self.hit = not self.hit
                elif self.hit:
                    self.hit = not self.hit
                for brick in self.bricks:
                    if self.rect.colliderect(brick.rect) == 1 and not self.hit:
                        if brick.rect.bottom > self.rect.centery > brick.rect.top:
                            angle = angle - math.pi
                            self.hit = not self.hit
                        else:
                            angle = -angle
                            self.hit = not self.hit
                        brick.health -= 1
                        break
        self.vector = (angle, z)


class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y, h=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('basic_block.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.health = h
        self.rect.topleft = (x, y)

    def update(self):
        pygame.event.pump()

    def is_dead(self):
        return self.health <= 0


class Boss(Brick):

    def __init__(self, x, y, h=5):
        super(Boss, self).__init__(x, y, h)
        self.position = 0

    def update(self):
        super(Boss, self).update()
        self.position += .01
        screen_loc = math.sin(self.position) * 520
        self.rect.topleft = (320 + screen_loc, 0)








class Paddle(pygame.sprite.Sprite):
    """Movable tennis 'bat' with which one hits the ball
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    X = 0
    Y = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('paddle.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0, 0]
        self.rect.midbottom = self.area.midbottom

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveleft(self):
        self.movepos[Paddle.X] = self.movepos[Paddle.X] - self.speed
        self.state = "moveleft"

    def moveright(self):
        self.movepos[Paddle.X] = self.movepos[Paddle.X] + self.speed
        self.state = "moveright"

    def still(self):
        self.movepos = [0, 0]
        self.state = "still"

def main():
    global bricks
    global player1
    global bricks
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Tom\'s Pong: v' + str(VERSION))
    try:

        ball, player1, bricks, score, lives, level = read_file("save")
        ball.set_bricks(bricks)
        ball.set_paddle(player1)
        bricks.append(Boss(320, 0))

    except FileNotFoundError as e:
        print(e)
        score = 0
        lives = 3
        level = 1

        player1 = Paddle()

        bricks = []
        bricks.append(Boss(320, 0))

        for i in range(level):
            for j in range(5):
                bricks.append(Brick(j * 128, (screen.get_height()/10) + 120))

        # Initialize ball
        speed = 13
        rand = 0.1 * random.randint(5, 8)
        ball = Ball((1.5, speed))

        ball.set_bricks(bricks)
        ball.set_paddle(player1)


    screen = pygame.display.set_mode((640, 480))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    ball.set_paddle(player1)
    # Initialize sprites
    playersprites = pygame.sprite.RenderPlain(player1)
    ballsprite = pygame.sprite.RenderPlain(ball)
    bricksprite = pygame.sprite.RenderPlain(bricks)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize clock
    clock = pygame.time.Clock()

    GAME_OVER = "GAME OVER"
    PAUSE = "PAUSE"
    PLAY = "PLAY"

    state = GAME_OVER


    game_exit = False
    # Event loop
    while not game_exit:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        screen.fill((0, 0, 0))

        if state == GAME_OVER: 

            bricksprite = pygame.sprite.RenderPlain(bricks)

            x = (screen.get_width()/2) - 300
            y = (screen.get_height()/2) - 100

            draw_text_to_screen(screen, "Game Over", x, y, Colors.WHITE, Fonts.TITLE_FONT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write_file ("save", ball, player1, bricks, lives, level, score)
                    game_exit = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = PLAY
                        lives = 10
                        score = 0
                        level = 1
                        screen.fill(Colors.BLACK)

                    if event.key == pygame.K_ESCAPE:
                        write_file("save", ball, player1, bricks, lives, level, score)
                        game_exit = True

            pygame.display.flip()

        elif state == PLAY:

            draw_text_to_screen(screen, "lives:" + str(lives), 20, screen.get_height() - 30 , Colors.WHITE, Fonts.TEXT_FONT)
            draw_text_to_screen(screen, "level:" + str(level), 20, screen.get_height() - 60 , Colors.WHITE, Fonts.TEXT_FONT)
            draw_text_to_screen(screen, "score:" + str(score), 20, screen.get_height() - 90 , Colors.WHITE, Fonts.TEXT_FONT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write_file("save", ball, player1, bricks, lives, level, score)
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1.moveleft()
                    if event.key == pygame.K_RIGHT:
                        player1.moveright()
                    if event.key == pygame.K_ESCAPE:
                        write_file("save", ball, player1, bricks, lives, level, score)
                        game_exit = True
                    if event.key == pygame.K_RETURN:
                        state = PAUSE
                    if event.key == pygame.K_SPACE:
                        ball.state = Ball.play
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player1.still()

            screen.blit(background, ball.rect, ball.rect)
            screen.blit(background, player1.rect, player1.rect)
            for brick in bricks:
                screen.blit(background, brick.rect, brick.rect)
            ballsprite.update()
            playersprites.update()
            bricksprite.update()

            for brick in bricks:
                if brick.is_dead():
                    bricks.remove(brick)
                    bricksprite.remove(brick)

            if ball.rect.bottom >= screen.get_height():
                lives -= 1

            if lives == 0:
                state = GAME_OVER
                ball.state = Ball.start

            if len(bricks) == 0:
                score += 10
                level += 1

                bricks.append(Boss(320, 0))
                for i in range(level):
                    for j in range(5):
                        bricks.append(Brick(j * 128, (screen.get_height() / 10)))
                ball.set_bricks(bricks)
                bricksprite = pygame.sprite.RenderPlain(bricks)


            ballsprite.draw(screen)
            playersprites.draw(screen)
            bricksprite.draw(screen)
            pygame.display.flip()

        elif state == PAUSE:
            x = (screen.get_width() / 2) - 300
            y = (screen.get_height() / 2) - 100

            draw_text_to_screen(screen, "PAUSED", x, y, Colors.WHITE, Fonts.TITLE_FONT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write_file("save", ball, player1, bricks, lives, level, score)
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        state = PLAY
                        screen.fill(Colors.BLACK)
                    if event.key == pygame.K_ESCAPE:
                        write_file("save", ball, player1, bricks, lives, level, score)
                        game_exit = True
            pygame.display.flip()


if __name__ == '__main__':
    main()
