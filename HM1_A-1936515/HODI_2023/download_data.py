# This part is for downloading the password-protected HODI dataset zip file

import os
import requests
import pyzipper

def download_file(url, save_path):
    """Download the password-protected HODI dataset zip file from the URL and save it to the specified path.

    Args:
        url (str): the GitHub URL of the zip file
        save_path (str): the path to save the downloaded file

    Returns:
        bool: True if the file was downloaded successfully, False otherwise
    """
    with requests.get(url, stream=True) as response:
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"File downloaded successfully to: {save_path}")
            return True
        else:
            print(f"Failed to download file from: {url}")
            return False

def unzip_file(zip_path, extract_dir, password=None):
    """Unzip the password-protected HODI dataset zip file to the specified directory.
    
    Make sure to have already installed the pyzipper (pip install pyzipper)

    Args:
        zip_path (str): the path to the zip file
        extract_dir (str): the directory to extract the zip file
        password (str, optional): the password to decrypt the zip file. Defaults to None.
    """
    with pyzipper.AESZipFile(zip_path, 'r', compression=pyzipper.ZIP_LZMA) as zf:
        if password:
            zf.setpassword(password.encode())
        zf.extractall(extract_dir)
    print(f"File unzipped successfully to: {extract_dir}")
    
def download_and_unzip(zip_url, zip_save_path, extract_dir):
    """Download the password-protected HODI dataset zip file from the URL 
    and unzip it to the specified directory.
    
    Args:
        zip_url (str): the GitHub URL of the zip file
        zip_save_path (str): the path to save the downloaded file
        extract_dir (str): the directory to extract the zip file
        
    Returns:
        None
        
    Example:
        download_and_unzip('https://github.com/HODI-EVALITA/HODI_2023_data/raw/main/HODI_2023_train.zip',
                           'HODI_2023/save_folder/HODI_2023_train.zip',
                           'HODI_2023/save_folder/HODI_2023_train')
    """
    # Download the password-protected ZIP file
    if download_file(zip_url, zip_save_path):
        # Unzip the downloaded file
        unzip_file(zip_save_path, extract_dir, password="hodi23evalita")
    
if __name__ == "__main__":
    # URL and file paths
    zip_url = "https://github.com/HODI-EVALITA/HODI_2023_data/raw/main/HODI_2023_train.zip"
    zip_save_path = "HODI_2023/save_folder/HODI_2023_train.zip"
    extract_dir = "HODI_2023/save_folder/HODI_2023_train"
    
    # Create the save folder if it doesn't exist
    os.makedirs("HODI_2023/save_folder", exist_ok=True)

    download_and_unzip(zip_url, zip_save_path, extract_dir)