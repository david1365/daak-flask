from twisted.application import internet, service
from twisted.web import static, server
from twisted.internet import reactor

root = static.File("/opt/lampp/htdocs")
root.putChild("doc", static.File("/usr/share/doc"))
reactor.listenTCP(8081, server.Site(root))
reactor.run()