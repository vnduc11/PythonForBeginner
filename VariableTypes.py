
my_variable = '''
    <html>
        <head>
            <title>Website1 create by Python</title>
        </head>
        <body>
            <h1>Thuc hanh Python tot</h1>
        </body>
    </html>
'''

my_html_file = open("/Users/VanNgocDuc/Documents/1.Work/Project/PythonForBeginner/my_html_file.html", "w")

my_html_file.write(my_variable)

my_html_file.close()
