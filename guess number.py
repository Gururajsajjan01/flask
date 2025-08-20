import random
from flask import Flask, request

app = Flask(__name__)
number = random.randint(1, 10)

@app.route('/')
def guess_form():
    return '''
        <h2>Guess a number (1–10)</h2>
        <form method="post" action="/check">
            <input type="number" name="guess">
            <input type="submit" value="Check">
        </form>
    '''

@app.route('/check', methods=['POST'])
def check():
    guess = int(request.form['guess'])
    if guess == number:
        return "🎉 Correct!"
    elif guess < number:
        return "Too low! Try again."
    else:
        return "Too high! Try again."

if __name__ == '__main__':
    app.run(debug=True)
