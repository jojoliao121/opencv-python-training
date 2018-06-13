
# coding: utf-8

# In[30]:


import cv2


# In[33]:


bernie = cv2.imread('C:\\Users\\jojo.b.liao\\opencv-python-training\\assets\\bernie.jpg', cv2.IMREAD_COLOR)
howie = cv2.imread('C:\\Users\\jojo.b.liao\\opencv-python-training\\assets\\howie.png', cv2.IMREAD_COLOR)


# In[34]:


def show_image(image):
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
sum_img = cv2.add(bernie, howie)


# In[14]:


show_image(sum_img)


# In[15]:


bigbang = cv2.imread('C:\\Users\\jojo.b.liao\\opencv-python-training\\assets\\accenture.png', cv2.IMREAD_COLOR)


# In[16]:


print(bigbang.shape)


# In[17]:


bigbang = cv2.resize(bigbang, (int(bigbang.shape[1] * 0.25), int(bigbang.shape[0] * 0.25)))


# In[18]:


print(bigbang.shape)


# In[19]:


rows, cols, channels = bigbang.shape


# In[20]:


roi = bernie[0:rows,0:cols]
cv2.imshow('roi',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[21]:


bigbang_gray = cv2.cvtColor(bigbang, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(bigbang_gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('mask', mask)
cv2.waitKey(0),
cv2.destroyAllWindows()


# In[23]:


mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(0),
cv2.destroyAllWindows()


# In[24]:


bernig_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
cv2.imshow('bernig_bg', bernig_bg)
cv2.waitKey(0),
cv2.destroyAllWindows()


# In[26]:


bigbang_fg = cv2.bitwise_and(bigbang,bigbang, mask = mask)
cv2.imshow('bigbang_fg', bigbang_fg)
cv2.waitKey(0),
cv2.destroyAllWindows()


# In[29]:


dst = cv2.add(bernig_bg, bigbang_fg)
bernie[0:rows,0:cols] = dst
cv2.namedWindow('bernie_bigbang', cv2.WINDOW_NORMAL)
cv2.imshow('bernie_bigbang', bernie)
cv2.waitKey(0),
cv2.destroyAllWindows()


# In[ ]:


#blending video
import cv2 

accenture_logo = cv2.imread('../assets/accenture.jpg', cv2.IMREAD_COLOR)


cap=cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

