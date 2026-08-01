from ethanPlatform import *

# xpos, ypos, xwidth, yheight, color


def level1():
    return [
        CustomPlatform(0,   600, 1280, 20, "white"),   # ground
        CustomPlatform(500, 250, 150,  20, "white"),
        CustomPlatform(400, 450, 150,  20, "white"),
        CustomPlatform(700, 150, 150,  20, "white"),
        CustomPlatform(250, 350, 150,  20, "white"),
        EscapeDoor(760, 90, 30, 60),
    ]


def level2():
    return [
        CustomPlatform(0, 600, 1280, 20, "white"),   # ground
        EscapeDoor(1200, 540, 30, 60),
    ]


levels = [level1, level2]
