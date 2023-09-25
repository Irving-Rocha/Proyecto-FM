"Programa de obtención de datos RGB de una imagen"
"Autor: Irving David Rocha Gaona" 
from PIL import Image
import pickle
import openpyxl

# En esta sección leeremos la imagen a analizar
image = Image.open("1EBT2 0cGy -1.bmp")
 
# En esta sección obtendremos las dimensiones de la imagen
width, height = image.size

# En esta sección obtendremos los valores RGB de cada pixel
pixels = []
position = []
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        pixel=pixel+(x,y)
        pixels.append(pixel)

# En esta sección crearemos un archivo de excel 
wb = openpyxl.Workbook()
hoja = wb.active


#En esta sección agregaremos los datos RGB a varias celdas a la vez
for i in range(len(pixels)):
    hoja.append(pixels[i])

#Esta sección guardaremos el archivo de Excel
wb.save('Datos 1EBT2 0cGy -1.xlsx')

  
#Por último en esta sección imprimiremos los datos obtenidos 
print(pixels)






