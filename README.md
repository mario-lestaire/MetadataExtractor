# MetadataExtractor

**MetadataExtractor** es una herramienta de _pentesting_ diseñada para extraer metadatos de imágenes en formatos como `.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp` y archivos PDF.

## 📋 Requisitos

- **Python 3**
- Bibliotecas:
  - PyPDF2
  - PIL (Pillow)
  - prettytable

### Instalación de bibliotecas:

pip install PyPDF2 Pillow prettytable

markdown
Copy code

## 🚀 Uso

Para usar **MetadataExtractor**, ejecuta el script `metadata_extractor.py` desde la línea de comandos, pasando el archivo del que deseas extraer metadatos:

python metadata_extractor.py <ruta_del_archivo>

shell
Copy code

### Ejemplo:

python metadata_extractor.py datosDePrueba/Cat_November_2010-1a.jpg

markdown
Copy code

## ⚙️ Funcionalidad

La herramienta identificará automáticamente si el archivo es una imagen o un archivo PDF y extraerá los metadatos correspondientes. Luego, los metadatos extraídos se mostrarán en una tabla en la terminal.

### 📸 Metadatos de imágenes

Para las imágenes, **MetadataExtractor** recopila metadatos EXIF utilizando la biblioteca PIL.

### 📄 Metadatos de PDF

Para los archivos PDF, la herramienta recopila metadatos del documento, como título, autor, y otros datos relacionados, utilizando la biblioteca PyPDF2.

## 🧪 Datos de prueba

Puedes encontrar ejemplos de archivos en formato `.jpg` y `.pdf` dentro de la carpeta `datosDePrueba` para probar la funcionalidad del script.

