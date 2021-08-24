import cv2
import numpy as np

img = cv2.imread("niebieska_foczka.jpeg")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")

try:
    adj = int(input("      Hue Change by Factor[0-18]:  "))
except:
    print("Wrong value")

(h,s,v) = cv2.split(imghsv)
h = (h+adj*10)%180
#h = np.clip(h,0,179)
imghsv = cv2.merge([h,s,v])

imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)

cv2.imshow('New Hue', imgrgb)
cv2.waitKey(0)
