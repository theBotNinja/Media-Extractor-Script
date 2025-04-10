# 📁 Media Extractor Script

A handy Python script to **extract and organize images, documents, videos, and audio files** from a selected folder (including all its subfolders) into categorized folders.



## 🚀 Features

- Recursively searches a directory and its subdirectories.
- Extracts and organizes:
  - 📷 Images
  - 📄 Documents
  - 🎥 Videos
  - 🎵 Audio files
- Option to **copy** or **move** files.
- Supports a wide range of file extensions.
- User-friendly prompts via terminal and folder picker.



## 🧠 How It Works

1. You choose the **source** directory (to extract from).
2. You choose the **destination** directory (to store extracted files).
3. The script:
   - Scans all subfolders.
   - Identifies file types using extension mappings.
   - Sorts and places them into folders named:
     - `imageExt/`
     - `docExt/`
     - `videoExt/`
     - `audioExt/`
4. You decide whether to **copy** or **move** the files.



## 🛠️ Requirements

- Python 3.x
- `tkinter` (used for GUI folder picker – preinstalled with most Python distributions)
- `shutil`, `os`, `time`, `random` (standard Python libraries)



## 📦 Setup & Usage

1. Clone or download this repo.
2. Run the script:

```Run
python media_ext.py
