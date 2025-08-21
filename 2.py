from flask import Flask, request, redirect, url_for

app = Flask(__name__)
tasks = []   # simple storage

@app.route('/')
def home():
    return "<h1>To-Do List</h1>" + "<br>".join(tasks) + '''
        <form method="post" action="/add">
            <input type="text" name="task">
            <input type="submit" value="Add Task">
        </form>
    '''

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
