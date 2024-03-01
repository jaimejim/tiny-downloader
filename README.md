# Tiny Downloader

This is a simple script to download youtube videos or playlists. It uses the `pytube` library to fetch and download videos, and `concurrent.futures` to parallelize downloads for playlists.

## Installation

- Install dependencies with [poetry](https://python-poetry.org/docs/#installation):

```bash
poetry install
```

-  Download a single video

```bash
poetry run python3 yt.py -d 'https://youtu.be/SlkxxHnh3tA'
```

- Download a playlist, videos are saved in the current directory or in a subdirectory for playlists.

```bash
poetry run python3 yt.py -d "https://www.youtube.com/watch?v=sOYPv4R6qSc&list=PLGUXlYAlP4EJ2y7vsmMU_UNQe3PtXqm_K"
Starting download for playlist: Erase Una Vez... La Vida
Starting download: Erase Una Vez... El Cuerpo Humano - Guerra a las toxinas
Starting download: Erase Una Vez... El Cuerpo Humano - El oido
Starting download: Erase Una Vez... El Cuerpo Humano - La respiracion
Starting download: Erase Una Vez... El Cuerpo Humano - La médula osea
Starting download: Erase Una Vez... El Cuerpo Humano - La vida y el sueno
Finished download: Erase Una Vez... El Cuerpo Humano - El oido
Starting download: Erase Una Vez... El Cuerpo Humano - Hormonas
Finished download: Erase Una Vez... El Cuerpo Humano - La vida y el sueno
Starting download: Erase Una Vez... El Cuerpo Humano - La vista
Finished download: Erase Una Vez... El Cuerpo Humano - Guerra a las toxinas
Starting download: Erase Una Vez... El Cuerpo Humano - La sangre
Finished download: Erase Una Vez... El Cuerpo Humano - La respiracion
Starting download: Erase Una Vez... El Cuerpo Humano - Los huesos y el esqueleto
```

## Note

I have set up the concurrent workers to `5`, a higher number may cause youtube to temporarily block your IP. 