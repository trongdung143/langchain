from docx2pdf import convert
import sys

try:
    filepath = f"./data/courses/{sys.argv[1]}"
    convert(filepath)
except ImportError:
    print("docx2pdf is not installed. Please install it using 'pip install docx2pdf'")
except Exception as e:
    print(f"Error: {e}")
