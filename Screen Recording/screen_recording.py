
import pyautogui as p
import cv2 
import numpy as np

#Create resolution
rs = p.size()

#filename in which we will storeoutput  recording
fn = input("Please Enter any file name and Path")

#Fix the frame rate
fps = 60.0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fn,fourcc,fps,rs)

#create recording module
cv2.namedWindow("LIve_Recording",cv2.WINDOW_NORMAL)

#Resize the window
cv2.resizeWindow("LIve_Recording",(600,400))

while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("screenshot", f)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
output.release()  