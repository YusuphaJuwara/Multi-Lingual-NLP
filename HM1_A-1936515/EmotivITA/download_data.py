import os
import requests

def download_csv_files(api_url, save_folder):
    """Download all CSV files from a GitHub repository.

    Args:
        api_url (str): The URL of the GitHub API endpoint for the repository.
        save_folder (str): The path to save the downloaded CSV files.
    """
    # Make a GET request to the GitHub API to fetch repository contents
    response = requests.get(api_url)
    if response.status_code == 200:
        repo_contents = response.json()
        for content in repo_contents:
            if content["type"] == "file" and content["name"].endswith(".csv"):
                file_url = content["download_url"]
                file_name = content["name"]
                file_path = os.path.join(save_folder, file_name)
                file_data = requests.get(file_url).content
                with open(file_path, "wb") as f:
                    f.write(file_data)
                print(f"{file_path} downloaded successfully.")
            elif content["type"] == "dir":
                sub_dir_url = content["url"]
                download_csv_files(sub_dir_url, save_folder)
    else:
        print(f"Failed to fetch repository contents from the API {api_url=}. \nStatus code: {response.status_code}")

if __name__ == "__main__":
    
    repo_url = "https://api.github.com/repos/GiovanniGafa/EmoITA/contents/"
    save_folder = "EmotivITA/save_folder"

    # Create the save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    download_csv_files(repo_url, save_folder)
