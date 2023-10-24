# MetadataExtractor

MetadataExtractor es una herramienta de pentesting diseñada para extraer metadatos de imágenes y archivos PDF. Utiliza la biblioteca PyPDF2 para los archivos PDF y la biblioteca PIL para las imágenes.

Requisitos
Python 3
Bibliotecas:
PyPDF2
PIL (Pillow)
prettytable
Para instalar las bibliotecas necesarias, puedes usar pip:

Copy code
pip install PyPDF2 Pillow prettytable
Uso
Para utilizar MetadataExtractor, simplemente invoca el script desde la línea de comandos, pasando el archivo del que deseas extraer metadatos:

php
Copy code
python metadata_extractor.py <filename>
Por ejemplo:

Copy code
python metadata_extractor.py datosDePrueba/Cat_November_2010-1a.jpg
Funcionalidad
La herramienta identificará automáticamente si el archivo es una imagen (soporta formatos como .jpg, .jpeg, .png, .tiff, y .bmp) o un archivo PDF. Luego, extraerá los metadatos y los mostrará en una tabla legible en la terminal.

Metadatos de imágenes
MetadataExtractor recopila metadatos EXIF de imágenes utilizando la biblioteca PIL.

Metadatos de PDF
Para los archivos PDF, la herramienta recopila metadatos del documento, como título, autor, y otros datos relacionados.

Datos de prueba
En la carpeta datosDePrueba encontrarás ejemplos en formato .jpg y .pdf que puedes utilizar para probar el script.
