# import packages


from PyPDF2 import PdfFileReader, PdfFileWriter
import re

## open the pdf file
inputpdf = PdfFileReader(open("2.pdf", "rb"))

## get number of pages
NumPages = inputpdf.getNumPages()

## define keyterms
String = "Pratik3"

## extract text and do the search
for i in range(0, NumPages):
   PageObj = inputpdf.getPage(i)
   #print("this is page " + str(i)) 
   Text = PageObj.extractText() 
   newText = Text.replace("\n", "")
   # print(Text)
   ResSearch = re.search(String, newText)
   if ResSearch:
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)