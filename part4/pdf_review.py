import os
from PyPDF2 import PdfFileWriter, PdfFileReader

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"

with open(os.path.join(base_path, "The Whistling Gypsy.pdf"), "rb") as file_handler:
    pdf_file_handler = PdfFileReader(file_handler)
    print(pdf_file_handler.getDocumentInfo().title)
    print(pdf_file_handler.getNumPages())

with open(os.path.join(base_path, "The Whistling Gypsy.pdf"), "rb") as input_fh, \
        open(os.path.join(base_path, "The Whistling Gypsy.txt"), "w", encoding="utf-8") as output_fh:
    pdf_file_handler = PdfFileReader(input_fh)
    total_pages = pdf_file_handler.getNumPages()
    for page in range(0, total_pages):
        text = pdf_file_handler.getPage(page).extractText()
        text = text.replace("  ", "\n")
        output_fh.write(text)

with open(os.path.join(base_path, "The Whistling Gypsy.pdf"), "rb") as input_fh, \
        open(os.path.join(base_path, "The Whistling Gypsy New.pdf"), "wb") as output_fh:
    pdf_file_handler = PdfFileReader(input_fh)
    pdf_outfile_handler = PdfFileWriter()
    total_pages = pdf_file_handler.getNumPages()
    for page in range(1, total_pages):
        pdf_outfile_handler.addPage(pdf_file_handler.getPage(page))
    pdf_outfile_handler.write(output_fh)