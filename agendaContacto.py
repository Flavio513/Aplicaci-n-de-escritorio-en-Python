from tkinter import * 
from tkinter import messagebox
 
import sqlite3

raiz= Tk()
raiz.title("Agenda de Contactos")
raiz.geometry("500x400")

miMenu= Menu(raiz)
raiz.config(menu=miMenu)

miFrame=Frame(raiz)
miFrame.pack()

#----Funciones Generales----#

def deleteEntries():
    EntryCodigoID.delete(0,'end'),EntryNombre.delete(0,'end'),EntryApellido.delete(0,'end'),EntryDireccion.delete(0,'end'),EntryTelefono.delete(0,'end'),EntryEmail.delete(0,'end'),TextComentarios.delete(1.0,END) 

#----Funciones Menu-------#

def info():
    messagebox.showinfo("Esta es la interfaz de mi Agenda de Contactos","Version 18-08-20")

def aviso():
    messagebox.showinfo("Advertencia"," El mensaje no fue guardado")

def avisoCerrar():
    raiz.destroy()

#------Funciones Botones-----#

def codigoBotonGuardar():
    conexion1=sqlite3.connect("baseContactos")
    miCursor=conexion1.cursor()

    try: 
        miCursor.execute("""
            CREATE TABLE USUARIOS (
                CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                TELEFONO VARCHAR(50),
                EMAIL VARCHAR(50),
                COMENTARIOS VARCHAR(500) )
        """)
    except sqlite3.OperationalError:
        pass
    finally:
        datos=(varNombre.get(),varApellido.get(),varDireccion.get(),varTelefono.get(),varEmail.get(),TextComentarios.get(1.0,END))

        miCursor.execute('INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?,?)',datos)
        deleteEntries()
        conexion1.commit()
        conexion1.close()

def codigoBotonBuscar():
    conexion1=sqlite3.connect("baseContactos")
    miCursor=conexion1.cursor()

    dicDatos = {"CODIGO":EntryCodigoID.get(), "NOMBRE":EntryNombre.get(), "APELLIDO": varApellido.get(), "DIRECCION": varDireccion.get(), "TELEFONO": varTelefono.get(), "EMAIL": varEmail.get()}

    #Print(dicDatos)
    for CAMPOS, VALORES in dicDatos.items():
        if VALORES!='':
            try:
                print(CAMPOS, VALORES)
                miCursor.execute("SELECT * FROM USUARIOS WHERE {}=(?)".format(CAMPOS),(VALORES,))
                verRegistro = miCursor.fetchall()
                varCodigoID.set(verRegistro[0][0])
                varNombre.set(verRegistro[0][1])
                varApellido.set(verRegistro[0][2])
                varDireccion.set(verRegistro[0][3])
                varTelefono.set(verRegistro[0][4])
                varEmail.set(verRegistro[0][5])
                TextComentarios.delete(1.0, END)
                TextComentarios.insert(END, verRegistro[0][6])
                break
            except IndexError:
                deleteEntries()
                break
    conexion1.commit()
    conexion1.close()

def codigoBotonModificar():
    conexion1 = sqlite3.connect("baseContactos")
    miCursor = conexion1.cursor()
    listaDatos = [EntryNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(), varEmail.get(),TextComentarios.get(1.0,END)]
    miCursor.execute("""UPDATE USUARIOS SET NOMBRE = ?, APELLIDO = ?, DIRECCION = ?, TELEFONO = ?, EMAIL = ?, COMENTARIOS = ? WHERE CODIGO={}""".format(EntryCodigoID.get()), listaDatos)
    deleteEntries()

    conexion1.commit()
    conexion1.close()

def codigoBotonEliminar():
    conexion1 = sqlite3.connect("baseContactos")
    miCursor = conexion1.cursor()
    listaDatos = [EntryNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(), varEmail.get(),TextComentarios.get(1.0,END)]
    miCursor.execute("DELETE FROM USUARIOS WHERE CODIGO={}".format(EntryCodigoID.get()))
    deleteEntries()

    conexion1.commit()
    conexion1.close()

def codigoBotonLimpiar():
    deleteEntries()

def codigoBotonoCerrar():
    raiz.destroy()

#-------------------- Row 1 ------------------------
varCodigoID = StringVar()
EntryCodigoID = Entry(miFrame, textvariable = varCodigoID)
EntryCodigoID.grid(row=1, column=1, sticky=W, padx=10, pady=10 )
labelCodigoID = Label(miFrame,text="CODIGO ID:")
labelCodigoID.grid(row=1, column=0, sticky=W)
botonGuardar = Button(miFrame,text="Guardar Registro",command=codigoBotonGuardar,width=15)
botonGuardar.grid(row=1,column=2,sticky=W)

#--------------------Row 2 -------------------------
varNombre = StringVar()
EntryNombre = Entry(miFrame,textvariable=varNombre)
EntryNombre.grid(row=2, column=1, sticky=W, padx=10, pady=10)
labelNombre = Label(miFrame,text="NOMBRE:")
labelNombre.grid(row=2, column=0,sticky=W)
botonBuscar = Button(miFrame,text="Buscar Registro",command=codigoBotonBuscar,width=15)
botonBuscar.grid(row=2,column=2,sticky=W)

#--------------------Row 3 ---------------------------
varApellido = StringVar()
EntryApellido = Entry(miFrame,textvariable=varApellido)
EntryApellido.grid(row=3, column=1, sticky=W, padx=10, pady=10)
labelApellido = Label(miFrame,text="APELLIDO:")
labelApellido.grid(row=3, column=0,sticky=W)
botonModificar = Button(miFrame,text="Modificar Registro",command=codigoBotonModificar,width=15)
botonModificar.grid(row=3,column=2,sticky=W)

#------------------Row 4----------------------------------
varDireccion = StringVar()
EntryDireccion = Entry(miFrame,textvariable=varDireccion)
EntryDireccion.grid(row=4, column=1, sticky=W, padx=10, pady=10)
labelDireccion = Label(miFrame,text="DIRECCIÓN:")
labelDireccion.grid(row=4, column=0,sticky=W)
botonEliminar = Button(miFrame,text="Eliminar Registro",command=codigoBotonEliminar,width=15)
botonEliminar.grid(row=4,column=2,sticky=W)

#-------------------Row 5 -------------------------------
varTelefono = StringVar()
EntryTelefono = Entry(miFrame,textvariable=varTelefono)
EntryTelefono.grid(row=5, column=1, sticky=W, padx=10, pady=10)
labelTelefono = Label(miFrame,text="TELÉFONO:")
labelTelefono.grid(row=5, column=0,sticky=W)
botonLimpiar = Button(miFrame,text="Limpiar Campos",command=codigoBotonLimpiar,width=15)
botonLimpiar.grid(row=5,column=2,sticky=W)

#-----------------------Row 6 --------------------------
varEmail = StringVar()
EntryEmail = Entry(miFrame,textvariable=varEmail)
EntryEmail.grid(row=6, column=1, sticky=W, padx=10, pady=10)
labelEmail = Label(miFrame,text="EMAIL:")
labelEmail.grid(row=6, column=0,sticky=W)
botonCerrar = Button(miFrame,text="Cerrar",command=codigoBotonoCerrar,width=15)
botonCerrar.grid(row=6,column=2,sticky=W)

#-------------------------Row 7 ---------------------------

TextComentarios=Text(miFrame, width=10, height=1)
TextComentarios.grid(column=1, row=7,  padx=10, pady=10, sticky=W,ipadx=30, ipady=60)
labelComentarios=Label(miFrame,text="COMENTARIOS:")
labelComentarios.grid(row=7,column=0,sticky=W)
ScrollbarComentarios = Scrollbar(miFrame,command=TextComentarios.yview)
ScrollbarComentarios.grid(row=7,column=2,sticky=W)


#--------------opciones Menú ------------------------------
miDB=Menu(miMenu, tearoff=0)
miDB.add_command(label="Guardar Registro",command=codigoBotonGuardar)
miDB.add_command(label="Buscar Registro",command=codigoBotonBuscar)
miDB.add_command(label="Cerrar",command=codigoBotonoCerrar)

miEdit=Menu(miMenu,tearoff=0)
miEdit.add_command(label="Modificar Registro",command=codigoBotonModificar)
miEdit.add_command(label="Eliminar Registro",command=codigoBotonEliminar)

miHelp=Menu(miMenu,tearoff=0)
miHelp.add_command(label="About",command=info)

miMenu.add_cascade(label="File",menu=miDB)
miMenu.add_cascade(label="Edit",menu=miEdit)
miMenu.add_cascade(label="Help",menu=miHelp)

raiz.mainloop()
