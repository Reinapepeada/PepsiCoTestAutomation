import tkinter as tk
from views.segunda_ventana import SegundaVentana


class VentanaPrincipal:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Plantas en MES")
        self.ventana_principal.geometry("400x400")
        self.ventana_principal.resizable(False, False)
        self.ventana_principal.protocol("WM_DELETE_WINDOW", self.ventana_principal.destroy)
        self.ventana_principal.grab_set()
        self.etiqueta = tk.Label(self.ventana_principal, text="Selecciona una planta para ver sus flujos de prueba")
        self.etiqueta.pack(pady=10)

    def abrir_segunda_ventana(self, ubicacion):
        segunda_ventana = SegundaVentana(self.ventana_principal, ubicacion)
        segunda_ventana.mostrar()

    def iniciar(self):
        ubicaciones = ["Vallejo", "Mexicali", "Guadalajara", "Saltillo", "Cerrillos", "Funza"]
        max_width = max(len(ubicacion) for ubicacion in ubicaciones) + 2  # Calculate the maximum width of the buttons

        for ubicacion in ubicaciones:
            boton_ubicacion = tk.Button(self.ventana_principal, text=ubicacion, width=max_width,
                                        command=lambda ubicacion=ubicacion: self.abrir_segunda_ventana(ubicacion))
            boton_ubicacion.pack(anchor='center')  # Center the button

        self.ventana_principal.mainloop()
