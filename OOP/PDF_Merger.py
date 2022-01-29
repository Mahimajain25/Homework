import os
from PyPDF2 import PdfFileMerger

def PDFmerger():
    source_dir = os.getcwd()
    #source_dir = input("Enter the Path")
    merger = PdfFileMerger()

    for item in os.listdir(source_dir):
        if item.endswith('pdf'):
            merger.append(item)
    merger.write('./final_PDFMerge.pdf')
    merger.close()





