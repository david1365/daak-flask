from twisted.web.server import Site, GzipEncoderFactory
from twisted.web.resource import Resource, EncodingResourceWrapper
from twisted.internet import reactor
from twisted.web.static import File

from daak1.daak.daak.logger import loggerDaak
from daak1.daak import urlMap

class ResourceDaak(Resource):

    isLeaf = True
    def render_GET(self, request):
        # path = request.uri[2:];
        # return urlMap[path]()#"<html>Hello, world!</html>"
        loggerDaak.info("get respons->" + request.uri)
        return "<html>Hello, world!</html>"


    def render_POST(self, request):
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["the-field"][0]),)



class Daak(Site):
    def doStart(self):
         Site.doStart(self)
         loggerDaak.info("daak server run.")


def run(port):
    resourceDaak = ResourceDaak()
    wrappedDaak = EncodingResourceWrapper(resourceDaak, [GzipEncoderFactory()])
    site = Daak(wrappedDaak)
    reactor.listenTCP(port, site)
    # log.msg("daak server run listen to port '" + str(port) + "'." )
    reactor.run()






run(5000)