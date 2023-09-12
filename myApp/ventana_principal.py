import tkinter as tk
from segunda_ventana import SegundaVentana


class VentanaPrincipal:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Plantas en MES")

    def abrir_segunda_ventana(self, ubicacion):
        segunda_ventana = SegundaVentana(self.ventana_principal, ubicacion)
        segunda_ventana.mostrar()

    def iniciar(self):
        ubicaciones = ["Vallejo", "Mexicali", "Guadalajara", "Saltillo", "Cerrillos", "Funza"]
        for ubicacion in ubicaciones:
            boton_ubicacion = tk.Button(self.ventana_principal, text=ubicacion, command=lambda ubicacion=ubicacion: self.abrir_segunda_ventana(ubicacion))
            boton_ubicacion.pack()
        
        self.ventana_principal.mainloop()
