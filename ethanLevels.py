from ethanPlatform import *


def level1():
    return[
        CustomPlatform(0, 600, 1280, 20, "yellow"), #floor
        # CustomPlatform ( 450, 450, 200 ,20, "yellow"), #1
        # CustomPlatform ( 450, 325,200,20, "yellow" ),#2
        CustomPlatform ( 200, 50,20, 500, "yellow" ),#3
        CustomPlatform ( 1000, 320,20, 300, "yellow" ),#4
        CustomPlatform ( 1000, 0,20, 200, "yellow" ),#4
    ]



def level2():
    return[
        CustomPlatform(0, 600, 1280, 20, "red"), 
        CustomPlatform ( 800, 400, 200 ,20, "red"),
        CustomPlatform ( 785, 303,200,20, "red" ),
        CustomPlatform(785, 203, 10, 100, "red" ),
        CustomPlatform(785, 33, 10, 100, "red" ),
        CustomPlatform(50, 530, 150, 20, "red" ),
        CustomPlatform(195, 400, 10, 150, "red" ),
        CustomPlatform(50, 400, 150, 20, "red" ),
        CustomPlatform(300, 400, 35, 20, "red" ),
        CustomPlatform(530, 400, 35, 20, "red" ),
        EscapeDoor(300, 150, 100, 20, 0,500 ),
        CustomPlatform(300, 170, 100, 20, "red" ),

    ]



def level3():
    return[
        CustomPlatform(0, 600, 1280, 20, "blue"), #floor 
        CustomPlatform ( 250, 450, 200 ,20, "blue"), #1
        CustomPlatform ( 250, 325,200,20, "blue" ), #2
        CustomPlatform ( 250, 325,200,20, "blue" ), #3
        

    ]


levels = [level1, level2, level3]
