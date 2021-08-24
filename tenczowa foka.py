import cv2
import numpy as np

img = cv2.imread("niebieska_foczka.jpeg")
user = input("For rainbow press (y)es, to Quit press (n)o\n")

while user != "n":
    for adj in range(0,37):
        print(adj)
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
        (h,s,v) = cv2.split(imghsv)
        h = (h+adj*10)%180
        #h = np.clip(h,0,179)
        imghsv = cv2.merge([h,s,v])
        imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
        cv2.imshow('Tenczowa foka', imgrgb)
        cv2.waitKey(100)
    cv2.imshow('Tenczowa foka', img)
    cv2.waitKey(1000)
    user = input("For rainbow press (y)es, to Quit press (n)o\n")
  

