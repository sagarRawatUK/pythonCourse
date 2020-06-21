import sys
import PyPDF2

#storing the input arguements in a list
inputs = sys.argv[1:]

#creating a merger function
def pdf_combiner(pdf_list):

    #creating a merger object
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    #writing the merged pdfs into a super pdf
    merger.write('super.pdf')

pdf_combiner(inputs)
