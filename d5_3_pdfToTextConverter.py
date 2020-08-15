from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter, HTMLConverter, XMLConverter
from pdfminer.layout import LAParams
import io

pdf=open('//home//gaurav//Documents//Coding//Alien Brains//Python_Automation//warmup_shedule.pdf','rb')

mem=io.StringIO()
lp=LAParams()
rm=PDFResourceManager()
cnv=TextConverter(rm,mem,laparams=lp)
ip=PDFPageInterpreter(rm,cnv)

for i in PDFPage.get_pages(pdf):
	ip.process_page(i)
	text=mem.getvalue()
file=open('//home//gaurav//Documents//Coding//Alien Brains//Python_Automation//pdf.txt','wb')
file.write(text.encode('utf-8'))