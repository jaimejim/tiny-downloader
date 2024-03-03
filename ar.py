import os
import click
import requests
from concurrent.futures import ThreadPoolExecutor

def search_archive_org(query):
    search_url = 'https://archive.org/advancedsearch.php'
    params = {
        'q': query,
        'fl[]': 'identifier',
        'rows': 1000,
        'output': 'json',
        'page': 1
    }
    response = requests.get(search_url, params=params)
    search_results = response.json()
    docs = search_results['response']['docs']
    return [doc['identifier'] for doc in docs]

def download_item(identifier, path):
    item_url = f'https://archive.org/metadata/{identifier}'
    response = requests.get(item_url)
    item_metadata = response.json()

    if 'files' in item_metadata:
        for file in item_metadata['files']:
            if file.get('format') == 'MPEG4':
                
                file_url = f"https://archive.org/download/{identifier}/{file['name']}"
                print(f'Starting download: {file["name"]}')
                file_response = requests.get(file_url, stream=True)
                if file_response.status_code == 200:
                    if path:
                        os.makedirs(path, exist_ok=True)
                    filename = os.path.join(path, file['name'])
                    with open(filename, 'wb') as f:
                        for chunk in file_response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    print(f'\033[92mFinished download: {file["name"]}\033[0m')
                else:
                    print(f'Failed to download {file["name"]}. Status code: {file_response.status_code}')
                break 
@click.command()
@click.option('-q', '--query', required=True, help='Search query to find items on Archive.org')
@click.option('-p', '--path', default='', help='Directory to save the downloaded items.')
def cli(query, path):
    identifiers = search_archive_org(query)
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_item, identifiers, [path] * len(identifiers))

if __name__ == '__main__':
    cli()
