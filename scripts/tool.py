import os

folder_path = "./data/courses/4d17dad2-a34f-46ae-83a7-abb7826d047b"
pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
