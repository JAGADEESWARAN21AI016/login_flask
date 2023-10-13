from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for security


# Simulated user database (for demonstration purposes)
users = {
    'username': 'password',
    'jaga': '1234'
}


@app.route('/')
def home():
    if 'username' in request.cookies:
        username = request.cookies.get('username')
        return f'Hello, {username}! <a href="/logout">Logout</a>'
    return 'Welcome! <a href="/login">Login</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            response = make_response(redirect('/'))
            response.set_cookie('username', username)
            return response
        else:
            return 'Invalid username or password. <a href="/login">Try Again</a>'
    return render_template('login.html')


@app.route('/logout')
def logout():
    if 'username' in request.cookies:
        response = make_response(redirect('/'))
        response.delete_cookie('username')
        return response
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
