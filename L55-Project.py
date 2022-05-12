from flask import Flask
import random

app = Flask(__name__)

correct_answer = random.randint(0, 9)

@app.route('/')
def number_guess():
    return ('<h1> "Guess a number between 0 & 9" </h1> '
            '<img src="http://cdn140.picsart.com/294101360037201.gif?to=min&r=1024"> </img>')


@app.route('/<n>')
def compare(n):
    guess = True
    while guess:
        if int(n) > correct_answer:
            return '<h1 >"Your guess is too high"</h1>\
                   <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"</img>'

        elif int(n) < correct_answer:
            return f'<p>"Your guess is too low"</p>\
                   <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"</img>'
        else:
            return '<h1> "You guessed right!" </h1>\
                   <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"> </img>'
            guess = False


if __name__ == '__main__':
    app.run(debug=True)