# yt.py

import os
import click
from pytube import YouTube, Playlist
from concurrent.futures import ThreadPoolExecutor
import fix 

def download(url, path=None, retries=3):
    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1} of {retries} for {url}")
            yt = YouTube(url)
            print(f"Video title: {yt.title}")
            video = yt.streams.get_highest_resolution()
            print(f'Starting download: {video.title}')
            if path:
                os.makedirs(path, exist_ok=True)
            video.download(path)
            print(f'\033[92mFinished download: {video.title}\033[0m')
            return 1
        except Exception as e:
            print(f"\nError downloading {url} on attempt {attempt + 1}/{retries}: {str(e)}")
            if "HTTP Error 400" in str(e):
                print("It seems like the URL is not properly formed or there's an issue with the request.")
            else:
                print(f"An unexpected error occurred: {str(e)}")
    return 0

@click.command(context_settings={"help_option_names": ['-h', '--help']})
@click.option('-d', '--download', 'url', help='''
\b
URL of the YouTube video or playlist to download.
''')
def cli(url):
    """Download a single video or a whole playlist."""
    if 'list=' in url:
        try:
            playlist = Playlist(url)
            print(f"Starting download for playlist: {playlist.title}")

            with ThreadPoolExecutor(max_workers=5) as executor:
                results = list(executor.map(download, playlist.video_urls, [playlist.title]*len(playlist.video_urls)))

            print(f"\nDownloaded {sum(results)} videos from the playlist.")
        except Exception as e:
            print(f"Failed to download playlist: {str(e)}")
    else:
        try:
            download(url)
        except Exception as e:
            print(f"Failed to download video: {str(e)}")

if __name__ == '__main__':
    cli()
