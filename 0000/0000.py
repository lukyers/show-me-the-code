#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw

img = raw_input("Enter your image path: ")
number = raw_input("Enter the number: ")
im = Image.open(img)
x, y = im.size

Font1 = ImageFont.truetype('consola.ttf', int(x*0.2))
d = ImageDraw.Draw(im)
d.text([x*0.7, y*0.1], unicode(number, 'UTF-8'), fill='#FF0000', font=Font1)

im.save("done.jpg")
