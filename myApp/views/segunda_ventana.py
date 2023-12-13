import tkinter as tk
import subprocess
import os
from views.vista_carpetas import ReportFoldersWindow

def ejecutar_comando_con_ruta(ruta, comando):
    resultado_text = tk.StringVar()
    try:
        subprocess.run(comando, cwd=ruta, shell=True, check=True)
        resultado_text.set("Comando ejecutado correctamente")
    except subprocess.CalledProcessError as e:
        resultado_text.set(f"Error: {e}")

class SegundaVentana:
    def __init__(self, ventana_principal, ubicacion):
        flujos=[["KPIS principales", "flujo_1_optimalRangesKpisDashboardPackaging"],['Downtime less8hours', 'flujo_2_dowtimes-8hoursExpired'],["% Waste-Unknowbags", 'flujo_3_%waste-unknowBags%'],["Equipment Status", "flujo_5_equipmentStatus"],["Adopcion de Recetas", "flujo N Recetas"],["Dashboard vs SRSS", "flujo_6_DashboardvsSRSS"],["Totalwast - CHW- OverUnder", "flujo_8_totalWaste-Chwaste-overUnder"],["Downtimes AU-TE-NE", "flujo_9_downtimesAU-TE-NE"],["kpisByOperator", "flujo_10_KpisByOperator"],["CHW-MHW", "flujo_11_CHW-MHW"],["TotalBags-Goodbags", "flujo_12_TotalBags-GoodBags"],["UnderOverWeight", "flujo_13_UnderOverWeight"],["x", "flujo_14_"],["x", "flujo_15_"]]
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.protocol("WM_DELETE_WINDOW", self.ventana.destroy)
        self.ventana.resizable(False, False)
        self.ventana.grab_set()
        self.ubicacion = ubicacion
        self.ventana.title(f"Detalles de {ubicacion}")
        self.ventana.geometry("400x450")
        self.etiqueta = tk.Label(self.ventana, text=f"Detalles de la planta en {ubicacion}")
        self.etiqueta.pack()
        self.etiqueta = tk.Label(self.ventana, text="Selecciona un flujo de prueba para ejecutarlo")
        self.etiqueta.pack(pady=10)
        
        button_frame = tk.Frame(self.ventana)  # Create a frame to hold the buttons
        
        for flujo in range(len(flujos)-1):
            boton_ruta = tk.Button(button_frame, text=flujos[flujo][0], command=lambda flujo=flujos[flujo]: ejecutar_comando_con_ruta(f"C:/Users/09384038/Desktop/proyect/PepsiCoTestAutomation/flujos_prueba/{self.ubicacion}/{flujo[1]}", 'pytest'))
            boton_ruta.grid(row=flujo, column=0, pady=0, sticky="nsew")        

        button_frame.pack()  # Pack the frame to add it to the window

        boton_carpetas = tk.Button(self.ventana, text="Reportes por Flujo", command=lambda: self.abrir_ventana_report_folders(flujos))
        boton_carpetas.configure(
            background="#4CAF50",  # Background color (you can change this)
            foreground="white",    # Text color
            font=("Arial", 12),    # Font settings
            width=20,              # Button width
            height=2,              # Button height
            borderwidth=3,         # Border width
        )
        boton_carpetas.pack(pady=10) 
    
    def abrir_ventana_report_folders(self,flujos):
        report_folders_window = ReportFoldersWindow(self.ventana, self.ubicacion, flujos)
        report_folders_window.mostrar()

    def mostrar(self):
        self.ventana.mainloop()


