def simple_app(environ, start_response):
    """Sim"""
    status = "200 OK"
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'Hello World!\n\nsyx\n']


class AppClass(object):
    status = "200 OK"
    response_headers = [('Content-type', 'text/html')]

    def __call__(self, environ, start_response):
        print(environ, start_response)
        start_response(self.status, self.response_headers)
        return [b'Hello AppClass.__call__\n']


application = AppClass()


class APpClassIter(object):
    status = "200 OK"
    response_headers = [('Content-type', 'text/html')]

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response(self.status, self.response_headers)
        yield b'Hello APpClassIter\n'
