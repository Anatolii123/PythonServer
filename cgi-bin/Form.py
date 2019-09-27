import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text3 = form.getfirst("TEXT_3", "не задано")
text4 = form.getfirst("TEXT_4", "не задано")
text5 = form.getfirst("TEXT_5", "не задано")
text6 = form.getfirst("TEXT_6", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)
text3 = html.escape(text3)
text4 = html.escape(text4)
text5 = html.escape(text5)
text6 = html.escape(text6)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Имя: {}</p>".format(text1))
print("<p>Фамилия: {}</p>".format(text2))
print("<p>Дата рождения: {}</p>".format(text3))
print("<p>Пол: {}</p>".format(text4))
print("<p>Желание поговорить о баге: {}</p>".format(text6))
print("<p>Комментарий: {}</p>".format(text5))
print("""
        <form action="http://localhost:8002/cgi-bin/Form.py" method="post">
        <table width="200%" cellspacing="0" cellpadding="4">
         <tr>
             <td align="right" width="100">Имя:</td>
             <td><input type="text" name="TEXT_1" maxlength="50" size="20"></td>
         </tr>
         <tr>
             <td align="right">Фамилия:</td>
             <td><input type="text" name="TEXT_2" maxlength="50" size="20"></td>
         </tr>
         <tr>
             <td align="right">Дата рождения:</td>
             <td><input type="text" name="TEXT_3" maxlength="50" size="20"></td>
         </tr>
         <tr>
             <td align="right">Пол:</td>
             <td><select type="select" name="TEXT_4" rows="1">
                  <option>мужской</option>
                  <option>женский</option>
                  <option>не определилось</option>
                 </select>
             </td>
         </tr>
         <tr>
               <td align="right">Хотите поговорить о баге?</td>
               <td>
                   <input name="TEXT_6" type="radio" value="Аминь"> Аминь
                   <input name="TEXT_6" type="radio" value="Алюминь"> Алюминь
                   <input name="TEXT_6" type="radio" value="Нет" checked> Нет
               </td>
         </tr>
         <tr>
             <td align="right" valign="top">Комментарий</td>
             <td><textarea name="TEXT_5" cols="35" rows="10"></textarea></td>
         </tr>
        </table>
        <br>
        <input type="submit">
    </form>
""")
print("""</body>
        </html>""")



