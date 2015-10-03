import cv2
import numpy as np

img_locations=["data/GetPicture1.jpeg", "data/GetPicture2.jpeg", "data/GetPicture3.jpeg"]

# Cropping the image to get only the cup. Could be automated, or simply ask the user to crop himself
def crop(img, width_start, width_end, height_start, height_end):
    return img[width_start:width_end, height_start:height_end]

# Binarization of the image, to get only black and white (2 colors)
def binarize(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    return cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

res_img = []
for img_loc in img_locations:
    img = cv2.imread(img_loc,0) # cv2.IMREAD_UNCHANGED
    h1, w1 = img.shape
    crop_img = crop(img, 0, w1-150, 0, h1)
    thresh, bin_img = binarize(crop_img)
    res_img.append(bin_img)

# Now we want to search similarities between pictures.
res = cv2.matchTemplate(res_img[0], res_img[0], cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print max_val

cv2.imshow('img1',res_img[0])
cv2.imshow('img2',res_img[1])
cv2.imshow('img3',res_img[2])


cv2.waitKey(0)
cv2.destroyAllWindows()