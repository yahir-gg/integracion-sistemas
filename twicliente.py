from zeep import Client
import tkinter as tk
import xml.etree.cElementTree as ET

# Empieza interfaz
raiz = tk.Tk()
raiz.title("Cliente")
raiz.geometry("400x300")
miFrame=tk.Frame()
#miFrame.pack()
miFrame.config(width="350", heigh="350")

# Anadir producto
def save_data(c_nombre,c_marca,c_desc,c_precio):
    vdos = tk.Toplevel()
    vdos.config(width="350",heigh="350")
    cliente = Client('http://localhost:8000/?wsdl')
    puno = c_nombre.get()
    pdos = c_marca.get()    
    ptres = c_desc.get()
    pcuatro = c_precio.get()
    res = cliente.service.addPd(puno,pdos,ptres,pcuatro)
    l_nombre=tk.Label(vdos,text=res)
    l_nombre.grid(row=0,column=0,padx=10,pady=10)
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
    vdos = tk.Toplevel()
    vdos.config(width="350",heigh="350")
    l_nombre=tk.Label(vdos,text="Nombre del producto")
    l_nombre.grid(row=0,column=0,padx=10,pady=10)
    c_nombre = tk.Entry(vdos)
    c_nombre.grid(row=0,column=1,padx=10,pady=10)

    l_marca= tk.Label(vdos,text="Marca")
    l_marca.grid(row=1,column=0,padx=10,pady=10)
    c_marca = tk.Entry(vdos)
    c_marca.grid(row=1,column=1,padx=10,pady=10)
    
    l_desc=tk.Label(vdos,text="Descripcion")
    l_desc.grid(row=2,column=0,padx=10,pady=10)
    c_desc = tk.Entry(vdos)
    c_desc.grid(row=2,column=1,padx=10,pady=10)
    
    l_precio=tk.Label(vdos,text="Precio del producto")
    l_precio.grid(row=3,column=0,padx=10,pady=10)
    c_precio = tk.Entry(vdos)
    c_precio.grid(row=3,column=1,padx=10,pady=10)
    
    botonenvio = tk.Button(vdos,text="Enviar",command=lambda:save_data(c_nombre,c_marca,c_desc,c_precio))
    botonenvio.grid(row=4,column=0,padx=10,pady=10)
# consultar producto
def send_id(id_to_send):
    vdos = tk.Toplevel()
    vdos.config(width="350",heigh="350")
    cliente = Client('http://localhost:8000/?wsdl')
    puno = id_to_send.get()
    res = cliente.service.consultar_pd(puno)
    l_n = tk.Label(vdos,text="Producto: "+res[0])
    l_n.grid(row=1,column=0,padx=10,pady=2)
    l_m = tk.Label(vdos,text="Marca: "+res[1])
    l_m.grid(row=2,column=0,padx=10,pady=2)
    l_d = tk.Label(vdos,text="Descripcion: "+res[2])
    l_d.grid(row=3,column=0,padx=10,pady=2)
    l_p = tk.Label(vdos,text="Precio: "+res[3])
    l_p.grid(row=4,column=0,padx=10,pady=2)
    print('Return:',res[0])


def consultar_producto():
    vdos = tk.Toplevel()
    vdos.config(width="350",heigh="350")
    l_id = tk.Label(vdos,text="Ingrese el ID del producto a consultar")
    l_id.grid(row=0,column=0,padx=10,pady=10)
    c_id = tk.Entry(vdos)
    c_id.grid(row=0,column=1,padx=10,pady=10)
    botonenvio = tk.Button(vdos,text="Enviar consulta",command=lambda:send_id(c_id))
    botonenvio.grid(row=1,column=0,padx=10,pady=10)

# eliminar producto
def save_delete(c_ID):
    vdos = tk.Toplevel()
    vdos.config(width="350",heigh="350")
    cliente = Client('http://localhost:8000/?wsdl')
    uno = c_ID.get()
    res = cliente.service.deletePd(uno)
    l_ID = tk.Label(vdos, text= res)
    l_ID.grid(row=0,column=0,padx=10,pady=10)
    print('Return:',res)

def ingresaID():
    vdos = tk.Toplevel()
    vdos.config(width="350",heigh="350")
    l_ID = tk.Label(vdos, text= "Ingrese ID del producto")
    l_ID.grid(row=0,column=0,padx=10,pady=10)
    c_ID = tk.Entry(vdos)
    c_ID.grid(row=0,column=1,padx=10,pady=10)
    botonenvia = tk.Button(vdos,text="Enviar elimina",command=lambda:save_delete(c_ID))
    botonenvia.grid(row=1,column=0,padx=10,pady=10)

botonaddPd = tk.Button(raiz,text="Aadir producto",height = 3, width = 20,command=ingresar_producto)
botonaddPd.grid(row=0,column=0,padx=10,pady=10)

boton_consulta = tk.Button(raiz,text="Consultar producto",height = 3, width = 20,command=consultar_producto)
boton_consulta.grid(row=0,column=1,padx=10,pady=10)

botondeletePd = tk.Button(raiz,text="Eliminar producto",height = 3, width = 20,command=ingresaID)
botondeletePd.grid(row=1,column=0,padx=10,pady=10)

botondeletePd = tk.Button(raiz,text="Actualizar producto",height = 3, width = 20,command=ingresaID)
botondeletePd.grid(row=1,column=1,padx=10,pady=10)
tk.mainloop()
# Termina interfaz

