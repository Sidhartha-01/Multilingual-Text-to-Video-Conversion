import os
import subprocess

def LipSync_Anchor(Audio_Location):
    base_path = r"C:\PIB_!!!!!\Wav2Lip-GFPGAN"

    outputPath = os.path.join(base_path, 'outputs')
    # inputAudioPath = os.path.join(base_path, 'inputs', 'kimk_audio.mp3')
    inputAudioPath = Audio_Location
    # print(inputAudioPath)
    inputVideoPath = os.path.join(base_path, 'inputs', 'Anchor2.mp4')
    # inputVideoPath = "C:\PIB_!!!!!\Wav2Lip-GFPGAN\inputs\1.mp4"

    lipSyncedOutputPath = os.path.join(base_path, 'outputs', 'result.mp4')
    checkpoint_path = r"C:\LYPSINC\Wav2Lip-GFPGAN\Wav2Lip-master\checkpoints\checkpoint_file.pth"

    # Create the output directory if it doesn't exist
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    # Define the command
    command = f'cd "C:\LYPSINC\Wav2Lip-GFPGAN\Wav2Lip-master" && python inference.py --checkpoint_path "{checkpoint_path}" --face "{inputVideoPath}" --audio "{inputAudioPath}" --outfile "{lipSyncedOutputPath}"'
    
    # command = (f'cd {"C:\LYPSINC\Wav2Lip-GFPGAN\Wav2Lip-master"} && python inference.py --checkpoint_path checkpoints/wav2lip.pth --face {inputVideoPath} --audio {inputAudioPath} --outfile {lipSyncedOutputPath}')

    # Running the command
    try:
        subprocess.run(command, shell=True, check=True)
        print("Conversion completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the conversion process: {e}")


# LipSync_Anchor("C:\PIB_!!!!!\Generated_Audio.mp3")