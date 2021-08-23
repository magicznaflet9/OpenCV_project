import cv2
import numpy as np

img = cv2.imread("niebieska_foczka.jpeg")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
##print("------img------\n",img)
##print("------imghsv------\n",imghsv)

gamma = float(input("       INPUT GAMMA:       "))
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(i*gamma + 2, 0, 255)
    #print(np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255))
#print("------lookUpTable------\n",lookUpTable)
res = cv2.LUT(imghsv, lookUpTable)
##print("------res------\n",res)

imgrgb = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

cv2.imshow('New Saturation', imgrgb)

cv2.waitKey(0)

