# https: // stackoverflow.com/questions/16373425/add-text-on-image-using-pil

from PIL import Image, ImageDraw, ImageFont

name = input("Insert Name: ")
if len(name) <= 15:
    namelength = (len(name) / 1.5)
else:
    namelength = len(name) * 2.6

img = Image.open('award.jpg')
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("STENCIL.TTF", 27)
if len(name) <= 15:
    draw.text((260 + namelength, 300), name, (50, 50, 50), font=font)
else:
    draw.text((260 - namelength, 300), name, (50, 50, 50), font=font)

img.save('output.jpg')
