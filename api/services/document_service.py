import pandas as pd
from pathlib import Path as path
import fitz
import docx2txt
class extarctor:
    def __init__(self,file):
        self.file_path=path(file)
        self.file_ext=self.file_path.suffix.lower()
    def is_file_extractor_pdf(self):
        if self.file_ext=='.pdf':
            File=fitz.open(str(self.file_path))
            text=""
            for page in File:
                text+=page.get_text()
            File.close()
            return text
    def is_file_extractor_docx(self):
        self.file_path=path(self.file)
        self.file_ext=self.file_path.suffix
        if self.file_ext=='.docx':
            text=docx2txt.process(self.file)
            return text