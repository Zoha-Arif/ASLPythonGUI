import tkinter as tk
from PIL import ImageTk, Image
import cv2
import requests
import random 
import numpy as np

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
#from utils import label_map_util
#from utils import visualization_utils as vis_


#Arranging the HomePage
FILENAME = 'home.png'
root = tk.Tk()
canvas = tk.Canvas(root, width=750, height=490)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = FILENAME)
#canvas.create_image(125, 125, image=tk_img)
#canvas.create_image(200, 400, image=tk_img, anchor='nw')
canvas.create_image(0, 0, image=tk_img, anchor='nw')


def translate():
    frameNumber = tk.Frame(root, bg="#FFD966")
    frameNumber.place(relwidth=1, relheight=1)
    cap = cv2.VideoCapture(0)  # Change only if you have more than one webcams
    try:
        if not os.path.exists('data'):
            os.makedirs('data')

    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = 0

#IMPLEMENT A METHOD THAT ONLY TAKES EVERY 25 IMAGES
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        # To stop duplicate images
        currentFrame += 1
        #Process images before feeding into tensorflow net
        img = cv2.imread(name)
        img = cv2.resize(img, (28, 28))
        


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
 
   
    
#Translate Button
translate_button = tk.Button(root, highlightthickness=0, text = "    T R A N S L A T E", command = translate, anchor = 'w',
                    width = 16, activebackground = "#16A9FF", bd=0, bg="#16A9FF",fg="#FFFFFF", font='Arial 9 bold')
translate_button_window = canvas.create_window(33, 43, anchor='nw', window=translate_button)    

#Sad Face/Help Button
image = Image.open("helpb.png")
image = image.resize((44, 44), Image.ANTIALIAS) ## The (250, 250) is (height, width)
#pw.pic = ImageTk.PhotoImage(image)
helpb = tk.Button(root, width=5, height=0, command = root.quit)
#image1 = ImageTk.PhotoImage(file="helpb.png")
image1 = ImageTk.PhotoImage(image)
# Color Code = #FFD966
helpb.config(image=image1, highlightthickness=0,  activebackground = "#FFD966", bd=0, bg="#FFD966", width=50, height=50)#These set the height and width of box of the picture.
helpb.image = image1
helpb_window = canvas.create_window(200, 30, anchor='nw', window=helpb) #These numbers move the picture. 

#Heart/Information Button
image = Image.open("heartb.png")
image = image.resize((38, 38), Image.ANTIALIAS) ## The (250, 250) is (height, width)
heartb = tk.Button(root, width=5, height=0, command = root.quit)
#image1 = ImageTk.PhotoImage(file="helpb.png")
image2 = ImageTk.PhotoImage(image)
# Color Code = #FFD966
heartb.config(image=image2, highlightthickness=0,  activebackground = "#FFD966", bd=0, bg="#FFD966", width=50, height=50) #These set the height and width of box of the picture.
heartb.image = image2
heartb_window = canvas.create_window(680, 30, anchor='nw', window=heartb) #These numbers move the picture. 


#while True: 
#        ret, frame = cap.read()
#        cv2.imshow('frame', frame)
#
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break 
#    cap.release()
#    cv2.destroyAllWindows()

root.mainloop()