from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

import docx
import os
from docxtpl import DocxTemplate

def crear_tabla_template(template_file, nombre_archivo, datos):
    doc = DocxTemplate(template_file)

    # Definir los datos para la tabla (una lista de listas)
    context = {
        'tabla': datos[1:]  # Excluir la primera fila, que contiene los encabezados
    }

    # Renderizar los datos en el marcador de posición
    doc.render(context)

    # Guardar el documento en un archivo
    doc.save(nombre_archivo)

if __name__ == "__main__":
    # Datos para la tabla (una lista de listas)
    datos_tabla = [
        ["Nombre", "Edad", "Ciudad"],
        ["Juan", "25", "Madrid"],
        ["María", "30", "Barcelona"],
        ["Pedro", "22", "Valencia"]
    ]

    # Archivo de plantilla de Word con el marcador de posición
    template_file = "template.docx"

    # Nombre del archivo de salida
    archivo_salida = "tabla_ejemplo.docx"

    # Crear la tabla en el documento de Word utilizando la plantilla
    crear_tabla_template(template_file, archivo_salida, datos_tabla)

    print(f"Tabla creada en el archivo '{archivo_salida}'")