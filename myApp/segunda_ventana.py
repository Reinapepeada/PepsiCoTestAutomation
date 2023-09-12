import tkinter as tk
import subprocess

def ejecutar_comando_con_ruta(ruta, comando):
    resultado_text = tk.StringVar()
    try:
        subprocess.run(comando, cwd=ruta, shell=True, check=True)
        resultado_text.set("Comando ejecutado correctamente")
    except subprocess.CalledProcessError as e:
        resultado_text.set(f"Error: {e}")
class SegundaVentana:
    def __init__(self, ventana_principal, ubicacion):
        self.ventana = tk.Toplevel(ventana_principal)
        self.ubicacion = ubicacion
        self.ventana.title(f"Detalles de {ubicacion}")

        self.etiqueta = tk.Label(self.ventana, text=f"Detalles de la planta en {ubicacion}")
        boton_ruta1 = tk.Button(self.ventana, text="Ruta 1", command=lambda: ejecutar_comando_con_ruta(f"c:/Users/09384038/Documents/GitHub/PepsiCoTestAutomation/{self.ubicacion}/flujo 5 equipment Status",'pytest'))
        boton_ruta1.pack()


    def mostrar(self):
        self.ventana.mainloop()
