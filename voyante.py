import cv2
import numpy as np

img1_location="data/GetPicture1.jpeg"
img2_location="data/GetPicture2.jpeg"
img3_location="data/GetPicture3.jpeg"

img1g = cv2.imread(img1_location,0) # cv2.IMREAD_UNCHANGED
img2g = cv2.imread(img2_location,0)
img3g = cv2.imread(img3_location,0)

# Cropping the image to get only the cup. Could be automated, or simply ask the user to crop himself
height1, width1 = img1g.shape
cropimg1 = img1g[0:width1-150, 0:height1]

height2, width2 = img2g.shape
cropimg2 = img2g[0:width2-150, 0:height2]

height3, width3 = img3g.shape
cropimg3 = img3g[0:width3-150, 0:height3]


# Binarization of the image, to get only black and white (2 colors)
blur1 = cv2.GaussianBlur(cropimg1,(5,5),0)
ret1,th1 = cv2.threshold(blur1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur2 = cv2.GaussianBlur(cropimg2,(5,5),0)
ret2,th2 = cv2.threshold(blur2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur3 = cv2.GaussianBlur(cropimg3,(5,5),0)
ret3,th3 = cv2.threshold(blur3,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Now we want to search similarities between pictures.
res = cv2.matchTemplate(th3, th3, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print max_val

cv2.imshow('imageg',img1g)
cv2.imshow('imageg2',img2g)
cv2.imshow('imageg3',img3g)
cv2.imshow('imagecrop',cropimg1)
cv2.imshow('imagecrop2',cropimg2)
cv2.imshow('imagecrop3',cropimg3)

cv2.imshow('imageout3',th3)
cv2.imshow('imageout2',th2)
cv2.imshow('imageout1',th1)




cv2.waitKey(0)
cv2.destroyAllWindows()