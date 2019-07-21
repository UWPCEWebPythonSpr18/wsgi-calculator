
import traceback
from templates import Template


def home():
    
    return Template.home()

def add(*args):
    
    try:
        sum = 0
        for i in range(0, len(args)):
            sum = sum + int(args[i])
    except ValueError:
        return "This application requires integer values."
    return str(sum)

def subtract(*args):

    try:
        diff = int(args[0])
        for i in range(1, len(args)):
            diff = diff - int(args[i])
    except ValueError:
        return "This application requires integer values."
    return str(diff)


def multiply(*args):

    try:
        multiple = 1
        for i in range(0, len(args)):
            multiple = multiple * int(args[i])
    except ValueError:
        return "This application requires integer values."
    return str(multiple)


def divide(*args):

    try:
        div = int(args[0])
        for i in range(1, len(args)):
            div = div / int(args[i])
    except ValueError:
        return "This application requires integer values."
    except ZeroDivisionError:
        return "Cannot divide by zero."
    return str(div)


def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """
    funcs = {
        '': home,
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
    }
    path = path.strip('/').split('/')
    func_name = path[0]
    args = path[1:]
    try:
        func = funcs[func_name]
    except KeyError:
        raise NameError

    return func_name, func, args

def application(environ, start_response):
    headers = [('Content-type', 'text/html')]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func_name, func, args = resolve_path(path)
        body = Template.answer(func_name, func(*args))
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = '<h1>Not Found</h1>'
    except Exception:
        status = '500 Internal Server Error'
        body = '<h1>Internal Server Error</h1>'
        print(traceback.format_exc())
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
