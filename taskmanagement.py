from flask import Flask,render_template, request, jsonify
import sqlite3
import smtplib, sslapp = Flask(__name__)######smtp_server = "smtp.gmail.com"
port = 587
sender_email = "youremail@gmail.com"
password = 'your_code'####connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, isCompleted INTEGER)')@app.route("/<int:id>")
def get_task(id, methods=["GET"]):
   connect = sqlite3.connect('database.db')
   cursor = connect.cursor()
   cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,))
   data = cursor.fetchall()
   return jsonify(data)@app.route("/")
def get_all_task(methods=["GET"]):
   connect = sqlite3.connect('database.db')
   cursor = connect.cursor()
   cursor.execute('SELECT * FROM tasks')
   data = cursor.fetchall()
   return jsonify(data)@app.route("/add/<title>")
def add_task(title, methods=["POST"]):
   with sqlite3.connect("database.db") as users:
       cursor = users.cursor()
       cursor.execute('INSERT INTO tasks (title, isCompleted) VALUES (?, ?)', (title, 0))
       users.commit()   return jsonify({'message': 'Task added successfully'})@app.route("/update/<int:id>")
def complete_task(id, methods=["PUT"]):
   with sqlite3.connect("database.db") as users:
       cursor = users.cursor()
       cursor.execute('UPDATE tasks SET isCompleted = 1 WHERE id = ?', (id,))
       users.commit()   return jsonify({'message': 'Task updated successfully'})@app.route("/delete/<int:id>")
def delete_task(id, methods=["DELETE"]):
   with sqlite3.connect("database.db") as users:
       cursor = users.cursor()
       cursor.execute('DELETE FROM tasks WHERE id = ?',(id,))
       if cursor.rowcount == 0:
           return jsonify({'message': 'Data not found'})
       users.commit()
   return jsonify({'message': 'Task deleted successfully'})@app.route("/send-email/<int:id>")
def send_email(id, methods=["GET"]):
   context = ssl.create_default_context()
   try:
       server = smtplib.SMTP(smtp_server,port)
       server.ehlo() # Can be omitted
       server.starttls(context=context) # Secure the connection
       server.ehlo() # Can be omitted
       server.login(sender_email, password)
       # TODO: Send email here
       server.sendmail(sender_email, 'eliye.vr.evan13@gmail.com', 'Olmaz')
       return jsonify({'message': 'Email sent successfully'})
   except Exception as e:
       # Print any error messages to stdout
       return jsonify({'error': str(e)}), 500
   finally:
       server.quit()if __name__ == '__main__':
   app.run(host='localhost', port=5001) (edited) 
