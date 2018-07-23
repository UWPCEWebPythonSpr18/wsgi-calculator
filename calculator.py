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
def homepage(*args):
    page = """
    <head>
        <title>AWESOME CALCULATOR</title>
    </head>
    <body>
        <h1>Calculator Instructions</h1>
        <h2>Please enter a URL containing a mathematical function and two values.</h2>
        <h2>Such as this one shown - "http://localhost:8080/divide/22/11"</h2>
        <h2>Functions such as "add", "subtract", "multiply" and "divide" are available.</h2>
    </body>
    """
    return page


def add(*args):
    output = args[0] + args[1]
    print("Output Value: {}".format(output))
    returnval = str(output)
    print("ReturnVal: {}".format(returnval))
    return returnval


def subtract(*args):
    output = args[0] - args[1]
    returnval = str(output)
    return returnval


def multiply(*args):
    output = args[0] * args[1]
    returnval = str(output)
    return returnval


def divide(*args):
    if (args[1] == 0):
        print("Undefined!!! You tried to divide by zero!")
        output = "Undefined - You tried to divide by zero!"
    else:
        output = str(args[0] / args[1])
    return output

# TODO: Add functions for handling more arithmetic operations.


def resolve_path(path):
    print("Entered resolve_path")
    availablefuncs = {"add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide}
    crackedpath = path.split('/')
    if crackedpath[1] == '':
        func = homepage
        args = [0,0]
        return func, args
    else:
        print(crackedpath)
        funcname = crackedpath[-3]
        arg1 = crackedpath[-2]
        arg2 = crackedpath[-1]
        print("Vals: {}, {}, {}".format(funcname, arg1, arg2))
        print("FunctionCall: {}".format(funcname))
        try:
            arg1val = int(arg1)
            arg2val = int(arg2)
            print("Vals OK")
        except ValueError:
            print("Please enter a valid number.")
            return NameError
        if funcname in availablefuncs.keys():
            print("function name found")
            func = availablefuncs.get(funcname)
        else:
            print("Function name not found")
            return NameError
            print("Selected function: {}".format(funcname))
        args = [arg1val, arg2val]
    return func, args

def application(environ, start_response):

  #functionoutput = func(args)
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
      print("About to call path resolve")
      func, args = resolve_path(path)
      print("CalledResolve_path")
      body = func(*args)
      print("Called Body")
      if body == "Undefined - You tried to divide by zero!":
          status = "400 - Bad Request"
      else:
          status = "200 OK"
  except NameError:
      print("Triggered Nameerror")
      status = "404 Not Found"
      body = "<h1>Not Found</h1>"
  except Exception:
      status = "500 Internal Server Error"
      body = "<h1>Internal Server Error</h1>"
  finally:
      headers.append(('Content-length', str(len(body))))
      start_response(status, headers)
      return [body.encode('utf8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
