import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_website(url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Save HTML
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    # Download CSS and JS files
    for tag, attr in [('link', 'href'), ('script', 'src')]:
        for resource in soup.find_all(tag):
            file_url = resource.get(attr)
            if file_url:
                file_url = urljoin(url, file_url)
                try:
                    download_file(file_url, output_dir)
                except Exception as e:
                    print(f"Failed to download {file_url}: {e}")

def download_file(file_url, output_dir):
    local_filename = os.path.join(output_dir, os.path.basename(file_url))
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded {file_url} to {local_filename}")
    else:
        print(f"Failed to fetch {file_url}: {response.status_code}")

if __name__ == "__main__":
    print("Welcome to the website downloader!")
    website_url = input("Please enter the URL of the website you want to download: ")
    output_directory = "website_copy"
    
    print(f"Downloading the website: {website_url}")
    download_website(website_url, output_directory)
    print(f"Website has been downloaded and saved to the '{output_directory}' folder.")
