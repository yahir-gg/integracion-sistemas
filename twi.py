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



class HelloWorldService(ServiceBase):
    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(name, times):
        for i in range(times):
            yield 'Hello, %s' % name

    @srpc(Unicode, Unicode,Unicode, Unicode, _returns= Unicode)
    def addPd(nombre_pm,marca_pm,desc_pm,precio_pm):
        tree = ET.parse('productos.xml')
        root = tree.getroot()
        producto = ET.SubElement(root, "producto")
        ET.SubElement(producto, "nombre").text = nombre_pm
        ET.SubElement(producto, "marca").text = marca_pm
        ET.SubElement(producto, "descripcion").text = desc_pm
        ET.SubElement(producto, "precio").text = precio_pm
        ET.ElementTree(root)
        tree.write("./productos.xml")
        msj = "Producto ingresado"
        return nombre_pm


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