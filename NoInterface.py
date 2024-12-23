import PyPDF2 # type: ignore
import tkinter as tk
from tkinter import filedialog
import re
import os

# Establece la ruta de guardado
ruta_guardado = r'C:\Users\ebarros\Documents\PDF\PDF_SEPARADOS2'
ruta_pdf = r'C:\Users\ebarros\Documents\PDF\archivo.pdf'

# # Verifica si la carpeta existe, de lo contrario la crea
if not os.path.exists(ruta_guardado):
    os.makedirs(ruta_guardado)

with open(ruta_pdf, 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    for i, page in enumerate(pdf.pages):
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
            
        # Extrae el texto de la página
        texto_pagina = page.extract_text()
            
        lineas = texto_pagina.split('\n')
                
        # Selecciona la línea que deseas utilizar como título
        titulo = lineas[2]  
                
        if titulo:
            cliente = titulo.split("(")[1].replace(" ", "")[:-1]
            nombre_archivo = f"{ruta_guardado}/{cliente}.pdf"
        else:
            nombre_archivo = f"{ruta_guardado}/Pagina_{i+1}.pdf"
            
        # Guarda el archivo PDF
        with open(nombre_archivo, 'wb') as output:
            writer.write(output)