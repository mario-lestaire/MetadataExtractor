#!/usr/bin/env python3

import sys
import os
from PyPDF2 import PdfFileReader
from PIL import Image
from PIL.ExifTags import TAGS
from prettytable import PrettyTable


def is_readable_string(s):
    """Determina si un string es legible o no."""
    try:
        s.encode('utf-8').decode('utf-8', 'strict')
        return True
    except:
        return False


def extract_image_metadata(filename):
    try:
        image = Image.open(filename)
        exif_data = image._getexif()
        if exif_data is None:
            print("No se encontraron metadatos EXIF en la imagen.")
            return None
    except Exception as e:
        print(f"Error al extraer metadatos EXIF: {e}")
        return None

    # Convertir los códigos de etiquetas en nombres legibles y filtrar aquellos que no se pueden decodificar correctamente
    readable_exif = {}
    for tag, value in exif_data.items():
        tag_label = TAGS.get(tag, tag)
        if isinstance(value, (str, int, float, list, tuple)):
            if isinstance(value, str) and not is_readable_string(value):
                continue
            readable_exif[tag_label] = value

    return readable_exif


def extract_pdf_metadata(filename):
    try:
        pdf = PdfFileReader(open(filename, "rb"))
        metadata = pdf.getDocumentInfo()
        return {k[1:]: v for k, v in metadata.items()}  # quita el primer carácter ("/") de cada clave
    except Exception as e:
        print(f"Error al extraer metadatos del PDF: {e}")
        return None


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"El archivo '{filename}' no existe.")
        sys.exit(1)

    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp')):
        metadata = extract_image_metadata(filename)
        title = "Metadatos de Imagen"
    elif filename.lower().endswith('.pdf'):
        metadata = extract_pdf_metadata(filename)
        title = "Metadatos de PDF"
    else:
        print("Formato de archivo no reconocido.")
        sys.exit(1)

    table = PrettyTable()
    table.title = title
    table.field_names = ["Clave", "Valor"]

    if metadata:
        for k, v in metadata.items():
            table.add_row([k, v])
        print(table)
    else:
        print("No se encontraron metadatos!")


if __name__ == "__main__":
    main()
