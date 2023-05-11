from docx import Document
import time
from docxtpl import DocxTemplate, InlineImage
import os
import win32com.client
from docxtpl import DocxTemplate, InlineImage

def createWord(data,documentName):
    # Create a new document from template
    templateDoc=DocxTemplate("documentation/template.docx")
    #variable que guarda la fecha
    fecha=time.strftime("%d/%m/%Y")
    #variable que guarda la hora
    hora=time.strftime("%H:%M:%S")
    #variable que guarda el usuario que hizo la prueba
    usuario="Operador del test : Alejandro "
    #variable que guarda el nombre del test
    test="Test : "+documentName
    
    # Create a context for rendering
    context = {
        'fecha': fecha,
        'hora': hora,
        'usuario': usuario,
        'test': test,
        'data': data
    }
    #render the document
    templateDoc.render(context)
    #save the document
    templateDoc.save("reportPDF/"+documentName+".docx")
    
    return documentName


def convertToPdf(documentName):
    wdFormatPDF = 17

    inputFile = os.path.abspath("reportPDF/"+documentName+".docx")
    outputFile = os.path.abspath("reportPDF/"+documentName+".pdf")
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(inputFile)
    doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()