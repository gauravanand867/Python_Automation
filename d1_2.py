from PyPDF2 import PdfFileWriter, PdfFileReader

"""
pluspdf=PdfFileWriter()
pdflist=["//home//gaurav//Documents//SG18318//SG18318_summer_training.pdf", "//home//gaurav//Documents//SG18318//UML_SG18318.pdf"]

for i in pdflist:
	eachpdf=PdfFileReader(i)
	nopage=eachpdf.getNumPages()
	print(nopage)						#Print No of Pages in each pdf
	for i in range(nopage):
		p=eachpdf.getPage(i)
		pluspdf.addPage(p)
pluspdf.encrypt('pdf121','owner121',True)			#To lock PDF
save_pdf=open("//home//gaurav//Documents//SG18318//both.pdf",'wb')
pluspdf.write(save_pdf)	"""

watermark=PdfFileReader("//home//gaurav//Documents//SG18318//SG18318_summer_training.pdf")
pdf=PdfFileReader("//home//gaurav//Documents//SG18318//UML_SG18318.pdf")
w_watermark=watermark.getPage(0)
newpdf=PdfFileWriter()
page=pdf.getNumPages()
for i in range(page):
	pages=pdf.getPage(i)
	pages.mergePage(w_watermark)
	newpdf.addPage(pages)

final=open("//home//gaurav//Documents//SG18318//watermark.pdf",'wb')
newpdf.write(final)
final.close()