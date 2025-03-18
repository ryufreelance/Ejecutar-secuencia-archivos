import os
import time

def abrir_archivos_en_carpeta(carpeta):
    # Iterar sobre los archivos en la carpeta dada
    for archivo in os.listdir(carpeta):
        # Construir la ruta completa al archivo
        ruta_archivo = os.path.join(carpeta, archivo)
        
        # Verificar si es un archivo
        if os.path.isfile(ruta_archivo):
            try:
                # Abrir el archivo con la aplicación predeterminada
                os.startfile(ruta_archivo)
                print(f"Abriendo archivo: {ruta_archivo}")
                time.sleep(5)  # Añadir un retraso de 5 segundos
            except Exception as e:
                print(f"No se pudo abrir el archivo {ruta_archivo}: {e}")

# Ejemplo de uso:
carpeta = r'C:\Users\TuUsuario\Carpeta'
abrir_archivos_en_carpeta(carpeta)
