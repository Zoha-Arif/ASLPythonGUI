import cv2
import numpy as np
from keras.models import load_model
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
import keras
import keyboard 
import multiprocessing
import markov_nextwordpred
import subprocess

model = load_model('./new_model6.h5')

gestures = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'K',
    11:'L',
    12:'M',
    13:'N',
    14:'O',
    15:'P',
    16:'Q',
    17:'R',
    18:'S',
    19:'T',
    20:'U',
    21:'V',
    22:'W',
    23:'X',
    24:'Y',
}

def predict(gesture):
    img = cv2.resize(gesture, (50,50))
    img = img.reshape(1,50,50,1)
    img = img/255.0
    prd = model.predict(img)
    index = prd.argmax()
    return gestures[index]

vc = cv2.VideoCapture(0)
rval, frame = vc.read()
old_text = ''
pred_text = ''
count_frames = 0
total_str = ''
flag = False
start = False

while True:
    
    if frame is not None: 
        #=============For text predictor============= 
        #from markov_nextwordpred import c, last_suggestion 
        def c(cVar): 
            cv2.putText(blackboard, cVar, (50, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 203, 253))
        def last(last_suggestion):
            cv2.putText(blackboard, last_suggestion, (50, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 203, 253))
        #============================================ 

        frame = cv2.flip(frame, 1)
        frame = cv2.resize( frame, (500,500) )
                                                  # B  G  R
        cv2.rectangle(frame, (300,300), (100,100), (0,203,253), 2)
        
        crop_img = frame[100:300, 100:300]
        grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        
        #thresh = cv2.threshold(grey,210,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        thresh = cv2.threshold(grey,210,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)[1]
        #thresh = cv2.Canny(grey,210,255) 
        #thresh = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        blackboard = np.zeros(frame.shape, dtype=np.uint8)
        cv2.putText(blackboard, "Translation: ", (30, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 203, 253))
        cv2.putText(blackboard, "Press 'C' to begin translation program and 'Q' to quit/return home.", (30, 60), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 203, 253))
        cv2.putText(blackboard, "Press 'D' to delete the last character in the translation.", (30, 77), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 203, 253))
        if count_frames > 20 and pred_text != "":
            total_str += pred_text
            count_frames = 0
            
        if flag == True:
            old_text = pred_text
            pred_text = predict(thresh)
        
            if old_text == pred_text:
                count_frames += 1
            else:
                count_frames = 0

            cv2.putText(blackboard, total_str, (30, 120), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 203, 253))
        res = np.hstack((frame, blackboard))
        
        cv2.imshow("ASL Translation App", res)
        cv2.namedWindow('ASL Translation App')
        #cv2.resizeWindow('ASL Translation App', 800, 800)
        cv2.imshow("Image", thresh)

        if (start == True):
            print('STDOUT:{}'.format(stdout))
            
    rval, frame = vc.read()

    keypress = cv2.waitKey(1)
    if keypress == ord('c'):
        flag = True
        start = True
        #=============================Begin word predictor=============================
        from subprocess import PIPE
        #process = subprocess.Popen(['markov_nextwordpred.py'], stdout=PIPE, stderr=PIPE)
        process = subprocess.Popen([sys.executable, "markov_nextwordpred.py"])
        stdout, stderr = process.communicate()
            
    if keypress == ord('q'):
        break
    if keypress == ord('d'):
        total_str = total_str[:-1]
    if keypress == ord('s'):
        total_str = total_str + ' '
    
    def nothing(x):
        pass
vc.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


# In[17]:


vc.release()

