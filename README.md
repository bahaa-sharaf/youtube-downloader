# YouTube Downloader Program

This is a simple program created using **CustomTkinter** to download audio or video from YouTube. It leverages the `yt_dlp` library to handle the downloading process and uses **threading** to ensure the program remains responsive during downloads.

---

## Features
- **Download Video**: Download videos from YouTube in your preferred quality (720p, 1080p, or the highest available).
- **Download Audio**: Extract audio from YouTube videos and save it as an MP3 file.
- **Responsive UI**: The program uses threading to run the download process in the background, ensuring the interface remains responsive.

---

## Requirements
To run this program on your device, you need to:

1. **Install Required Modules**:
   - Install `customtkinter` for the graphical user interface.
   - Install `yt_dlp` for downloading YouTube videos and audio.

   You can install these modules using `pip`:
   ```bash
   pip install customtkinter yt_dlp
   ```

2. **Set the Output Folder**:
    - Change the output folder path in the code to your desired location (e.g., your Downloads folder):
    - In the code, locate the following line (around line 98):
    ```python
    self.output_path = "Downloads"
    ```
    - Replace the path with your preferred output directory.

---

## How It Works
  1. Run the program.
  2. Enter a YouTube URL in the provided text box.
  3. Choose whether to download video or audio.
  4. Quality
      - For video downloads, you can choose between 720p, 1080p, or the highest available quality. Video is saved as an MP4 file.
      - For audio downloads, the program extracts the best audio quality and saves it as an MP3 file.
  6. Click "Submit" to start the download.
  7. The program will display the download status (e.g., "Downloading...", "Successfully downloaded!", or an error message).


## Example Output Folder Structure
After downloading, your output folder will look something like this:
```
Downloads/
├── YouTube Video Downloader/
│   ├── Video Title (Video).mp4
│   ├── Video Title (Audio).mp3
│   └── ...
```
