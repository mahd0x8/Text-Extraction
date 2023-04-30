from ReadDOCX import ExtractData
from pdf2docx import parse

"""
- This code defines a function called ExtractPDFData that takes a filename as input, converts the PDF file to a Word document
using the pdf2docx library, and extracts data from the resulting Word document using the ExtractData function from a separate 
Python module called ReadDOCX.

- The first line of the code imports the ExtractData function from the ReadDOCX module, while the second line imports the 
parse function from the pdf2docx library.

-The ExtractPDFData function takes a filename as input and uses the parse function from pdf2docx to convert the input PDF 
file to a Word document with the same name but with a .docx extension. It then passes the filename of the newly created 
Word document to the ExtractData function from ReadDOCX to extract and process data from the document.
Finally, it returns the dictionary of extracted data.
"""

def ExtractPDFData(filename):
    parse(filename, filename.replace(".pdf",".docx"))
    return ExtractData(filename.replace(".pdf",".docx"),"pdf")