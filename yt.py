import os
import click
from pytube import YouTube, Playlist
from concurrent.futures import ThreadPoolExecutor

def download(url, path=None, retries=3):
    for _ in range(retries):
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            print(f'Starting download: {video.title}')
            if path:
                os.makedirs(path, exist_ok=True)
            video.download(path)
            print(f'\033[92mFinished download: {video.title}\033[0m')
            return 1
        except Exception as e:
            print(f"\nError downloading {url}: {str(e)}")
    return 0

@click.command(context_settings={"help_option_names": ['-h', '--help']})
@click.option('-d', '--download', 'url', help='''
\b
URL of the YouTube video or playlist to download.
''')
def cli(url):
    """Download a single video or a whole playlist."""
    if 'list' in url:
        playlist = Playlist(url)
        print(f"Starting download for playlist: {playlist.title}")

        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(download, playlist.video_urls, [playlist.title]*len(playlist.video_urls)))

        print(f"\nDownloaded {sum(results)} videos from the playlist.")
    else:
        download(url)

if __name__ == '__main__':
    cli()