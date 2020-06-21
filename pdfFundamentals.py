import PyPDF2
 #opening the pdf
with open('dummy.pdf','rb') as file:

    #creating a reader object
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)


    #number of pages
    print(reader.getNumPages())


    #rotating the pdf clockwise or counterclockwise
    page.rotateClockwise(90)
    page.rotateCounterClockwise(90)


    #creating a writer object
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    #writing into a new pdf file
    with open('tilted.pdf','wb') as new_file:
        writer.write(new_file)
