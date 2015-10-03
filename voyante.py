import cv2
import numpy as np

img1_location="data/GetPicture1.jpeg"
img2_location="data/GetPicture2.jpeg"
img3_location="data/GetPicture3.jpeg"

img1 = cv2.imread(img1_location,cv2.IMREAD_UNCHANGED)
img1g = cv2.imread(img1_location,0)
# img2 = cv2.imread(img2_location,cv2.IMREAD_UNCHANGED)
# img3 = cv2.imread(img3_location,cv2.IMREAD_UNCHANGED)



height, width, channels = img1.shape
cropimg1 = img1g[0:width-150, 0:height]


blur = cv2.GaussianBlur(cropimg1,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('imageg',img1g)
cv2.imshow('imagecrop',cropimg1)
cv2.imshow('imageout2',blur)
cv2.imshow('imageout3',th3)




cv2.waitKey(0)
cv2.destroyAllWindows()