import PyPDF2 # type: ignore
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import threading
import os

# Establece la ruta de guardado
ruta_guardado = r'C:\Users\ebarros\Documents\PDF\PDF_SEPARADOS'
ruta_pdf = r'C:\Users\ebarros\Documents\PDF\archivo.pdf'

# # Verifica si la carpeta existe, de lo contrario la crea
# if not os.path.exists(ruta_guardado):
#     os.makedirs(ruta_guardado)

def iniciar_separcion():
    thread = threading.Thread(target=separar_pdf)
    thread.start()

def separar_pdf():
    archivo = entry.get()
    directorio = entry_directorio.get()
    
    pdf = PyPDF2.PdfReader(archivo)
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
            nombre_archivo = f"{directorio}/{cliente}.pdf"
        else:
            nombre_archivo = f"{directorio}/Pagina_{i+1}.pdf"
        
        consola.insert(tk.END, nombre_archivo + " se llama el nuevo archivo creado...\n")
        consola.see(tk.END)  # Scroll hasta el final
        
        # Verifica si el archivo existe
        if os.path.exists(nombre_archivo):
            print(f"El archivo {nombre_archivo} ya existe.")

        # Verifica si la ruta es correcta
        if not os.path.isdir(os.path.dirname(nombre_archivo)):
            print(f"La ruta {os.path.dirname(nombre_archivo)} no es válida.")

        # Intenta crear el directorio si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
        # Guarda el archivo PDF
        with open(nombre_archivo, 'wb') as output:
            writer.write(output)

    entry.delete(0, tk.END)
    entry_directorio.delete(0, tk.END)
    finalizar_proceso()

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    entry_directorio.delete(0, tk.END)
    entry_directorio.insert(0, directorio)

def finalizar_proceso():
    # Código a ejecutar al finalizar el proceso
    messagebox.showinfo("Proceso finalizado", "El proceso ha terminado")

root = tk.Tk()
root.title("Separador de PDF")

entry = tk.Entry(root, width=50)
entry.pack()

boton = tk.Button(root, text="Seleccionar archivo", command=lambda: [entry.delete(0, tk.END), entry.insert(0, filedialog.askopenfilename())])
boton.pack()

label_directorio = tk.Label(root, text="Directorio de guardado:")
label_directorio.pack()

entry_directorio = tk.Entry(root, width=50)
entry_directorio.pack()

boton_directorio = tk.Button(root, text="Seleccionar directorio", command=seleccionar_directorio)
boton_directorio.pack()

consola = scrolledtext.ScrolledText(root, width=100, height=20)
consola.pack()

boton_separar = tk.Button(root, text="Separar PDF", command=iniciar_separcion)
boton_separar.pack()

root.mainloop()