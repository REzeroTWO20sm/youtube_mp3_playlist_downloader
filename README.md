# YouTube Playlist to MP3 Downloader

Программа позволяет скачать все видео из плейлиста на YouTube в формате MP3.

## Требования быстрый старт windows

- Доступ к YouTube (zapret, vpn, proxy и другие типы обходов)

## Быстрый старт в Widnows

1. [Переходим в Relese](https://github.com/REzeroTWO20sm/youtube_mp3_playlist_downloader/releases/tag/Youtube_Playlist_mp3_downloader) и скачиваем архив windows_youtube_mp3_playlist_downloader_with_ffmpeg.
2. Разархивируйте его
3. Запускаем прямо из папки файл YoutubeMP3PlaylistDownloader.exe и можем использовать программу

## Требования source code

- ffmpeg в системных путях (БЕЗ НЕГО РАБОТАТЬ НЕ БУДЕТ)
- Python 3.10 или выше
- Доступ к YouTube (проверьте, зайдя в браузер)

## Установка source code

1. Создание виртуального окружения:
```bash
python -m venv venv
```

2. Активация виртуального окружения:

Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

Windows (CMD):
```cmd
venv\Scripts\activate.bat
```

Linux:
```bash
source venv/bin/activate
```

3. Установка зависимостей:
```bash
pip install -r requirements.txt
```

## Использование

Запуск программы:
```bash
python youtube_music_downloader.py
```
