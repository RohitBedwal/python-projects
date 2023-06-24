from pypdf import PdfWriter

read=PdfWriter()
for x in ["15.pdf","45.pdf"]:#here  write the path of pdf you want to merge 
  read.append(x)

read.write("")#wrint name of pdf you want to give to it
read.close()