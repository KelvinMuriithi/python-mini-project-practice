from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = "flash message"


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER']= 'kelvin'
app.config['MYSQL_PASSWORD'] ='password'
app.config['MYSQL_DB'] = 'python_crud'

mysql = MySQL(app)


@app.route('/')
def Index():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM python_students")
    data = cur.fetchall()
    cur.close()
    
    
    return render_template('index.html', students =data)
@app.route('/insert', methods = ['POST'])




def insert():
    if request.method == "POST":
        
        flash("Data inserted successfully.")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO python_students (name, email, phone) VALUES(%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/update', methods =['POST', 'GET'])
def update():
    if request.method == "POST":
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        cur = mysql.connection.cursor()
        cur.execute(""" 
                    UPDATE python_students
                    SET name=%s, email=%s, phone=%s 
                    WHERE id=%s
                    """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete(id_data):
     cur = mysql.connection.cursor()
     cur.execute("DELETE FROM python_students WHERE id =%s", (id_data,))
     mysql.connection.commit()
     flash("Data deleted succefully")
     return redirect(url_for('Index'))        
    
       
    


if __name__ == "__main__":
    app.run()