def simple_app(environ, start_response):
    """Sim"""
    status = "200 OK"
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'Hello World!\n\n邵曰信的网页']
