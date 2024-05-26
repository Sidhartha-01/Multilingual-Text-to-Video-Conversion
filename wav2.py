import os
import requests

# Define the base path
base_path = r"C:\LYPSINC\Wav2Lip-GFPGAN"

# Define folder names and paths
wav2lip_folder_name = 'Wav2Lip-master'
gfpgan_folder_name = 'GFPGAN-master'
wav2lip_path = os.path.join(base_path, wav2lip_folder_name)
gfpgan_path = os.path.join(base_path, gfpgan_folder_name)

# Define the URLs
s3fd_url = 'https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth'
gdown_url = 'https://drive.google.com/uc?export=download&id=1fQtBSYEyuai9MjBOF8j7zZ4oQ9W2N64q'

# Define the output paths
s3fd_output_path = os.path.join(wav2lip_path, 'face_detection', 'detection', 'sfd', 's3fd.pth')
gdown_output_path = os.path.join(wav2lip_path, 'checkpoints', 'checkpoint_file.pth')

# Ensure the directories exist
os.makedirs(os.path.dirname(s3fd_output_path), exist_ok=True)
os.makedirs(os.path.dirname(gdown_output_path), exist_ok=True)

# Function to download a file from a URL
def download_file(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {output_path}")
    else:
        raise Exception(f"Failed to download file from {url}. Status code: {response.status_code}")

# Download the s3fd.pth file
download_file(s3fd_url, s3fd_output_path)

# Download the file from Google Drive using the direct download link
download_file(gdown_url, gdown_output_path)

print("All files downloaded successfully.")
