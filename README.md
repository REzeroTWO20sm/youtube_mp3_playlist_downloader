```markdown
# YouTube Playlist to MP3 Downloader

Скрипт позволяет скачать все видео из плейлиста на YouTube в формате MP3.

## Требования

- Python 3.10 или выше
- Доступ к YouTube (проверьте, зайдя в браузер)

## Установка

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

Запуск скрипта:
```bash
python youtube_music_downloader.py
```

При запуске скрипт запросит:
- `playlist_url` — ссылка на плейлист YouTube
- `file_path` — путь, куда скачаются MP3 файлы
```
