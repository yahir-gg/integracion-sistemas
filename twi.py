import logging
logging.basicConfig(level=logging.DEBUG)
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.primitive import Integer
from spyne.model.primitive import Unicode
from spyne.model.complex import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.twisted import TwistedWebResource
from twisted.internet import reactor
from twisted.web.server import Site
import xml.etree.cElementTree as ET
from lxml import etree
from StringIO import StringIO 
 
dtd = etree.DTD(StringIO("""
<!ELEMENT abarrotes (producto*)>
<!ELEMENT producto (nombre, marca, descripcion,precio)>
<!ATTLIST producto id CDATA #REQUIRED>
<!ELEMENT nombre (#PCDATA)>
<!ELEMENT marca (#PCDATA)>
<!ELEMENT descripcion (#PCDATA)>
<!ELEMENT precio (#PCDATA)>
""")) 

def validar_xml(archivo_xml_temp):
    mytree = etree.parse(archivo_xml_temp)
    determinante = dtd.validate(mytree)
    return determinante

class HelloWorldService(ServiceBase):
    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(name, times):
        for i in range(times):
            yield 'Hello, %s' % name

    @srpc(Unicode, Unicode,Unicode, Unicode, _returns= Unicode)
    def addPd(nombre_pm,marca_pm,desc_pm,precio_pm):
        parametros=[]
        parametros.append(nombre_pm)
        parametros.append(marca_pm)
        parametros.append(desc_pm)
        parametros.append(precio_pm)
        tree = ET.parse('productos.xml')
        root = tree.getroot()
        id_new_nodo = len(root.getchildren())+1
        producto = ET.SubElement(root, "producto",id=str(id_new_nodo))
        ET.SubElement(producto, "nombre").text = nombre_pm
        ET.SubElement(producto, "marca").text = marca_pm
        ET.SubElement(producto, "descripcion").text = desc_pm
        ET.SubElement(producto, "precio").text = precio_pm
        ET.ElementTree(root)
        tree.write("./productos_tmp.xml")
        nameF = "productos_tmp.xml"
        validacion = validar_xml(nameF)
        evalido = bool
        for e in parametros:
            if e=="":
                evalido = False
                break
            else:
                evalido = True


        if validacion == True and evalido == True:
            tree.write("./productos.xml")
            msj = "Archivo XML valido. El producto ha sido agregado"
            return msj
        else:
            msj = "Archivo XML invalido. No se agrego el producto"
            return msj

    @srpc(Unicode, _returns= Iterable(Unicode))
    def consultar_pd(id_consultar):
        tree = ET.parse('productos.xml')
        root = tree.getroot()
        pen = root.find(".//producto[@id='"+id_consultar+"']")
        hijos = pen.getchildren()
        xml_lt=[]
        xml_str=""
        for e in hijos:
              xml_lt.append(e.text)
        
        for e in xml_lt:
            xml_str=xml_str+e+"\n"

        return xml_lt[0],xml_lt[1],xml_lt[2],xml_lt[3]

    @srpc(Unicode, _returns = Unicode)
    def deletePd(id_pt):
        tree = ET.parse('productos.xml')
        root = tree.getroot()
        #producto = ET.SubElement(root, "producto")
        for producto in root.findall('producto'):
            idP = producto.attrib['id']
            if idP == id_pt:
                root.remove(producto)
        tree.write("./productos.xml")
        return "Producto eliminado"

application = Application([HelloWorldService],
                          tns='spyne.examples.hello',
                          in_protocol=Soap11(),
                          out_protocol=Soap11()
                          )

if __name__ == '__main__':
    resource = TwistedWebResource(application)
    site = Site(resource)
    reactor.listenTCP(8000, site, interface='0.0.0.0')
    reactor.run()