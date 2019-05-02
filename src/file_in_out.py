import struct
import os.path
from src.main import Ball
from src.main import Paddle
from src.main import Brick

def read_file(file):
    with open(file, "rb") as file:
        data = bytearray(file.read())
        file.close()

        print(os.getcwd())

    format = ">iidiiiii"

    c_size = struct.calcsize(format)
    slice = data[0: c_size]
    bx, by, b_T, px, score, lives, level,n_bricks = struct.unpack(format, slice)

    ball = Ball((b_T, 10))
    ball.set_location((bx, by))
    paddle = Paddle()
    paddle.rect.x = px

    ball.set_paddle(paddle)

    b_fmt = ">iii"
    b_size = struct.calcsize(b_fmt)
    bricks = []

    for i in range(n_bricks):
        start = c_size + (i * b_size)
        end = start + b_size
        slice = data[start: end]
        bx, by, bh = struct.unpack(b_fmt, slice)
        b = Brick(bx,by,bh)

        bricks.append(b)

    return ball, paddle, bricks, score, lives, level


def write_file(file, ball, paddle, bricks, score, lives, level):
        ba = bytearray()
        fmt = ">iidiiiii"
        header = struct.pack(fmt, ball.rect.x, ball.rect.y, ball.vector[0], paddle.rect.x, score, lives, level, len(bricks))
        ba.extend(header)
        br_fmt = ">iii"
        for brick in bricks:
            br_data = struct.pack(br_fmt, brick.rect.x, brick.rect.y, brick.health)
            ba.extend(br_data)

        with open(file, "wb") as file:
            file.write(ba)
            file.close()
