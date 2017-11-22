from src.daak.decorators import route

@route("/")
def test():
    return 'hello iran'