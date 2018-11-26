from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

xmargin = 3.2 * inch
ymargin = 6 * inch

d = canvas.Canvas("hello_again.pdf", pagesize=letter)
d.setLineWidth(1)
d.drawString(xmargin, ymargin, "Hello Ishwara from Sai M!")
d.save()
