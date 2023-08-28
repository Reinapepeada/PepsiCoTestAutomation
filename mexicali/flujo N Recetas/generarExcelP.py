import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Luis'],
    'Edad': [25, 30, 28, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
}

df = pd.DataFrame(data)

# Especificar el nombre del archivo Excel
nombre_archivo = 'ejemplo_pandas.xlsx'

# Crear un escritor de Excel
writer = pd.ExcelWriter(nombre_archivo, engine='xlsxwriter')

# Convertir el DataFrame en una hoja de Excel
df.to_excel(writer, sheet_name='Hoja1', index=False)

# Obtener el objeto de la hoja de Excel
worksheet = writer.sheets['Hoja1']

# Obtener dimensiones del DataFrame
num_rows, num_cols = df.shape

# Crear un objeto de formato para encabezados de columna
header_format = writer.book.add_format({'bold': True, 'text_wrap': True, 'valign': 'top', 'border': 1})

# Configurar las celdas de encabezado
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

# Configurar el ancho de las columnas basado en la longitud del contenido
for i, col in enumerate(df.columns):
    max_len = max(df[col].astype(str).apply(len).max(), len(col))
    worksheet.set_column(i, i, max_len + 2)

# Guardar el archivo Excel
writer._save()

print(f"Archivo '{nombre_archivo}' creado exitosamente.")
