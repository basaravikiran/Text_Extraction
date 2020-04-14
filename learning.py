"""
import numpy as np
import cv2
img=cv2.imread('Screenshot.png')

print((img.shape))

cv2.imshow('ImageWindow', img)
cv2.waitKey(5000)

import cv2
import pytesseract

img = cv2.imread('image.jpg')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)
"""
import cv2
import pytesseract
img = cv2.imread("Screenshot.png")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_crop = img[80:150,0:290]
cv2.imshow("cropped", img_crop)
cv2.waitKey(0)
img_rgb = cv2.cvtColor(img_crop, cv2.COLOR_BGR2RGB)
custom_config = r'--oem 3 --psm 6'
text_output= pytesseract.image_to_string(img_rgb, config=custom_config)
print(text_output=='Network\nconnection lost')

img_crop1 = img[730:800,120:295]
cv2.imshow("cropped", img_crop1)
cv2.waitKey(0)
img_rgb = cv2.cvtColor(img_crop1, cv2.COLOR_BGR2RGB)
text_output= pytesseract.image_to_string(img_rgb, config=custom_config)
print(text_output)


gray = cv2.cvtColor(img_crop1,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow("cropped", thresh)
cv2.waitKey(0)
text_output= pytesseract.image_to_string(thresh, config=custom_config)
print(text_output)
