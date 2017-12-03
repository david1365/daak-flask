from twisted.web.server import Site, GzipEncoderFactory
from twisted.web.resource import Resource, EncodingResourceWrapper
from twisted.internet import reactor

class Daak(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world!</html>"

    def render_POST(self, request):
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["the-field"][0]),)

resourceDaak = Daak()
wrappedDaak = EncodingResourceWrapper(resourceDaak, [GzipEncoderFactory()])
site = Site(wrappedDaak)
reactor.listenTCP(5000, site)
reactor.run()