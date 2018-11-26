import os
import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
with open(os.path.join(base_path, "Walrus.pdf"), "rb") as input_file_handler, \
        open(os.path.join(base_path, "Walrus Output.pdf"), "wb") as output_file_handler :
    pdf_ifh = PdfFileReader(input_file_handler)
    pdf_ofh = PdfFileWriter()
    pdf_ifh.decrypt("IamtheWalrus")
    print(pdf_ifh.getDocumentInfo().title)
    print(pdf_ifh.getNumPages())
    for page_num in range(0, pdf_ifh.getNumPages()):
        page = pdf_ifh.getPage(page_num)
        page.rotateCounterClockwise(90)
        page_left = copy.copy(page)
        page_right = copy.copy(page)
        page_left.mediaBox.upperRight = (page.mediaBox.upperRight[0]/2, page.mediaBox.upperRight[1])
        page_right.mediaBox.lowerLeft = (page.mediaBox.lowerRight[0]/2, 0)
        pdf_ofh.addPage(page_left)
        pdf_ofh.addPage(page_right)
    pdf_ofh.write(output_file_handler)