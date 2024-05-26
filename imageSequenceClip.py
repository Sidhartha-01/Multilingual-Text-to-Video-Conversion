from moviepy.editor import *
import os

def imageSequence(location,checked,Name_of_Video):
    img=[]
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    for images in os.listdir(location):
        if images.endswith(image_extensions):
            pathu=os.path.join(location,images)
            img.append(pathu)
    print(img)
    clips = [ImageClip(m).set_duration(3) for m in img]

    con = concatenate_videoclips(clips, method="compose")
    image_sequence_file=Name_of_Video+'.mp4'
    print(image_sequence_file)
    con.write_videofile(image_sequence_file, fps=24)

# imageSequence(r"C:\Users\Raviteja K\PycharmProjects\opencv1\venv\images\hello",3,"temp")
# imageSequence(r"C:\PIB_!!!!!\images\Resultant_Generated_Images",3,"temp")