import os
import re
import requests
from urllib.parse import urlparse
import sys

def extract_urls(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = re.findall(url_pattern, data)
        return urls

def save_urls_to_file(urls, file_path):
    with open(file_path, 'w') as file:
        for url in urls:
            file.write(url + '\\n')

def download_files(urls, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    downloaded_files = 0
    empty_files = 0
    failed_connections = 0
    for url in urls:
        file_name = os.path.basename(urlparse(url).path)
        if not file_name:
            continue
        try:
            response = requests.get(url)
            if response.content:
                with open(os.path.join(folder_path, file_name), 'wb') as file:
                    file.write(response.content)
                downloaded_files += 1
                print(f"He descargado {downloaded_files}/{len(urls)} documentos")
            else:
                empty_files += 1
        except requests.exceptions.RequestException as e:
            print(f"No se pudo descargar el archivo {url}. Error: {e}")
            failed_connections += 1

    return downloaded_files, empty_files, failed_connections

def main():
    # Check if a file name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Por favor, proporciona un nombre de archivo como argumento en la línea de comandos.")
        return

    # Get the file name from the command line arguments
    file_name = sys.argv[1]

    # Extract URLs from the document
    urls = extract_urls(file_name)

    # Remove duplicate URLs
    urls = list(set(urls))

    # Save the URLs to a .txt file
    save_urls_to_file(urls, 'urls.txt')

    # Download the files
    downloaded_files, empty_files, failed_connections = download_files(urls, 'downloaded_files')

    # Print the results
    print(f"Se encontraron {len(urls)} URLs distintas.")
    print(f"Se descargaron {downloaded_files} archivos.")
    print(f"No se pudo conectar a {failed_connections} URLs.")
    print(f"{empty_files} URLs no tenían nada para descargar.")

# Run the main function
if __name__ == "__main__":
    main()
