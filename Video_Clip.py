from moviepy.editor import *

def Video_clip(file):
    
    l=30
    # a=r"C:\Users\Siddharth\Downloads\m2.mp4"
    #left
    a=file
    #Anchor
    b=r"C:\PIB_!!!!!\Wav2Lip-GFPGAN\outputs\result.mp4" 
    clip1 = VideoFileClip(a).subclip(0,l)
    clip2 = VideoFileClip(b).subclip(0,l)

    # final1 = clip1.fx(vfx.resize,width=200,height=200)
    # final2 = clip2.fx(vfx.resize,width=50,height=50)

    # final1 = clip1.resize((400,200))
    # final2 = clip2.resize((200,200))

    final1 = clip1.resize((400,400))
    final2 = clip2.resize((250,400))

    combined = clips_array([[final1,final2]])

    combined.write_videofile("Actual_Generated_Video.mp4", codec='libx264', bitrate='200000M')
    # combined.write_videofile("BB3.mp4", codec='libx264')
    # combined.ipython_display()

# temp = "temp.mp4";
# Video_clip(rf"C:\PIB_!!!!!\{temp}")