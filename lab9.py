from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar 


def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

displayText("etch n sketch", lcd,1,1)





def func(pixel=1,x=70,y=30):
    switch = True
    while switch == True:
        input = getchar()
        if input == '\x1b[A':
            y -= 1
            if y == 0:
                y = 63
            lcd.set_pixel(x,y,pixel)
            lcd.show()
        if input == '\x1b[B' :
            y += 1
            if y > 63:
                y = 1
            lcd.set_pixel(x,y,pixel)
            lcd.show()
        if input == '\x1b[C':
            x += 1
            if x > 127:
                x = 1
            lcd.set_pixel(x,y,pixel)
            lcd.show()
        if input == '\x1b[D' :
            x -= 1
            if x == 0:
                x = 126
            lcd.set_pixel(x,y,pixel)
            lcd.show()
        if input == 'q':
            break
        if input == 's':
            clearScreen(lcd)

func()

