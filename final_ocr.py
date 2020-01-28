import cv2
import pytesseract

cap = cv2.VideoCapture('/home/nithing/Desktop/alita_cast.mp4')
i = 0
f = open("datasheet1.txt", "a+")
f.truncate(0)
temp_text = ""
while (cap.isOpened()):
    ret, image = cap.read()

    if ret == False:
        break
    if i % 24 == 0:
        image = cv2.bitwise_not(image)
        cv2.imshow("", image)
        cv2.waitKey(20)
        text = pytesseract.image_to_string(image)
        print(text)
        if temp_text == text:
            continue
        else:
            f.write(text + " ,")
            temp_text = text

    i += 1
f.close()

cap.release()
cv2.destroyAllWindows()
