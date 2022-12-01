from tkinter import*
import random

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

#-----------------------------
#frame de graficacion
#-----------------------------
frame_graficacion= Frame(ventana_principal)
frame_graficacion.config(bg= "white", width=520, height=520)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creacion canva
c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)


ventana_principal.mainloop()