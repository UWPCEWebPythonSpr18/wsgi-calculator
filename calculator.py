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


def add(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    print(args)
    val = 0
    for i in args:
      val += int(i)
    return str(val)

# TODO: Add functions for handling more arithmetic operations.

def multiply(*args):
    val = 1
    for i in args:
      val *= int(i)
    return str(val)


def subtract(*args):
    val = int(args[0])
    for i in args[1:]:
      val -= int(i)
    return str(val)


def divide(*args):
    val = int(args[0])
    for i in args[1:]:
      val /= int(i)
    return str(val)


def resolve_path(path):
    funcs = { 'add':add,
             'multiply':multiply,
             'subtract':subtract,
             'divide':divide
           }

    path = path.strip('/').split('/')
    args = path[1:]
    args = [int(arg) for arg in args]
    func_name = path[0]

    try:
        func = funcs[func_name]
    except KeyError:
        raise NameError

    return func, args

def application(environ, start_response):
    # TODO: Your application code from the book database
    # work here as well! Remember that your application must
    # invoke start_response(status, headers) and also return
    # the body of the response in BYTE encoding.
    #
    # TODO (bonus): Add error handling for a user attempting
    # to divide by zero.
    headers = [("Content-type", "text/html")]

    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError

        if path == '/':
            body = "<body>To Calculate: choose a function from [add, subtract, multiply, divide]"+"\r\n"
            body += "followed by /x/y where x and y are the integers to calculate."+"\r\n\r\n"
            body += "example: visit localhost:8080/add/2/3 to display 5.</body>"
        else:
            func, args = resolve_path(path)
            body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 NOT FOUND"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 INTERNAL SERVER ERROR"
        body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]

if __name__ == '__main__':
    # TODO: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
