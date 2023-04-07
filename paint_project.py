import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)+255
cizim = False
def mouse_event(event,x,y,flags,param):
    global cizim
    if event == cv2.EVENT_LBUTTONDOWN:
        cizim = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim == True:
            cv2.circle(img,(x,y),5,(50,100,200),1)
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP:
        cizim = False



cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",mouse_event)
while(1):
    cv2.imshow("Paint",img)

    if cv2.waitKey(20) & 0xFF == 27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()