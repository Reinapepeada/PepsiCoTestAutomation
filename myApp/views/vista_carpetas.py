import tkinter as tk
import os
import subprocess
from tkinter import messagebox

class ReportFoldersWindow:
    def __init__(self, ventana_principal, ubicacion, flujos):
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.protocol("WM_DELETE_WINDOW", self.ventana.destroy)
        self.ubicacion = ubicacion
        self.ventana.title(f"Report Folders for {ubicacion}")
        self.ventana.geometry("400x450")

        # Label for the window
        self.etiqueta = tk.Label(self.ventana, text=f"Report Folders for the plant at {ubicacion}")
        self.etiqueta.pack(pady=10)

        # Label for instruction
        self.etiqueta = tk.Label(self.ventana, text="Select a test flow to open its report folder")
        self.etiqueta.pack(pady=5)

        # Frame for buttons
        button_frame = tk.Frame(self.ventana)

        # Create buttons to navigate to report folders for each test flow
        for flujo in range(len(flujos)):
            folder_name = flujos[flujo][1]
            button = tk.Button(button_frame, text=f"📂 {flujos[flujo][0]}", command=lambda folder=folder_name: self.open_report_folder(folder))
            button.grid(row=flujo, column=0, pady=0, sticky="nsew")

        button_frame.pack()

    def open_report_folder(self, folder_name):
        try:
            # Construct the folder path using an f-string
            folder_path =fr"C:\Users\09384038\Desktop\proyect\PepsiCoTestAutomation\flujos_prueba\{self.ubicacion}\{folder_name}\reportOutput"
            
            # Print the constructed folder path for debugging
            print("Folder Path:", folder_path)

            # Check if the folder exists
            if os.path.exists(folder_path):
                # Open the folder using the default file explorer
                subprocess.Popen(['explorer',folder_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            else:
                messagebox.showinfo("Info", "Folder does not exist.")
        except Exception as e:
            # Display a detailed error message
            messagebox.showerror("Error", f"An error occurred while opening the folder: {e}")

    def mostrar(self):
        self.ventana.mainloop()

