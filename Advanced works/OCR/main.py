import pytesseract
from PIL import Image
import cv2 #pip install pillow opencv-python

myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(Image.open("test.jpg"), config=myconfig)
with open("test_script.txt", "w") as f:
    f.write(text)

import fitz
import io

def extract_images(pdf):
    doc = fitz.open(pdf)
    images = []
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        image_list = page.get_images(full = True)
        for img_index, img in enumerate(image_list):
            base_image = doc.extract_image(img[0])
            image_bytes = base_image['image']
            image = Image.open(io.BytesIO(image_bytes))
        images.append(image)
    return images

def ocr(image_list):
    text = ""
    for i, img in enumerate(image_list):
        text += f"\n\n<{i}>\n"
        text += pytesseract.image_to_string(img, config=myconfig)
    return text


pdf = "1960_Feynman_ Room in the bottom.pdf"
images = extract_images(pdf)
txt = ocr(images)

with open(f"{pdf.split('.')[0]}.txt", "w") as f:
    f.write(txt)