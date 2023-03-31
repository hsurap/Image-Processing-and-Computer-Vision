import cv2    
#openCV use as cv2 in python
#Image conversion project colored image into grayscale.

path = input("Enter the Path and name of an image===")
print("You Enter this===",path)

#Now read image 
img1 = cv2.imread(path,0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,1)#it accept 3 parameters 0,-1,1#used for any rotation
cv2.imshow("converted image==",img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
    
elif k == ord("s"):
    cv2.imwrite("H:\\ouput.png",img1)  #it accept name of image and data
    cv2.destroyAllWindows()  #openCV use as cv2 in python