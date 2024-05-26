import subprocess

# Define the path to the requirements.txt file
requirements_path = r"C:\LYPSINC\Wav2Lip-GFPGAN\requirements.txt"

# Function to install packages from requirements.txt
def install_requirements(requirements_path):
    try:
        subprocess.run(['pip', 'install', '-r', requirements_path], check=True)
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")

# Install required packages
install_requirements(requirements_path)

