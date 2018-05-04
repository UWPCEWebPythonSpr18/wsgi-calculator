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
  http://localhost:8080/divide/6/0     => HTTP "400 Bad Request"
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
def home_page():
    <h1>{title}</h1>
    <table>
      <tr><th>Author</th><td>{author}</td></tr>
      <tr><th>Publisher</th><td>{publisher}</td></tr>
      <tr><th>ISBN</th><td>{isbn}</td></tr>
    </table>
    <a href="/">Back to the list</a>

def add(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    sum = "0"
    output = args[0] + args[1]
    return str.output


def subtract(*args):
    output = args[0] - args[1]
    return str.output


def multiply(*args):
    output = args[0] * args[1]
    return str.output


def divide(*args):
    if (args[1] == 0):
        print("Undefined!!! You tried to divide by zero!")
        break
    else:
        output = args[0] / args[1]
    return str.output

# TODO: Add functions for handling more arithmetic operations.

def resolve_path(path):
    funcname, arg1, arg2 = path.split('/')
    """
    Should return two values: a callable and an iterable of
    arguments.
    """

    # TODO: Provide correct values for func and args. The
    # examples provide the correct *syntax*, but you should
    # determine the actual values of func and args using the
    # path.
    try:
        arg1val = int(arg1)
        arg2val = int(arg2)
    except ValueError:
        print("Please enter a valid number.")



    try:
        func = {"add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide}.get(funcname)
    except NameError:
        print("Please select an appropriate function.")

    args = [arg1val, arg2val]

    return func, args

def application(environ, start_response):

  functionoutput = func(args)
    # TODO: Your application code from the book database
    # work here as well! Remember that your application must
    # invoke start_response(status, headers) and also return
    # the body of the response in BYTE encoding.
    #
    # TODO (bonus): Add error handling for a user attempting
    # to divide by zero.
    pass

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
