import datetime
import os
import tkinter as tk
from tkinter import ttk, Entry


import datetime
import os
import tkinter as tk
from tkinter import ttk, Entry

class ScheduledTestInterface:
    hora_objetivo = datetime.datetime.now()+datetime.timedelta(minutes=60)  # Class attribute to store the target time

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Scheduled Test Monitor")
        self.ventana.geometry("400x350")

        self.label_title = ttk.Label(self.ventana, text="Scheduled Test Monitor")
        self.label_title.pack(pady=10)

        self.label_hora_actual = ttk.Label(self.ventana, text="")
        self.label_hora_actual.pack()

        self.label_hora_objetivo = ttk.Label(self.ventana, text="")
        self.label_hora_objetivo.pack()

        self.label_tiempo_restante = ttk.Label(self.ventana, text="")
        self.label_tiempo_restante.pack()

        self.boton_ejecutar = ttk.Button(
            self.ventana, text="Ejecutar Pruebas Ahora", command=self.ejecutar_pruebas_ahora
        )
        self.boton_ejecutar.pack(pady=10)

        self.mensaje_estado = tk.StringVar()
        self.mensaje_estado.set("Esperando para ejecutar los comandos...")
        self.label_estado = ttk.Label(self.ventana, textvariable=self.mensaje_estado)
        self.label_estado.pack(pady=10)

        self.entry_nueva_hora = Entry(self.ventana)
        self.entry_nueva_hora.pack(pady=10)

        self.boton_cambiar_hora = ttk.Button(
            self.ventana, text="Cambiar Hora Objetivo", command=self.actualizar_hora_objetivo
        )
        self.boton_cambiar_hora.pack(pady=5)

        self.verificar_hora()  # Start the time verification process

    def ejecutar_Comandos_Ruta(self):
        plantas = ["Saltillo", "Vallejo", "Mexicali", "Funza", "Cerrillos", "Guadalajara", "7Lagoas"]

        for planta in plantas:
            try:
                os.chdir(f"C:/Users/09384038/Desktop/proyect/PepsiCoTestAutomation/flujos_prueba/{planta}/flujo N Recetas")
                resultado = os.system("pytest")
                if resultado == 0:
                    self.mensaje_estado.set("Comandos ejecutados correctamente.")
                else:
                    self.mensaje_estado.set("Error al ejecutar los comandos.")
            except Exception as e:
                self.mensaje_estado.set(f"Error: {str(e)}")

        os.system("pause")

    def actualizar_hora_objetivo(self):
        nueva_hora_str = self.entry_nueva_hora.get()
        try:
            nueva_hora = datetime.datetime.strptime(nueva_hora_str, "%H:%M:%S")
            ahora = datetime.datetime.now()
            hora_objetivo_nueva = datetime.datetime(ahora.year, ahora.month, ahora.day, nueva_hora.hour, nueva_hora.minute, nueva_hora.second)

            if ahora >= hora_objetivo_nueva:
                hora_objetivo_nueva += datetime.timedelta(days=1)

            tiempo_restante = hora_objetivo_nueva - ahora

            if hora_objetivo_nueva != self.hora_objetivo:
                self.hora_objetivo = hora_objetivo_nueva

            self.actualizar_interfaz(ahora, self.hora_objetivo, tiempo_restante)
            self.ventana.after(1000, lambda: self.verificar_hora())
        except ValueError:
            self.mensaje_estado.set("Error: Formato de hora incorrecto. Utilice HH:MM:SS")

    def verificar_hora(self):
        ahora = datetime.datetime.now()
        tiempo_restante = self.hora_objetivo - ahora

        if tiempo_restante.total_seconds() <= 0:
            self.ejecutar_Comandos_Ruta()
            self.mensaje_estado.set("Comandos ejecutados automáticamente.")
            tiempo_restante = datetime.timedelta(seconds=60)

        self.actualizar_interfaz(ahora, self.hora_objetivo, tiempo_restante)
        self.ventana.after(1000, lambda: self.verificar_hora())

    def ejecutar_pruebas_ahora(self):
        self.ejecutar_Comandos_Ruta()
        self.mensaje_estado.set("Comandos ejecutados manualmente.")

    def actualizar_interfaz(self, ahora, hora_objetivo, tiempo_restante):
        self.label_hora_actual.config(text=f'Hora actual: {ahora.strftime("%H:%M:%S")}')
        self.label_hora_objetivo.config(
            text=f'Hora objetivo: {hora_objetivo.strftime("%H:%M:%S")}'
        )

        horas, rem = divmod(tiempo_restante.seconds, 3600)
        minutos, segundos = divmod(rem, 60)

        self.label_tiempo_restante.config(text=f"Tiempo restante: {horas}:{minutos}:{segundos} segundos")

    def start(self):
        self.ventana.mainloop()

scheduled_test_interface = ScheduledTestInterface()
scheduled_test_interface.start()



