from twisted.web.server import Site, GzipEncoderFactory
from twisted.web.resource import Resource, EncodingResourceWrapper
from twisted.internet import reactor
from src.daak import log
from src.daak import restTest
from src.daak import urlMap

class Daak(Resource):

    isLeaf = True
    def render_GET(self, request):
        path = request.uri[2:];
        return urlMap[path]()#"<html>Hello, world!</html>"

    def render_POST(self, request):
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["the-field"][0]),)



def run(port):
    resourceDaak = Daak()
    wrappedDaak = EncodingResourceWrapper(resourceDaak, [GzipEncoderFactory()])
    site = Site(wrappedDaak)
    reactor.listenTCP(port, site)
    log.msg("daak server run listen to port '" + str(port) + "'." )
    reactor.run()






run(5000)