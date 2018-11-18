import sys
import algo
import csv
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter


def main(pdf,i):
    import getopt
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    outfile = 'pdf'+str(i)
    outtype = 'text'
    imagewriter = None
    rotation = 0
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    fname=pdf

    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug
    PDFDevice.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = file(outfile, 'w')
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                               imagewriter=imagewriter)
    fp = file(fname, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        page.rotate = (page.rotate+rotation) % 360
        interpreter.process_page(page)
    fp.close()
    device.close()
    outfp.close()
    return


if __name__ == '__main__':
    #x=int(input("Enter the number of pdf files to be converted :"))
    #for i in range(x):
    #    pdf=raw_input("\nPlease enter the name of the pdf files : \n")
     #   main(pdf,i+1)
     #   algo.main('pdf'+str(i+1))
    
    x=sys.argv[1:]
    for i in range(len(x)):
        main(x[i],i+1)
        results = algo.main('pdf'+str(i+1))
        
        
        # Results is a List of Lists
        #TODO Convert Results into a CSV for Analysis in Excel
        with open('excel'+str(i+1)+'.csv', 'wb') as myfile:
            fields=['Date','Shop','Money Spent']
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(fields)
            wr.writerows(results)    
            
      


       
            
