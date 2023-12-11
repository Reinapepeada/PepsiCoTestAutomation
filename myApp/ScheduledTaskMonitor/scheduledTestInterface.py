import datetime
import os
import tkinter as tk
from tkinter import ttk


def ejecutar_Comandos_Ruta():
    
    #defino las plantas a las que se ejecutará las pruebas
    plantas=["Saltillo","Vallejo","Mexicali","Funza","Cerrillos"]

    #ejecuto los comandos para cada planta
    for planta in plantas:
        try:
            os.chdir(f"C:/Users/09384038/Desktop/proyect/PepsiCoTestAutomation/flujos_prueba/{planta}/flujo N Recetas")
            resultado = os.system("pytest")
            if resultado == 0:
                mensaje_estado.set("Comandos ejecutados correctamente.")
            else:
                mensaje_estado.set("Error al ejecutar los comandos.")
        except Exception as e:
            mensaje_estado.set(f"Error: {str(e)}")

    
    #espera que termine la ejecución de los comandos
    os.system("pause")


def verificar_hora():
    ahora = datetime.datetime.now()
    hora_objetivo = datetime.datetime(ahora.year, ahora.month, ahora.day, 9, 10, 0)

    if ahora >= hora_objetivo:
        hora_objetivo += datetime.timedelta(days=1)

    tiempo_restante = hora_objetivo - ahora
    tiempo_restante_horas = tiempo_restante.total_seconds() // 3600
    minutos, segundos = divmod(tiempo_restante.total_seconds(), 60)

    if tiempo_restante.total_seconds() <= 60:
        ejecutar_Comandos_Ruta()
        mensaje_estado.set("Comandos ejecutados automáticamente.")
        tiempo_restante = datetime.timedelta(seconds=60)

    actualizar_interfaz(ahora, hora_objetivo, tiempo_restante)
    ventana.after(1000, verificar_hora)

def ejecutar_pruebas_ahora():
    ejecutar_Comandos_Ruta()
    mensaje_estado.set("Comandos ejecutados manualmente.")

def actualizar_interfaz(ahora, hora_objetivo, tiempo_restante):
    label_hora_actual.config(text=f'Hora actual: {ahora.strftime("%H:%M:%S")}')
    label_hora_objetivo.config(
        text=f'Hora objetivo: {hora_objetivo.strftime("%H:%M:%S")}'
    )
    
    horas, rem = divmod(tiempo_restante.seconds, 3600)
    minutos, segundos = divmod(rem, 60)

    label_tiempo_restante.config(text=f"Tiempo restante: {horas}:{minutos}:{segundos} segundos")
# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Scheduled Test Monitor")
ventana.geometry("400x300")

label_title = ttk.Label(ventana, text="Scheduled Test Monitor")
label_title.pack(pady=10)

label_hora_actual = ttk.Label(ventana, text="")
label_hora_actual.pack()

label_hora_objetivo = ttk.Label(ventana, text="")
label_hora_objetivo.pack()

label_tiempo_restante = ttk.Label(ventana, text="")
label_tiempo_restante.pack()

# Botón para ejecutar pruebas ahora
boton_ejecutar = ttk.Button(
    ventana, text="Ejecutar Pruebas Ahora", command=ejecutar_pruebas_ahora
)
boton_ejecutar.pack(pady=10)

# Mensaje de estado
mensaje_estado = tk.StringVar()
mensaje_estado.set("Esperando para ejecutar los comandos...")
label_estado = ttk.Label(ventana, textvariable=mensaje_estado)
label_estado.pack(pady=10)

# Iniciar el proceso de verificación de la hora
verificar_hora()

ventana.mainloop()
