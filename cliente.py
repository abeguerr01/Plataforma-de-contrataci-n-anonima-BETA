#Codigo para CEEI GUADLAJARA
#Centro: IES NEWTON-SALAS (Villanueva de la Torre)
#Miembros: Alejandro Beguer, Daniel Rivas, Gabriel Palomo, Manuel Cañas

import tkinter as tk
import json

# - FUNCIONES - #

def borrar():
    input_DNI.delete(0, tk.END)
    input_nombre.delete(0, tk.END)
    input_apellido1.delete(0, tk.END)
    input_apellido2.delete(0, tk.END)
    input_nSS.delete(0, tk.END)
    input_fn.delete(0, tk.END)
    input_dicap.delete(0, tk.END)
    input_tit.delete(0, tk.END)
    input_habilidades.delete(0, tk.END)

    etiqueta_cnt.config(text="Formulario borrado")
    etiqueta_cnt.config(fg="red")


def done():
    dni = input_DNI.get()
    input_DNI.delete(0, tk.END)
    nombre = input_nombre.get()
    input_nombre.delete(0, tk.END)
    apellido1 = input_apellido1.get()
    input_apellido1.delete(0, tk.END)
    apellido2 = input_apellido2.get()
    input_apellido2.delete(0, tk.END)
    ss = input_nSS.get()
    input_nSS.delete(0, tk.END)
    fn = input_fn.get()
    input_fn.delete(0, tk.END)
    disc = input_dicap.get()
    input_dicap.delete(0, tk.END)
    titulos = input_tit.get()
    input_tit.delete(0, tk.END)
    habilidades = input_habilidades.get()
    input_habilidades.delete(0, tk.END)

    etiqueta_cnt.config(text="Formulario enviado")
    etiqueta_cnt.config(fg="green")

    nomcrip = nombre[0] + apellido1[0] + apellido2[0]
    CVzip ={
        'CURRICULUM':{
            'Usuario':nomcrip,
            'DNI':dni,
            'Titularidad':titulos,
            'Habilidades':habilidades
        }
    }
    datos_json = json.dumps(CVzip, indent=4)
    with open(f"CVs/CVzip/{nomcrip}_{dni}-zip.json", "w") as archivozip:
        archivozip.write(datos_json)

    CVcom ={
        'CURRICULUM COMPLETO':{
            'Usuario':nomcrip,
            'Nombre completo':nombre+' '+apellido1+' '+apellido2,
            'DNI':dni,
            'Numero seguridad social':ss,
            'Fecha de nacimiento':fn,
            'Discapacidad':disc,
            'Titularidad':titulos,
            'Habilidades':habilidades
        }
    }
    datos_json = json.dumps(CVcom, indent=4)
    with open(f"CVs/CVcom/{nomcrip}_{dni}-com.json", "w") as archivocom:
        archivocom.write(datos_json)

    print (CVzip)
    print (CVcom)
    print ('\n\n REGISTRADO CORRECTAMENTE')


# - CONFIGURACIÓN DE APP - #

app = tk.Tk()
app.geometry("600x450")
app.configure(background='#71bcdf')
tk.Wm.wm_title(app,'Demo')

main = tk.Frame(app)
main.pack()


# - CONTENIDO DE LA APP - #

Titulo_frame = tk.Frame(app)
etiqueta_Titulo = tk.Label(Titulo_frame, text="TITULO")
etiqueta_Titulo.pack(pady=10)
Titulo_frame.pack(pady=10)

# DNI
dni_frame = tk.Frame(app)
etiqueta_dni = tk.Label(dni_frame, text="Ingrese su DNI o NIE:")
etiqueta_dni.pack(side="left")
input_DNI = tk.Entry(dni_frame)
input_DNI.pack(side="left")
dni_frame.pack(pady=5)

# Nombre
nombre_frame = tk.Frame(app)
etiqueta_nom = tk.Label(nombre_frame, text="Ingrese su nombre:")
etiqueta_nom.pack(side="left")
input_nombre = tk.Entry(nombre_frame)
input_nombre.pack(side="left")
nombre_frame.pack(pady=5)

# Apellidos
apellido1_frame = tk.Frame(app)
etiqueta_ap1 = tk.Label(apellido1_frame, text="Ingrese su primer apellido:")
etiqueta_ap1.pack(side="left")
input_apellido1 = tk.Entry(apellido1_frame)
input_apellido1.pack(side="left")
apellido1_frame.pack(pady=5)

apellido2_frame = tk.Frame(app)
etiqueta_ap2 = tk.Label(apellido2_frame, text="Ingrese su segundo apellido:")
etiqueta_ap2.pack(side="left")
input_apellido2 = tk.Entry(apellido2_frame)
input_apellido2.pack(side="left")
apellido2_frame.pack(pady=5)

# Seguridad social
ss_frame = tk.Frame(app)
etiqueta_ss = tk.Label(ss_frame, text="Ingrese su número de la seguridad social:")
etiqueta_ss.pack(side="left")
input_nSS = tk.Entry(ss_frame)
input_nSS.pack(side="left")
ss_frame.pack(pady=5)

# Fecha nacimiento
fn_frame = tk.Frame(app)
etiqueta_fn = tk.Label(fn_frame, text="Ingrese su fecha de nacimiento (DD-MM-AAAA):")
etiqueta_fn.pack(side="left")
input_fn = tk.Entry(fn_frame)
input_fn.pack(side="left")
fn_frame.pack(pady=5)

# Descripción
dicap_frame = tk.Frame(app)
etiqueta_dicap = tk.Label(dicap_frame, text="Diganos su discapacidad:")
etiqueta_dicap.pack(side="left")
input_dicap = tk.Entry(dicap_frame)
input_dicap.pack(side="left")
dicap_frame.pack(pady=5)

tit_frame = tk.Frame(app)
etiqueta_tit = tk.Label(tit_frame, text="Diganos su titularidad:")
etiqueta_tit.pack(side="left")
input_tit = tk.Entry(tit_frame)
input_tit.pack(side="left")
tit_frame.pack(pady=5)

hab_frame = tk.Frame(app)
etiqueta_habilidades = tk.Label(hab_frame, text="Diganos sus habilidades:")
etiqueta_habilidades.pack(side="left")
input_habilidades = tk.Entry(hab_frame)
input_habilidades.pack(side="left")
hab_frame.pack(pady=5)

cnt_frame = tk.Frame(app)
etiqueta_cnt = tk.Label(cnt_frame, text="")
etiqueta_cnt.pack()
cnt_frame.pack(pady=10)

#Botones
botones_frame = tk.Frame(app)
enviar = tk.Button(app, text="Enviar", command=done)
enviar.pack()
bor = tk.Button(app, text="Borrar", command=borrar)
bor.pack()
botones_frame.pack()

app.mainloop()