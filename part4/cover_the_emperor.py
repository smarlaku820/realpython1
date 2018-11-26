import os
from PyPDF2 import PdfFileReader, PdfFileWriter

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
out_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files/Output"
with open(os.path.join(base_path, "Emperor cover sheet.pdf"), "rb") as fh1, \
        open(os.path.join(base_path, "The Emperor.pdf"), "rb") as fh2, \
        open(os.path.join(out_path, "The Covered Emperor.pdf"), "wb") as fh3:
    pdf_ifh1 = PdfFileReader(fh1)
    pdf_ifh2 = PdfFileReader(fh2)
    pdf_ofh = PdfFileWriter()
    pdf_ofh.addPage(pdf_ifh1.getPage(0))
    for page_num in range(0, pdf_ifh2.getNumPages()):
        pdf_ofh.addPage(pdf_ifh2.getPage(page_num))
    pdf_ofh.write(fh3)