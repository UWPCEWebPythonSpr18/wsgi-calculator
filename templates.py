
class Template():
    
    def home():
     
        return '''   
        <head>
            <title>Internet Programming in Python: wsgi-calculator Assignment</title>
        </head>
        <body>
            <h1>Internet Programming in Python: wsgi-calculator Assignment</h1>
            <h2>Please follow the format below to operate the calculator:</h2>
            <p>For multiplacation: http://localhost:8080/multiply/3/5</p>
            <p>For addition:  http://localhost:8080/add/23/42</p>
            <p>For subtraction: http://localhost:8080/subtract/23/42</p>          
            <p>For division: http://localhost:8080/divide/22/11</p>               
        </body>
        '''

    def answer(operation, ans):

        page = '''
        <h1>The answer for the {} operation is: {}.</h1>
        '''
        return page.format(operation, ans)



