"""
Generador de arte ASCII 
Convierte imágenes a arte ASCII usando mapeo de brillo a caracteres.
Caracteres utilizados:●♠♦+♥♣★♫ 
"""
import sys 
print(sys.version)

from PIL import Image, ImageFilter,ImageDraw, ImageFont
#Python libreria Pillow, es como el photoshop en python
#permite manipular imagenes

import tkinter as tk
#piezas de tipo lego para construir ventanas, interfaces graficas

from tkinter import filedialog
#explorar archivos en laptop, seleccionar carpetas etc

import tkinter.ttk as ttk
#widges mas bonitos, es version mas moderna

def version_final(ruta_imagen, ancho=180):
#abrimos imagen y convertimos a escala de grises
    imagen = Image.open(ruta_imagen).convert("L")
#Aplicar filtro de enfoque para acentuar bordes
    imagen = imagen.filter(ImageFilter.SHARPEN)
#size 1= alto original, size0= ancho original
    proporcion = imagen.size[1] / imagen.size[0]
#creamos nuevo alto
    alto = int(ancho * proporcion)
#redimensionamos imagen, lanczos para que no se vea pixeleado
    imagen = imagen.resize((ancho, alto), Image.LANCZOS)
#carga pixeles para poder leer la imagen, sin esto
#no pudiesemos acceder a x,y
    pixeles = imagen.load()

# creamos la paleta a utilizar 
    mi_paleta = "●♠♦+♥♣★♫ "  
    
#creamos lista vacia
    lineas = []
    
#recorremso cada fila
    for y in range(alto):
        linea = []
        for x in range(ancho):
            #brillo numero entre 0 (negro puro) y 255(blanco puro)
            brillo = pixeles[x, y]
            if brillo < 15:    
                linea.append(mi_paleta[0])  
            elif brillo < 40:
                linea.append(mi_paleta[1])  
            elif brillo < 70: 
                linea.append(mi_paleta[2])  
            elif brillo < 100: 
                linea.append(mi_paleta[3])  
            elif brillo < 140:   
                linea.append(mi_paleta[4]) 
            elif brillo <180: 
                linea.append(mi_paleta[5]) 
            elif brillo<220:
                linea.append(mi_paleta[7]) 
            else:                
                linea.append(mi_paleta[8]) #espacio
#une todos los caracteres haciendo que esten pegados/unidos
        lineas.append(''.join(linea))
    
    return lineas

#creacion de interfaz
def interfaz_simple():
    #creamos ventana vacia
    ventana = tk.Tk()
    ventana.title("MI CONVERSOR ASCII-by Georgett Vásquez")
    #le damos tamaño especifico 
    ventana.geometry("1000x700")
    ventana.config(bg='#cca9dd')
   
    frame_bienvenida = tk.Frame(ventana, bg='#FFE4E1')  # Fondo rosita
    frame_bienvenida.pack(fill=tk.X, pady=10)
    
    label_bienvenida= tk.Label(frame_bienvenida,
                              text="BIENVENIDO/A A MI CONVERSOR ASCII, ESPERO TE GUSTE",
                              font=("Comic Sans MS", 18, "bold"),
                              fg="#FF1493",
                              bg="#FFE4E1", 
                              pady=20)
    label_bienvenida.pack()
    
    label_subtitulo= tk.Label(frame_bienvenida,
                              text="Convierte tus imagenes en arte con caracteres ●♦♠♥♣*★♫",
                              font=("Arial", 12),
                              fg="#8B008B",  # Dark Magenta
                              bg="#FFE4E1")
    label_subtitulo.pack(pady=5)
    
    def cargar_imagen():
        #buscamos nuestro archivo
        ruta = filedialog.askopenfilename(
            #titulo de la ventana siguiente
            title="Selecciona una imagen",
            #filtramos para que muestre archivos de imagen
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if not ruta:
            return
        
        # convierte imagen a ascii
        lineas = version_final(ruta, 150) 
        
        # Mostrar resultado
        texto.config(state=tk.NORMAL)
        texto.delete(1.0, tk.END)
        
        #escribe el ascii line apor linea
        for linea in lineas:
            texto.insert(tk.END, linea + '\n')
            
        #para que el usuario no pueda modificar resultado
        texto.config(state=tk.DISABLED)
    
    # Botón simple
    btn = tk.Button(ventana, text="CARGA TU IMAGEN", 
                   command=cargar_imagen, bg="blue", fg="white",
                   font=("Arial", 14))
    btn.pack(pady=20)
    
    #funcion para guardar el ascii en formto txt
    def guardar_texto_ascii():
        try:
            contenido = texto.get(1.0, tk.END)  
            archivo = filedialog.asksaveasfilename(
                title="Guardar arte ASCII",
                defaultextension=".txt",
                filetypes=[("Archivos de texto", "*.txt")]
            )
            if archivo:
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                print(f"Guardado en: {archivo}")
        except Exception as e:
            print(f" Error al guardar: {e}")
    
    #funcion para formato imagen
    def guardar_como_imagen():
        try:
            texto_ascii = texto.get(1.0, tk.END).strip()
            if not texto_ascii:
                print("No hay arte ASCII para guardar")
                return
            lineas = texto_ascii.split('\n')
            
            # CONFIGURACIÓN QUE IMITA EXACTAMENTE EL CONVERSOR
            font_size = 6    # Más pequeño para mejor precisión
            char_width = 4   # Ancho de carácter en píxeles
            char_height = 8  # Alto de carácter en píxeles
            
            # Dimensiones basadas en el texto real
            max_ancho_chars = max(len(linea) for linea in lineas)
            ancho_imagen = max_ancho_chars * char_width
            alto_imagen = len(lineas) * char_height
            
            # Crear imagen
            img = Image.new('RGB', (ancho_imagen, alto_imagen), color='black')
            draw = ImageDraw.Draw(img)
            
            # Fuente monoespaciada obligatoria
            try:
                # Forzar Courier o similar
                font = ImageFont.truetype("cour.ttf", font_size)
            except:
                try:
                    font = ImageFont.truetype("consola.ttf", font_size)
                except:
                    # Crear fuente básica monoespaciada
                    font = ImageFont.load_default()
            
            # Dibujar CARÁCTER POR CARÁCTER para control exacto
            for y, linea in enumerate(lineas):
                for x, char in enumerate(linea):
                    x_pos = x * char_width
                    y_pos = y * char_height
                    draw.text((x_pos, y_pos), char, fill='white', font=font)
            
            archivo = filedialog.asksaveasfilename(
                title="Guardar imagen PNG exacta",
                defaultextension=".png",
                filetypes=[("PNG", "*.png")]
            )
            
            if archivo:
                img.save(archivo, 'PNG')
                print(f"Imagen  guardada: {archivo}")
        except Exception as e:
            print(f" Error: {e}")
        
    # Área de texto
    texto = tk.Text(ventana, font=("Courier", 4), wrap=tk.NONE,
                   bg="black", fg="white")
    texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # FRAME para botones es como un cajon donde se colocan
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=15)
    
    # BOTÓN GUARDAR TEXTO
    btn_guardar_texto = tk.Button(frame_botones, text="GUARDAR EN TXT", 
                                 command=guardar_texto_ascii, bg="purple", fg="white",
                                 font=("Arial", 12), width=18)
    btn_guardar_texto.pack(side=tk.LEFT, padx=5)
    
    # BOTÓN GUARDAR IMAGEN
    btn_guardar_imagen = tk.Button(frame_botones, text="GUARDAR EN PNG", 
                                  command=guardar_como_imagen, bg="#E75480", fg="white",
                                  font=("Arial", 12), width=18)
    btn_guardar_imagen.pack(side=tk.LEFT, padx=5)
    
    ventana.mainloop()
    #mantiene ventana abierta para interactuar con el usuario

#funciona tipo si quiero reutilizar funciones en otro archivo 
#no se ejecuta todo el codigo
if __name__ == "__main__":
    interfaz_simple()