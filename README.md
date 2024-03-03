# Tiny Downloader

This are a couple of simple scripts to download videos or playlists from Youtube or Archive.org. Downloads are parallelized using `concurrent.futures` for efficiency.

## Installation

- Install dependencies with [poetry](https://python-poetry.org/docs/#installation):

```bash
poetry install
```

### Downloading from YouTube

- Download a single video:

```bash
poetry run python3 yt.py -d 'https://youtu.be/SlkxxHnh3tA'
```

- Download a playlist (videos are saved in the current directory or in a subdirectory for playlists):

```bash
poetry run python3 yt.py -d "https://www.youtube.com/watch?v=sOYPv4R6qSc&list=PLGUXlYAlP4EJ2y7vsmMU_UNQe3PtXqm_K"
Starting download for playlist: Erase Una Vez... La Vida
Starting download: Erase Una Vez... El Cuerpo Humano - Guerra a las toxinas
Starting download: Erase Una Vez... El Cuerpo Humano - El oido
```

### Downloading from Archive.org

- Download videos by a search query to the API. For example, this will download videos matching the search query from Archive.org:

```bash
poetry run python ar.py --query "subject:\"Sinfonías Tontas\"" -p "sinfonias tontas"
Starting download: 50 - 02 El Toque de Oro (1935) (2do Redoblaje).mp4
Starting download: 38 - 02 La Tierra de los Sueños (1933) (2do Redoblaje).mp4
Starting download: 74 - 01 El Cerdito Práctico (1939) (1er Redoblaje).mp4
Starting download: 17 - Melodías de Mamá Ganso (1931) (2do Redoblaje).mp4
```

## Note

The concurrent workers are set to `5`. A higher number may cause YouTube to temporarily block your IP. For Archive.org downloads, ensure you comply with their terms of service and use responsibly to avoid overloading their servers.