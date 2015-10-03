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

def find_match(img, templates):
    max_res = 2 # impossible value
    tmpl_match = 0
    for i in range(len(templates)):
        res = cv2.matchTemplate(img, templates[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if min_val < max_res:
            max_res = max_val
            tmpl_match = i

    return tmpl_match, max_res

def show_binary_images(imgs):

    ite = 0
    for i in imgs:
        cv2.imshow('img' + str(ite),res_img[0])
        ite += 1

    cv2.waitKey(0)
    cv2.destroyAllWindows()

res_img = []
for img_loc in img_locations:
    img = cv2.imread(img_loc,0) # cv2.IMREAD_UNCHANGED
    h1, w1 = img.shape
    crop_img = crop(img, 0, w1-150, 0, h1)
    thresh, bin_img = binarize(crop_img)
    res_img.append(bin_img)

# We have created templates to work with
# Now we want to search similarities between pictures.
# Ideally you would have a database of template already ready

# In this case, we imagine that template number 1 is the image taken by the user.
# We then match this template against our knowledge database (templates 1 to 3).
# Since we match an image against itself, the result should be obvious.
test_img = res_img[2]
templates = res_img
tmpl_match, max_res = find_match(test_img, templates)

print "The best template is : " + str(tmpl_match) + " with correlation value " + str(max_res)
show_binary_images(res_img)