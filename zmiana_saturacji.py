import cv2
import numpy as np

img = cv2.imread("niebieska_foczka.jpeg")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")

try:
    adj = int(input("      Saturation Change by Factor:  "))
except:
    print("Wrong value")

(h,s,v) = cv2.split(imghsv)
s = s*adj-2*adj
s = np.clip(s,0,255)
imghsv = cv2.merge([h,s,v])

imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)

cv2.imshow('New Saturation', imgrgb)
cv2.waitKey(0)
