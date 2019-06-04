"""
For your homework this week, you'll be creating a wsgi application of
your own.

You'll create an online calculator that can perform several operations.

You'll need to support:

  * Addition
  * Subtractions
  * Multiplication
  * Division

Your users should be able to send appropriate requests and get back
proper responses. For example, if I open a browser to your wsgi
application at `http://localhost:8080/multiple/3/5' then the response
body in my browser should be `15`.

Consider the following URL/Response body pairs as tests:

```
  http://localhost:8080/multiply/3/5   => 15
  http://localhost:8080/add/23/42      => 65
  http://localhost:8080/subtract/23/42 => -19
  http://localhost:8080/divide/22/11   => 2
  http://localhost:8080/               => <html>Here's how to use this page...</html>
```

To submit your homework:

  * Fork this repository (Session03).
  * Edit this file to meet the homework requirements.
  * Your script should be runnable using `$ python calculator.py`
  * When the script is running, I should be able to view your
    application in my browser.
  * I should also be able to see a home page (http://localhost:8080/)
    that explains how to perform calculations.
  * Commit and push your changes to your fork.
  * Submit a link to your Session03 fork repository!


"""
import traceback

def instructions(*args):
    """Returns a STRING with instructions for the system"""
    body = ['<h1>Calculator Instructions<h1>',
            '<h3>Begin by typing the URL into the address bar <a href="localhost:8080">localhost:8080</a>.</h3>',
            '<p>Then type a "/" and add, subtract, multiply or divide</p>']

    body.append('</ul>')
    body.append('<p>Next, type "/x/y/... where x and y are the numbers to use.</p>')
    body.append('<p>Have fun!</p>')
  
    return '\n'.join(body)

def add(*args):
    """ Returns a STRING with the sum of the arguments """

    addition = sum(args)

    return str(addition)

def sub(*args):
    
    subtraction = args[0]
    for i in args[1:]:
          subtraction -= i
    return str(subtraction)


def mult(*args):

    multiplication = args[0]
    for j in args[1:]:
        multiplication = multiplication*j
    return str(multiplication)


def div(*args):
      
    division = args[0]
    try:
      for z in args[1:]:
            division = division/z
      return str(division)
    except ZeroDivisionError:
      return "You have attempted to divide by zero. A hole has been torn in the fabric of space-time"


def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """

    functions = {
        '': instructions,
        'add': add,
        'subtract': sub,
        'multiply': mult,
        'divide': div,
    }
    
    path = path.strip('/').split('/')

    try:
        func = functions[path[0]]
        args = [float(x) for x in path[1:]]
    except (KeyError, ValueError):
        raise NameError

    return func, args

def application(environ, start_response):
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
        print(traceback.format_exc())
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
