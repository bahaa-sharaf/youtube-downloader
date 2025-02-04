import customtkinter as ctk
import yt_dlp
import os
import threading

class YouTubeDownloader:
    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.title("YouTube Downloader by Bahaa Sharaf and ChatGPT v2")
        self.root.geometry("500x400")
        self.root.grid_columnconfigure((0, 1), weight=1)

        self.title = ctk.CTkLabel(self.root, text="YouTube Downloader", font=('Montserrat Bold', 27))
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(30,0))

        self.subtitle = ctk.CTkLabel(self.root, text="By Bahaa Sharaf ft. ChatGPT & DeepSeek", font=('Montserrat', 14))
        self.subtitle.grid(row=self.title.grid_info()['row']+1, column=0, columnspan=2, padx=10, pady=(0,10))

        self.url_box = ctk.CTkEntry(self.root, width=350, placeholder_text="Enter YouTube URL")
        self.url_box.grid(row=self.subtitle.grid_info()['row']+1, column=0, columnspan=2, padx=10, pady=10)

        self.choice = "" # v for video, a for audio

        self.video = ctk.CTkButton(self.root, width=60, text="Download Video", command=self.video)
        self.video.grid(row=self.url_box.grid_info()['row']+1, column=0, padx=10, pady=10)

        self.audio = ctk.CTkButton(self.root, width=60, text="Download Audio", command=self.audio)
        self.audio.grid(row=self.url_box.grid_info()['row']+1, column=1, padx=10, pady=10)

        self.quality_label = ctk.CTkLabel(self.root, text="Select the video quality:")

        self.quality_var = ctk.StringVar(value="best")
        self.vquality_720 = ctk.CTkRadioButton(self.root, text="720", value="720", variable=self.quality_var)
        self.vquality_1080 = ctk.CTkRadioButton(self.root, text="1080", value="1080", variable=self.quality_var)
        self.vquality_highest = ctk.CTkRadioButton(self.root, text="Highest", value="best", variable=self.quality_var)

        self.submit = ctk.CTkButton(self.root, width=60, text="Submit", command=self.submit)
        self.submit.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = ctk.CTkLabel(self.root, text="", font=("Consolas", 12))
        self.result_label.grid(row=16, column=0, columnspan=2)

        self.root.mainloop()


    # Functions
    def video(self):
        self.quality_label.grid(row=self.video.grid_info()['row']+1, column=0, columnspan=2)
        self.vquality_720.grid(row=self.quality_label.grid_info()['row']+1, column=0, columnspan=2)
        self.vquality_1080.grid(row=self.vquality_720.grid_info()['row']+1, column=0, columnspan=2)
        self.vquality_highest.grid(row=self.vquality_1080.grid_info()['row']+1, column=0, columnspan=2)
        self.choice="v"

    def audio(self):
        self.quality_label.grid_forget()
        self.vquality_720.grid_forget()
        self.vquality_1080.grid_forget()
        self.vquality_highest.grid_forget()
        self.choice="a"


    def DownloadVideo(self):
        print(f"url: {self.url}\nchoice(v/a): {self.choice}\nquality: {self.quality_var.get()}")

        self.ydl_opts = {'outtmpl': os.path.join(self.output_path, '%(title)s (Video).%(ext)s'),
                         'format': self.quality_var.get()}
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
                self.result_label.configure(bg_color='transparent', text="Successfully downloaded!", text_color='green')
        except Exception as e:
            print(f"Error: {e}")
            self.result_label.configure(bg_color="#5a0c19", text=f"Error: {e}", text_color='white')


    def DownloadAudio(self):
        self.ydl_opts = {'outtmpl': os.path.join(self.output_path, '%(title)s (Audio).%(ext)s'),
                    'format': "bestaudio",
                    'postprocessors':[{'key': 'FFmpegExtractAudio',
                                       'preferredcodec': 'mp3'}]}
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
                self.result_label.configure(bg_color='transparent', text="Successfully downloaded!", text_color='green')
        except Exception as e:
            print(f"Error: {e}")
            self.result_label.configure(bg_color="#5a0c19", text=f"Error: {e}", text_color='white')


    def submit(self):
        self.result_label.configure(text="Downloading...")
        self.url = self.url_box.get()
        
        self.output_path = "Downloads"  # Change this to your desired output folder
        os.makedirs(self.output_path, exist_ok=True)

        if self.choice == "v":
            threading.Thread(target=self.DownloadVideo, daemon=True).start()
        else:
            threading.Thread(target=self.DownloadAudio, daemon=True).start()
    

YouTubeDownloader()
