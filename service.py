from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, String, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json


class EKYCService(ServiceBase):
    @rpc(String, String, _returns=Unicode)
    def getFaceEmbeddings(ctx, nid, imageString):
        return "[1,2,3]"
    @rpc(String, _returns=Unicode)
    def parseNid(ctx, imageString):
        return json.dumps( {
                    "nid": 199212345672,
                    "dob": "01-10-1990",
                    "name": "Hasan Mahmud",
                    "bengali_name": "হাসান মাহমুদ",
                    "fathers_name": "কাজি  আমানুল্লাহ  মিয়া ",
                    "mothers_name": "আখতার বানু",
                    "error": None}).encode('utf8')
    @rpc(String, String, _returns=Unicode)
    def verifyNidInfo(ctx, info):
        return "verified"


application = Application([EKYCService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()