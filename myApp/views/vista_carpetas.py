
import tkinter as tk
import os
import subprocess

class ReportFoldersWindow:
    def __init__(self, ventana_principal, ubicacion, flujos):
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.protocol("WM_DELETE_WINDOW", self.ventana.destroy)
        self.ubicacion = ubicacion
        self.ventana.title(f"Report Folders for {ubicacion}")
        self.ventana.geometry("400x450")
        self.etiqueta = tk.Label(self.ventana, text=f"Report Folders for the plant at {ubicacion}")
        self.etiqueta.pack(pady=10)

        # Create buttons to navigate to report folders for each test flow
        for i in flujos:
            folder_name = i[1]
            button = tk.Button(self.ventana, text=f"📂 Test Flow {i[0]}", command=lambda folder=folder_name: self.open_report_folder(folder))
            button.pack()

    def open_report_folder(self, folder_name):
        # Construct the folder path using an f-string
        folder_path = f"C:/Users/09384038/Desktop/proyect/PepsiCoTestAutomation/flujos_prueba/{self.ubicacion}/{folder_name}/reportOutput"
        print(f"Opening folder at {folder_path}")
        try:
            # Open the folder using the default file explorer
            os.startfile(folder_path)
        except Exception as e:
            print(f"An error occurred while opening the folder: {e}")

    def mostrar(self):
        self.ventana.mainloop()