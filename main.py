import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def download_video():
    video_url = entry.get()
    download_folder = filedialog.askdirectory()
    if download_folder:
        try:
            status_text.set("Downloading video or playlist...\nThis may take several minutes.")
            #os.system(f'youtube-dl -x --audio-format mp3 -o "{download_folder}/%(title)s.%(ext)s" {video_url}')
            os.system(f'youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-formatmp3 --audio-quality160K --output "%(title)s.%(ext)s" --yes-playlist {video_url}')
            status_text.set("Video or playlist downloaded and converted to MP3!")
        except Exception as e:
            status_text.set("An error occurred while downloading the video or playlist.")
    else:
        status_text.set("No download location selected.")

root = tk.Tk()
root.title("YouTube Video/Playlist Downloader")

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry = tk.Entry(frame, font=40)
entry.pack(side="left", fill="both", expand=True)

download_button = tk.Button(frame, text="Download Video/Playlist", command=download_video)
download_button.pack(side="left")

status_text = tk.StringVar()
status_text.set("Enter a YouTube video or playlist link above and select a download location.")
status_label = tk.Label(root, textvariable=status_text)
status_label.pack(side="top", fill="both", expand=True)

root.mainloop()
