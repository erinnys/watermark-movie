# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:17:28 2023

@author: Xavier
"""

from PIL import Image, ImageDraw, ImageFont
import cv2

name='picturedata/4p_5th_hetero.0000'
movie=[]


for i in range(10):
	img=Image.open('picturedata/4p_5th_hetero.{}.ppm'.format(i))
	lengx,lengy=img.size
	draw=ImageDraw.Draw(img)
	fon = ImageFont.truetype("arial.ttf", 100)
	tex='Time : {} ps'.format(round(0.1*i,5))
	w=fon.getlength(tex)
	draw.text(xy=((lengx-w)/2,lengy*18/20),text=tex,fill='red',font=fon)
	img.save('{}.jpg'.format(i))
	movie.append('{}.jpg'.format(i))
fps=5
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('movie.mp4', fourcc, fps, (lengx, lengy))
for i in movie:
    frame = cv2.imread(i)
    video.write(frame)
video.release()