from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=blrsrv1;'
        'DATABASE=mstRMdesign;'
        'UID=sa;'
        'PWD=sa'
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.User_Master WHERE [1_User_ID] = ? AND [2_Password] = ?", (user_id, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for('home'))
        else:
            flash('Invalid User ID or Password. Please try again.')
    return render_template('login.html')

@app.route('/mchome')
def mchome():
    return render_template('mchome.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
