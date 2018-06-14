
# coding: utf-8

# In[ ]:


import cv2
import numpy as np


# In[ ]:


#from_future_ import absolute import
#from_future_ import absolute division
#from_future_ import absolute print_function
 


def apply_invert(frame):
    return cv2.bitwise_not(frame)

def apply_sepia(frame, intensity=0.5):
    blue, green, red= 20, 66, 112
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_height, frame_width, frame_channel=frame.shape
    sepia_bgra=(blue, green, red,1)
    overlay=np.full((frame_height, frame_width,4), sepia_bgra, dtype='uint8')
    frame=cv2.addWeighted(overlay, intensity, frame, 1.0,0)
    frame=cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame

def apply_alpha_convert(frame):
    try:
        frame.shape[3]
    except IndexError:
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame
    
def apply_portrait_mode(frame):
    frame=apply_alpha_convert(frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask=cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    
    mask=cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    blurred=cv2.GaussianBlur(frame, (21,21), 0)
    blended=apply_blend(frame, blurred, mask)
    frame=cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return frame

    #cv2.imshow('mask', mask)
    #cv2.imshow('blurred', blurred)
    
def apply_blend(frame_1, frame_2, mask):
    alpha=mask/255.0
    blended=cv2.convertScaleAbs(frame_1 *(1 - alpha) + (frame_2 * alpha))
    return blended
   
    
cap= cv2.VideoCapture(0)

while True:
    _, frame= cap.read()
    invert=apply_invert(frame)
    sepia=apply_sepia(frame)
    portrait=apply_portrait_mode(frame)
    #blend= apply_blend(frame)
    #cv2.imshow('frame', frame)
    #cv2.imshow('invert', invert)
    #cv2.imshow('sepia', sepia)
    cv2.imshow('portrait', portrait)
    k=cv2.waitKey(1)
    
    if k==ord('q') or k==27:
        cap.release()
        cv2.destroyAllWindows()
        break

