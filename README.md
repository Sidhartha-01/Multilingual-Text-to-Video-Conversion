# Multilingual-Text-to-Video-Conversion
A Python script to generate a video from the given Press Information Bureau (PIB) URL.

**WORKFLOW**
*![Screenshot 2024-05-26 151249](https://github.com/Sidhartha-01/Multilingual-Text-to-Video-Conversion/assets/129527324/15b55431-c17c-4350-93ec-3be8a5c9f2bb)

**STEPS**
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

**DEMO GENERATED VIDEOS**
1. DEMO-1
   URL: https://pib.gov.in/PressReleasePage.aspx?PRID=2021647
   
   GENERATED VIDEO:
   https://github.com/Sidhartha-01/Multilingual-Text-to-Video-Conversion/assets/129527324/f93620ea-b8ce-45f1-92e3-4661b56906e7

2. DEMO-2
   URL: https://pib.gov.in/PressReleasePage.aspx?PRID=2021672

   GENERATED VIDEO:
   https://github.com/Sidhartha-01/Multilingual-Text-to-Video-Conversion/assets/129527324/5b42583d-59a5-4bae-a19b-1bfe30f9ca93

**REFFERED OPEN SOURCE CODE(Wav2Lip)**
1. https://github.com/ajay-sainy/Wav2Lip-GFPGAN
2. https://github.com/Rudrabha/Wav2Lip
3. https://github.com/TencentARC/GFPGAN



