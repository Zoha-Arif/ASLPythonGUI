import cv2
import numpy as np
from keras.models import load_model

execfile('markov_nextwordpred.py')
 
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

while True:
    
    if frame is not None: 
        
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
        
        cv2.imshow("Translation App", res)
        cv2.imshow("Image", thresh)
        
    rval, frame = vc.read()
    keypress = cv2.waitKey(1)
    if keypress == ord('c'):
        flag = True
    if keypress == ord('q'):
        break
    if keypress == ord('d'):
        total_str = total_str[:-1]

vc.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


# In[17]:


vc.release()

