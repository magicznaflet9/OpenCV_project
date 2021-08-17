import cv2
import time

user = input("(g)rayscale / (c)color (q)uit\n")
while user != "q":
    if user == "g":
        img = cv2.imread("/Users/zofiabochenek/test/FOKA.png",cv2.IMREAD_GRAYSCALE)
        cv2.imshow("puszysta foczka w skali szarości",img)
        print("before waitkey")
        cv2.waitKey(50)
        print("after waitkey")
        cv2.destroyAllWindows()
        print("after destroyall")
        time.sleep(1)
        print("after sleep")
    elif user == "c":
        img = cv2.imread("/Users/zofiabochenek/test/FOKA.png",cv2.IMREAD_COLOR)
        cv2.imshow("puszysta foczka w kolorze",img)
        cv2.waitKey(0)
        time.sleep(1)
        cv2.destroyAllWindows()
    else:
        print("Nie ma takiej komendy leszczu")
    user = input("Wybierz coś innego: (g)rayscale / (c)color (q)uit\n")
print("Koniec")
