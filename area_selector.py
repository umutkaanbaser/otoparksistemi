import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import os 
cap = cv2.VideoCapture("otoparkVideo.mp4")
oldframes = deque(maxlen=30)
back_flip=False
back_indis=0
waitTime=0
counter_image=0
system_info = "a:oynat,b:geri oynat,c:durdur,d:1 ileri,e:1 geri,f:sec"
last_press=""
while cap.isOpened():
    if back_flip:
        back_indis = max((len(oldframes)-1)*-1,back_indis-1)
        frame = oldframes[back_indis].copy()
    elif back_indis<0:
        back_indis = min(0,back_indis+1)
        frame = oldframes[back_indis].copy()
    else:
        ret,frame = cap.read()
        
        _frame = frame.copy()
        oldframes.append(_frame)
        if not ret: break

    cv2.putText(frame,system_info,(10,10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255))
    cv2.putText(frame,f"son: {last_press}",(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255))
    
    cv2.imshow("frame",frame)
    key = cv2.waitKey(waitTime)
    if key==ord("q"):
        break
    elif key == ord("a"):
        waitTime=30
        back_flip=False
        last_press="a"
    elif key == ord("b"):
        waitTime=30
        back_flip=True
        last_press="b"
    elif key == ord("c"):
        waitTime=0
        last_press="c"
    elif key == ord("d"):
        back_flip=False
        waitTime=0
        last_press="d"
    elif key == ord("e"):
        back_flip=True
        waitTime=0
        last_press="e"
    elif key == ord("f"):
        (x,y,w,h) = cv2.selectROI("frame",frame,False)
        select_roi = _frame[y:y+h,x:x+w]
        cv2.imwrite(f"images/{counter_image}_img.jpg",select_roi)
        counter_image+=1;
        last_press="f"
