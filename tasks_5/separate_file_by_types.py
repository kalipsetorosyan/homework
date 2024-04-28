#!/usr/bin/python3

import os
import glob
import shutil

def extentions():
    ext = {
        "jpg": "images",
        "png": "images",
        "svg": "images",
        "sql": "sql",
        "exe": "programs",
        "pdf": "pdf",
        "xlsx": "excel",
        "rar": "archive",
        "zip": "archive",
        "docx": "word",
        "txt": "text",
        "pptx": "powerpoint",
        "mp3": "audio",
        "mp4": "video",
        "json": "json",
        "js": "web",
        "css": "web",
    }
    return ext

def sorting_file_by_type(ext):
    path = ""
    for extention, folder_name in ext.items():
        files = glob.glob(os.path.join(path,f"*.{extention}"))
        print(f"[*] found {len(files)} with extension {extention}.")
    if not os.path.isdir(os.path.join(path,folder_name)):
        os.mkdir(os.path.join(path,folder_name))
        print(f"[+] created folder {folder_name}.")
    for file in files:
        basname = os.path.basename(file)
        dst = os.path.join(path,folder_name,basname)
        print(f"[*] file transferred {file} to {dst}")
        shutil.move(file, dst)