from tkinter import*
import random

# Funciones de la app
def crear():
    MATRIZ = []

    for i in range(matriz.get):
        MATRIZ.append([])
        for j in range(matriz.get):
            MATRIZ[i].append(random.randint(1,9))

    # Mostrar matriz
    for k in range(matriz.get):
        # Creació de los rectangulos
        rectangulo=c.create_rectangle(60,10,BASE/2-10, ALTURA,  fill="pink", outline="green")
        for j in range(matriz.get):
            print(MATRIZ[k][j], end = "\t")

# proporciciones de la ventana 
BASE =  500
ALTURA = 500

#---------------------------
#Ventana principal
#---------------------------
ventana_principal = Tk()
ventana_principal.title("Buscar número en matriz")
ventana_principal.resizable(False,False)
ventana_principal.config(bg = "black")

# Variable global de filas y columnas

matriz =StringVar()
 

#-----------------------------
#frame de graficacion
#-----------------------------
frame_graficacion= Frame(ventana_principal)
frame_graficacion.config(bg= "white", width=520, height=520)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creacion canva
c= Canvas(frame_graficacion, width=BASE, height= 348)
c.place(x=10, y=184)

# Frame entrada
frame_entrada = Frame(frame_graficacion)
frame_entrada.config(bg= "black", width=BASE, height=164)
frame_entrada.place(x = 10, y = 10)

# Caja de entrada de texto de tamaño de matriz
tx = Label(frame_entrada, text = "Tamaño matriz")
tx.config(bg = "black", fg = "white", font = ("Arial", 20))
tx.place(x = 20 , y = 5)

# Entrada de creacion matriz
entry_matriz = Entry(frame_entrada)
entry_matriz.config(bg = "White", fg = "black", font = ("Arial",20))
entry_matriz.focus_set()
entry_matriz.place(x = 50, y = 50, width = 120)

#
# Caja de entrada de texto numero a encontrar
tx = Label(frame_entrada, text = "Número a buscar")
tx.config(bg = "black", fg = "white", font = ("Arial", 20))
tx.place(x = 250 , y = 5)

# Entrada de numeroa  buscar
entry_buscar = Entry(frame_entrada)
entry_buscar.config(bg = "White", fg = "black", font = ("Arial",20))
entry_buscar.focus_set()
entry_buscar.place(x = 290, y = 50, width = 120)

#-----------
# Creacion de botones

# Boton para crear la matriz
boton_crear = Button(frame_entrada, text = "Crear" ,font=("Arial", 20), command=crear)
boton_crear.place(x = 50, y = 100, width = 120, height = 30)

# Boton para buscar
boton_buscar = Button(frame_entrada, text = "Buscar" ,font=("Arial", 20))
boton_buscar.place(x = 290, y = 100, width = 120, height = 30)


# Creació de los rectangulos
#rectangulo=c.create_rectangle(60,10,BASE/2-10, ALTURA,  fill="pink", outline="green")


ventana_principal.mainloop()