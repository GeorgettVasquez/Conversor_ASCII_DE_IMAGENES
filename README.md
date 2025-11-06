# Generador de Arte ASCII

Este proyecto convierte imágenes en **arte ASCII** usando caracteres especiales como:  
`● ♠ ♦ + ♥ ♣ ★ ♫`  
El programa también permite **guardar el resultado** como texto o como imagen, y cuenta con una **interfaz gráfica** fácil de usar.

## 🛠 Tecnologías y librerías utilizadas

- Python 3.11.1
- [Pillow](https://python-pillow.org/) – manipulación de imágenes
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – interfaz gráfica
- Librerías estándar de Python `tkinter.filedialog` para poder abrir tus archivos

##  Funcionalidades

1. **Convertir imágenes a ASCII**  
   - Convierte cualquier imagen seleccionada a caracteres ASCII mapeando el brillo de cada píxel.
   - Puedes ajustar el ancho de la imagen ASCII para mejor resolución.

2. **Guardar resultado**  
   - Como archivo de texto (`.txt`) con los caracteres ASCII.
   - Como imagen (`.png`) que mantiene el formato del ASCII visualmente.

3. **Interfaz gráfica (GUI)**  
   - Ventana interactiva con botones para cargar imágenes y guardar resultados.
   - Área de previsualización del arte ASCII.
