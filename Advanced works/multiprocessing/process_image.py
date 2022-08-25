import time
import requests
import concurrent.futures
from PIL import Image, ImageFilter

start_time = time.time()

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
]

size = (1200, 1200)

# Without Multiprocessing

# for img_name in img_names:
#     img = Image.open(img_name)
#     img = img.filter(ImageFilter.GaussianBlur(15))

#     img.thumbnail(size)
#     img.save(f'processed/{img_name}')
#     print(f"Image {img_name} is processed.....")

# Multiprocessing
def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(16))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f"Image {img_name} is processed.....")

if __name__=="__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)


    print(f"Process finished --- {round((time.time() - start_time), 2)} seconds ---")