import os, sys

folder_path = f"./data/courses/{sys.argv[1]}"
pdf_files = [f for f in os.listdir(folder_path) if f.lower()]
