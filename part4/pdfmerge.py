import os
from PyPDF2 import PdfFileWriter, PdfFileReader

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
with open(os.path.join(base_path, "The Emperor.pdf"), "rb") as input_file_reader, \
        open(os.path.join(base_path, "New Suit.pdf"), "wb") as output_file_reader, \
        open(os.path.join(base_path, "top secret.pdf"), "rb") as watermark_file:
    pdf_ifh = PdfFileReader(input_file_reader)
    pdf_wh = PdfFileReader(watermark_file)
    pdf_ofh = PdfFileWriter()
    for page_num in range(0, pdf_ifh.getNumPages()):
        page = pdf_ifh.getPage(page_num)
        page.mergePage(pdf_wh.getPage(0))
        pdf_ofh.addPage(page)
    pdf_ofh.encrypt("password")
    pdf_ofh.write(output_file_reader)