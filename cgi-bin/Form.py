import cgi
import html

form = cgi.FieldStorage()
text = form.getfirst("text", "не задано")
text = html.escape(text)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных формы</title>
        </head>
        <body>""")

print("<h1>Обработка данных формы!</h1>")
print("<p>text: {}</p>".format(text))

print("""</body>
        </html>""")
