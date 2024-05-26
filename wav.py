import subprocess
import os

# Define the repository URL and base path
repo_url = "https://github.com/ajay-sainy/Wav2Lip-GFPGAN.git"
base_path = "C:\LYPSINC\Wav2Lip-GFPGAN"

# Clone the repository
subprocess.run(["git", "clone", repo_url])

# Change the current working directory to the cloned repository
os.chdir(base_path)

# Print the current working directory to verify
print("Current working directory:", os.getcwd())
