
# coding: utf-8

# In[ ]:


def apply_invert(frame):
    return cv2.bitwise_not(frame)

cap= cv2.VideoCapture(0)

while True:
    _, frame= cap.read()
    invert=apply_invert(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('invert', invert)
    
    k=cv2.waitKey(1)
    
    if k==ord('q') or k==27:
        cap.release()
        cv2.destroyAllWindows()
        break
        
        

