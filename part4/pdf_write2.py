import os
from PyPDF2 import PdfFileReader, PdfFileWriter

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
with open(os.path.join(base_path, "Pride and Prejudice.pdf"), "rb") as ifh, \
    open(os.path.join(base_path, "portion.pdf"), "wb") as ofh:
    pdf_ifh = PdfFileReader(ifh)
    pdf_ofh = PdfFileWriter()
    for page_num in range(1, 4):
        pdf_ofh.addPage(pdf_ifh.getPage(page_num))
    pdf_ofh.write(ofh)