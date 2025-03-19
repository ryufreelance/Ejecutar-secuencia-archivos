# Ejecutar-secuencia-archivos

Este proyecto contiene un script de Python que permite abrir automáticamente todos los archivos de una carpeta específica utilizando las aplicaciones predeterminadas del sistema operativo. Es ideal para procesar lotes de archivos o realizar análisis rápidos.

---

## Características

- **Automatización**: Abre todos los archivos en la carpeta especificada de forma automática.
- **Control de retraso**: Introduce un retraso de 5 segundos entre la apertura de cada archivo para evitar la sobrecarga del sistema.
- **Gestión de errores**: Muestra mensajes en caso de que un archivo no pueda ser abierto.

---

## Requisitos Previos

- **Python 3.6** o superior.
- Sistema operativo **Windows** (el script utiliza `os.startfile`, que es específico de Windows).

---

## Instalación

Sigue estos pasos para usar el script:

1. Clona este repositorio o descarga el archivo del script.
2. Asegúrate de tener Python instalado. Puedes verificar la instalación con el comando:

   ```bash
   python --version
3. Abre el archivo script.py en tu editor de texto o IDE favorito.

---

## Uso

1. Crea una carpeta donde ubicaras los archivos que deseas procesar.
2. Configura la variable carpeta en el script con la ruta de la carpeta que deseas procesar. Por ejemplo:

    ```python
    carpeta = r'C:\Users\TuUsuario\Carpeta'
2. Ejecuta el script desde tu terminal o entorno de desarrollo integrado (IDE):

    ```bash
    python script.py
3. El script abrirá cada archivo en la carpeta utilizando las aplicaciones predeterminadas del sistema operativo. Habrá un retraso de 5 segundos entre la apertura de cada archivo, este retraso puedes modificarlo segun la necesidad en la variable `time.sleep(5)`.