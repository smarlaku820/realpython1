import os
import copy
from PyPDF2 import PdfFileWriter, PdfFileReader

# Rotating the Pages in clock-wise direction
base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
with open(os.path.join(base_path, "ugly.pdf"), "rb") as input_file_handler,\
        open(os.path.join(base_path, "Neat Ugly.pdf"), "wb") as output_file_handler:
    pdf_ifh = PdfFileReader(input_file_handler)
    pdf_ofh = PdfFileWriter()
    for page_num in range(0, pdf_ifh.getNumPages()):
        page = pdf_ifh.getPage(page_num)
        if page_num % 2 == 0:
            page.rotateClockwise(90)
        pdf_ofh.addPage(page)
    pdf_ofh.write(output_file_handler)

# Understanding the Page Dimensions
with open(os.path.join(base_path, "half and half.pdf"), "rb") as input_file_handler:
    pdf_ifh = PdfFileReader(input_file_handler)
    page = pdf_ifh.getPage(0)
    #print(page.mediaBox.lowerLeft)
    #print(page.mediaBox.lowerRight)
    #print(page.mediaBox.upperLeft)
    #print(page.mediaBox.upperRight)

# Now crop the pages and save it to a new PDF file
with open(os.path.join(base_path, "half and half.pdf"), "rb") as input_file_handler, \
        open(os.path.join(base_path, "The Little Mermaid.pdf"), "wb") as output_file_handler:
    pdf_ifh = PdfFileReader(input_file_handler)
    pdf_ofh = PdfFileWriter()
    for page_num in range(pdf_ifh.getNumPages()):
        page = pdf_ifh.getPage(page_num)
        page_left = copy.copy(page)
        page_right = copy.copy(page)
        page_left.mediaBox.lowerRight = (page.mediaBox.lowerRight[0]/2, 0)
        page_right.mediaBox.lowerLeft = (page.mediaBox.lowerRight[0]/2, 0)
        pdf_ofh.addPage(page_left)
        pdf_ofh.addPage(page_right)
    pdf_ofh.write(output_file_handler)