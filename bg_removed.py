from PIL import Image,ImageOps
import os
from os import listdir
import cv2

def BG_adder(location):  # direcoty name
    i = 1
    Total = []
    # border_size = 30  # Adjust the border size as needed
    # border_color = (0, 0, 0)  # Specify the border color as an RGB tuple (red in this case)

    folder_dir = location
    for images in os.listdir(folder_dir):

        img1 = Image.open(r"C:\PIB_!!!!!\Blue-bg.jpg")  # background
        Image1copy = img1.copy()
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
            path = os.path.join(folder_dir, images)
            img2 = Image.open(path)  # small inage
            Image2copy = img2.copy()
            # Image2copy = cv2.imread(Image2copy)
            # Image2copy = cv2.copyMakeBorder(
            #     Image2copy, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 0])

            new_image = Image2copy.resize((500, 500))
            # new_image = ImageOps.expand(new_image, border=border_size, fill=border_color)

            width = img1.width - 100
            height = img1.height + 100

            Image1copy.paste(new_image, (width // 3, height // 4))

            # Image1copy.show()
            final_name = 'image' + str(i) + '.png'
            path2 = os.path.join(folder_dir, final_name)
            Image1copy.save(path2)
            Total.append(Image1copy)
            os.remove(path)
            i = i + 1


# BG_adder(r"C:\PIB_!!!!!\images\Resultant_Generated_Images")
