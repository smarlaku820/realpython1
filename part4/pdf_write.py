import os
from PyPDF2 import PdfFileReader

base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp11/practice_files"
with open(os.path.join(base_path, "Pride and Prejudice.pdf"), "rb") as ifh, \
        open(os.path.join(base_path, "Pride and Prejudice.txt"), "w") as ofh:
    pdf_fh = PdfFileReader(ifh)
    title = pdf_fh.getDocumentInfo().title
    total_pages = pdf_fh.getNumPages()
    ofh.write(title+"\n")
    ofh.write("Number of pages: {}\n\n".format(total_pages))
    for page_num in range(0, total_pages):
        text = pdf_fh.getPage(page_num).extractText()
        text = text.replace("  ", "\n")
        ofh.write(text)