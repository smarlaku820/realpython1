import os
from PyPDF2 import PdfFileReader

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
with open (os.path.join(base_path, "Pride and Prejudice.pdf"), "rb") as file_handle:
    pdf_file_handle = PdfFileReader(file_handle)
    print("Number of Pages", pdf_file_handle.getNumPages())
    print("Title:", pdf_file_handle.getDocumentInfo().title)
    print(pdf_file_handle.getPage(147).extractText())