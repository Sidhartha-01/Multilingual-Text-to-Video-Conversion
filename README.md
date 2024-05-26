# Multilingual-Text-to-Video-Conversion
A Python script to generate a video from the given Press Information Bureau (PIB) URL.

**Work-Flow**
![WhatsApp Image 2024-05-26 at 15 13 10_8fc4735d](https://github.com/Sidhartha-01/Multilingual-Text-to-Video-Conversion/assets/129527324/e3ed21c8-e7c9-416f-9dc9-940724c311f9)

**Steps:**
1. Give the PIB- URL.
2. Now it will process/runs all the files.
   By generating,  
   1. Summary.
   2. From summary generating the Speech.
   3. Now generates the lip-Sync video stored in "Wav2Lip-GFPGAN\outputs".
   4. Generates required tokens -> Images.
   5. Adds up Border and changes Background.
   6. From the images generates Image-Sequence Clip.
   7. Merging the Lip-Sync Clip and Image-Sequence Clip.

3. Now the Actual video is generated as \Actual_Generated_Video.mp4.
