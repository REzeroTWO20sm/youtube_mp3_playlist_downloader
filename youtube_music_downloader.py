import yt_dlp
import os
import PySimpleGUI as sg
import threading


def progress_hook(d):
    if d["status"] == "downloading":
        msg = f"Название: {(d.get('filename', '?')).rsplit('/', 1)[-1]} | Загрузка: {d.get('_percent_str', '?')} | Скорость: {d.get('_speed_str', '?')}"
        window.write_event_value("-STATUS-", msg)
    elif d["status"] == "finished":
        window.write_event_value("-STATUS-", "Конвертация в MP3...")


def download_audio_from_playlist(url, output_path):
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": f"{output_path}/%(title).80s.%(ext)s",
        "download_archive": f"{output_path}/archive.txt",
        "restrictfilenames": False,
        "windows_filenames": False,
        "quiet": False,
        "progress_hooks": [progress_hook],
        "nocheckcertificate": True,
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"],
            }
        },
        "socket_timeout": 30,
        "retries": 10,
        "fragment_retries": 10,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            window.write_event_value("-STATUS-", "Начинаю загрузку плейлиста...")
            ydl.download([url])
            window.write_event_value("-STATUS-", "Готово!")
        except Exception as e:
            window.write_event_value("-STATUS-", f"Ошибка: {e}")


layout = [
    [sg.Text("Введите ссылку на плейлист: "), sg.InputText(key="-LINK-")],
    [sg.Text("Введите путь сохраниеия MP3: "), sg.InputText(key="-PATH-")],
    [sg.Button("Начать загрузку")],
    [sg.Multiline(key="-OUTPUT-", size=(60, 10), disabled=True, autoscroll=True)],
]

window = sg.Window("YoutubeMP3PlaylistDownloader", layout, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Выход"):
        break
    if event == "Начать загрузку":
        window["-OUTPUT-"].update("")
        threading.Thread(
            target=download_audio_from_playlist,
            args=(values["-LINK-"], values["-PATH-"]),
            daemon=True,
        ).start()
    elif event == "-STATUS-":
        window["-OUTPUT-"].print(values["-STATUS-"])

window.close()
