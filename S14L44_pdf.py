import PyPDF2
import os
os.chdir(r'C:\Users\benne\OneDrive\Documents\GitHub\Automate_the_boring_stuff')

# Open a reader on pdf file
with open('meetingminutes1.pdf', 'rb') as pdfFile:
    reader = PyPDF2.PdfFileReader(pdfFile)
    # Print the number of pages
    print(reader.numPages)
    # Access a certain page
    page = reader.getPage(0)
    # Print the text from a page
    print(page.extractText())
    # Loop through all pages and print text
    for pageNum in range(reader.numPages):
        print(reader.getPage(pageNum).extractText())

with open('meetingminutes1.pdf', 'rb') as pdf1File,\
        open('meetingminutes2.pdf', 'rb') as pdf2File,\
        open('combinedminutes.pdf', 'wb') as outputFile:
    reader1 = PyPDF2.PdfFileReader(pdf1File)
    reader2 = PyPDF2.PdfFileReader(pdf2File)
    writer = PyPDF2.PdfFileWriter()
    for pageNum in range(reader1.numPages):
        page = reader1.getPage(pageNum)
        writer.addPage(page)
    print('reader1 complete')
    for pageNum in range(reader2.numPages):
        page2 = reader2.getPage(pageNum)
        writer.addPage(page2)
    print('reader2 complete')
    writer.write(outputFile)

