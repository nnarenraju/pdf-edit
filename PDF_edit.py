#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
PDF_edit.py
    Convert, stitch and delete from PDF files

Created on Mon Aug 05 09:23:28 2019

__author__      = nnarenraju
__copyright__   = Copyright 2019, PDF Edit
__credits__     = nnarenraju
__license__     = Apache License 2.0
__version__     = 1.0.1
__maintainer__  = nnarenraju
__email__       = nnarenraju@gmail.com
__status__      = inUsage

"""

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from PIL import Image

def jpg2pdf(filenames=[], outputfile=r"image.pdf"):
    """ Covert JPG to PDF """
    for filename in filenames:
        image = Image.open(r'{}'.format(filename))
        img = image.convert('RGB')
        img.save(outputfile)

def stitch_pdfs(filenames=[], outputfile="stitched.pdf"):
    """ Concatenate PDF files together """
    merger = PdfFileMerger()
    # Append all required files together
    # files is a list of strings: "filename.pdf"
    for file in filenames:
        merger.append(file)
    
    # Writing onto new file
    merger.write(outputfile)
    # Close file
    merger.close()

def fine_stitch_pdfs(file_and_page=[("", "")], outputfile="fine_stitched.pdf"):
    """ Fine stitch specific pages from PDF files """
    # Merge certain selected pages 
    merger = PdfFileMerger()
    # Read pages
    for file, page in file_and_page:
        merger.merge(page, file)
    
    # Writing onto new file
    merger.write(outputfile)
    # Close file
    merger.close()

def delete_pages(filename, delete_pages=[], outputfile='cleaned.pdf'):
    """ Deletes pages from a PDF document """
    # page numbering starts from 0
    # Sanity check
    if delete_pages == []:
        raise ValueError("Page numbers not provided!")
    # Read PDF file
    infile = PdfFileReader('{}.pdf'.format(filename), 'rb')
    output = PdfFileWriter()
    
    # Put pages not in delete_pages into new PDF file
    for i in range(infile.getNumPages()):
        if i not in delete_pages:
            p = infile.getPage(i)
            output.addPage(p)
    
    # Write new PDF file with removed pages
    with open(outputfile, 'wb') as f:
        output.write(f)

if __name__ == "__main__":
    
    pass
    
    
    
    
    










        