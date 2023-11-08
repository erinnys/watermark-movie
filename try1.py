# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:17:28 2023

@author: Xavier
"""

from PIL import Image, ImageDraw, ImageFont
import imageio

name='picturedata/4p_5th_hetero.0000'
step=0.1
movie=[]


for i in range(9):
	img=Image.open('picturedata/4p_5th_hetero.0000{}.ppm'.format(i))
	lengx,lengy=img.size
	draw=ImageDraw.Draw(img)
	fon = ImageFont.truetype("arial.ttf", 100)
	tex='time : {}'.format(round(0.1*i,5))
	w=fon.getlength(tex)
	draw.text(xy=((lengx-w)/2,lengy/20),text=tex,fill='red',font=fon)
	img.save('{}.jpg'.format(i))
	movie.append(img)
fps=5
with imageio.get_writer('', fps=fps) as video:
    for image in images:
        frame = image.convert('RGB')
        video.append_data(frame)

