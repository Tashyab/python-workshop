import pytesseract
import PIL.Image
import cv2 #pip install pillow opencv-python

myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("test.jpg"), config=myconfig)
with open("test_script.txt", "a+") as f:
    f.write(text)
