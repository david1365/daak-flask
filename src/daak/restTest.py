from src.daak.decorators import jsonPost

@jsonPost()
def test():
    return 'hello iran'