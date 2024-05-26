from PIL import Image, ImageOps
import os


def add_border(location):
    border_size = 20  # Adjust the border size as needed
    border_color = (0,)  # Specify the border color as an RGB tuple (red in this case)
    for images in os.listdir(location):
        # print(images)
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
            # images=''.join(images.split('.'))
            path = os.path.join(location, images)
            image = Image.open(path)
            image.info.clear()
            image.save(path)

            image = Image.open(path)
            image = image.resize((400, 400))
            try:
                # Add a border to the image
                bordered_image = ImageOps.expand(image, border=border_size, fill=border_color)

                # Save the result to the same file, overwriting the original image
                bordered_image.save(path)
            except Exception as e:
                print("Occured Error?")
                continue

    print("Successfully Added Border!!")


# add_border(r"C:\PIB_!!!!!\images\Resultant_Generated_Images")