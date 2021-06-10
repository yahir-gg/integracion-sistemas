from zeep import Client
import tkinter as tk
import xml.etree.cElementTree as ET
# Empieza interfaz
raiz = tk.Tk()
raiz.title("Cliente")
# raiz.geometry("650x350")
miFrame=tk.Frame()
miFrame.pack()
miFrame.config(width="650", heigh="350")

frame_add_pd=tk.Frame()
frame_add_pd.pack()
frame_add_pd.config(width="650",heigh="350")


def save_data(c_nombre,c_marca,c_desc,c_precio):
    cliente = Client('http://localhost:8000/?wsdl')
    puno = c_nombre.get()
    pdos = c_marca.get()
    ptres = c_desc.get()
    pcuatro = c_precio.get()
    res = cliente.service.addPd(puno,pdos,ptres,pcuatro)
    print('Return:',res)

    #cliente.service.say_hello('audifonos',1)
    """root = ET.Element("root")
    producto = ET.SubElement(root, "producto")
    nombre = ET.SubElement(producto, "nombre", name="nodo")
    nombre.text = puno
    ET.SubElement(producto, "marca", atributo="algo").text = pdos
    arbol = ET.ElementTree(root)
    arbol.write("./prueba.xml")"""


def ingresar_producto():
    l_nombre=tk.Label(miFrame,text="Nombre del producto")
    l_nombre.grid(row=0,column=0,padx=10,pady=10)
    c_nombre = tk.Entry(miFrame)
    c_nombre.grid(row=0,column=1,padx=10,pady=10)

    l_marca= tk.Label(miFrame,text="Marca")
    l_marca.grid(row=1,column=0,padx=10,pady=10)
    c_marca = tk.Entry(miFrame)
    c_marca.grid(row=1,column=1,padx=10,pady=10)
    
    l_desc=tk.Label(miFrame,text="Descripcion")
    l_desc.grid(row=2,column=0,padx=10,pady=10)
    c_desc = tk.Entry(miFrame)
    c_desc.grid(row=2,column=1,padx=10,pady=10)
    
    l_precio=tk.Label(miFrame,text="Precio del producto")
    l_precio.grid(row=3,column=0,padx=10,pady=10)
    c_precio = tk.Entry(miFrame)
    c_precio.grid(row=3,column=1,padx=10,pady=10)
    
    botonenvio = tk.Button(raiz,text="Enviar",command=lambda:save_data(c_nombre,c_marca,c_desc,c_precio))
    botonenvio.pack()

botonaddPd = tk.Button(raiz,text="Aadir producto",command=ingresar_producto)
botonaddPd.pack()



    





tk.mainloop()
# Termina interfaz

