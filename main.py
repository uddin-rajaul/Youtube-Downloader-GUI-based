import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def choose_download_location():
    global download_folder
    download_folder = filedialog.askdirectory()
    if download_folder:
        status_text.set("Download location selected.")
    else:
        status_text.set("No download location selected.")

def download_video():
    video_url = entry.get()
    if download_folder:
        try:
            status_text.set("Downloading video or playlist...\nThis may take several minutes.")
            process = subprocess.Popen(f'youtube-dl --yes-playlist -x --audio-format mp3 -o "{download_folder}/%(title)s.%(ext)s" {video_url}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while process.poll() is None:
                output = process.stdout.readline().decode()
                status_text.set(output)
            status_text.set("Video or playlist downloaded and converted to MP3!")
        except Exception as e:
            status_text.set("An error occurred while downloading the video or playlist.")
    else:
        status_text.set("No download location selected.")

root = tk.Tk()
root.title("YouTube Video/Playlist Downloader")

canvas = tk.Canvas(root, height=500, width=800)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.11, anchor='n')

entry = tk.Entry(frame, font=40)
entry.pack(side="left", fill="both", expand=True)

download_location_button = tk.Button(frame, text="Choose Download Location", command=choose_download_location)
download_location_button.pack(side="left")

download_button = tk.Button(frame, text="Download Video/Playlist", command=download_video)
download_button.pack(side="left")

status_text = tk.StringVar()
status_text.set("Enter a YouTube video or playlist link and select a download location.")
status_label = tk.Label(root, textvariable=status_text)
status_label.pack(side="top", fill="both", expand=True)

root.mainloop()
