from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar 


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


list = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]
y = input("Please enter a Y variable")
x = input("Please enter an X variable")
x = int(x)
y = int(y)
def  shape(x,y,list):
    oldx = x
    for codes in list:
        y += 1
        x = oldx
        for code in codes:
            x += 1
            lcd.set_pixel(x, y, code)
            lcd.show()
shape(x,y,list)