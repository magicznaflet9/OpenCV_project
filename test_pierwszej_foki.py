import cv2
print("I got here")
img = cv2.imread("/Users/zofiabochenek/test/FOKA.png")
cv2.imshow("puszysta foczka",img)
cv2.waitKey(0)
img = cv2.imread("/Users/zofiabochenek/test/FOKA.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("puszysta foczka w skali szarości",img)
cv2.waitKey(0)
#cv2.destroyAllWindows()

print("Pamiętaj zabrać skarpety")
