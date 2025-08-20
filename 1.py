from flask import Flask ,request,redirect,url_for,session,Response

app = Flask(__name__)
app.secret_key = "supersecert123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "gururaj" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials, try again", mimetype="text/plain")

    # <-- This runs only for GET request
    return '''
        <h2>Login page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

    
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
    <h2>welcome , {session["user"]}:</h2>
    <a href = {url_for("logout")}>logout</a>
    '''
    
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
