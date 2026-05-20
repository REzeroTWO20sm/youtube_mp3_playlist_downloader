import yt_dlp
import os


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
        "restrictfilenames": True,
        "windows_filenames": True,
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download completed!")
        except Exception as e:
            print(f"Error: {e}")


url = input("playlist_url: ")
file_path = input("file_path: ")
download_audio_from_playlist(url, file_path)
