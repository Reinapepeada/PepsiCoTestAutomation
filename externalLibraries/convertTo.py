from docx import Document
import time
from docxtpl import DocxTemplate, InlineImage
import os
import win32com.client
from docxtpl import DocxTemplate, InlineImage


def obtener_nombre_archivo_actual():
    documentName=os.path.basename(__file__) if "__file__" in globals() else None
    documentName=documentName.replace(".py","")
    documentName=documentName.replace("_"," ")
    documentName=documentName.upper()
    documentName=documentName.replace("TEST","TEST ")
    documentName=documentName.replace("TC","TC ")
    return documentName

def createWord(data,documentName,failTubes,goodTubes):

    #tomando el nombre del documento
    
    
    # Create a new document from template
    templateDoc=DocxTemplate("documentation/template2.docx")
    #variable que guarda la fecha
    fecha=time.strftime("%d/%m/%Y")
    #variable que guarda la hora
    hora=time.strftime("%H:%M:%S")
    #variable que guarda el nombre del test
    test="Test : "+documentName

    dataFormateada=""
    for i in range(len(data)):
        for j in range(len(data[i])):
            dataFormateada+='\t'+data[i][j]+"\t"
            
        dataFormateada+="\n-----------------------------------------------------------------------------------------------------------------\n"

    data=dataFormateada
    
    # Create a context for rendering
    context = {
        'fecha': fecha,
        'hora': hora,
        'test': test,
        'data': data,
        'failTubes': failTubes,
        'goodTubes': goodTubes,
        'totalTubes': failTubes+goodTubes
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
    try:
        doc = word.Documents.Open(inputFile)
        doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
        doc.Close()
        print("Conversión completada con éxito.")
    except Exception as e:
        print("Error al convertir el documento:", e)
    finally:
        word.Quit()