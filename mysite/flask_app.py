
from flask import Flask, render_template, request


def search4letters(phrase: str, letters: str) -> set:
    """ return any letters in a phrase """
    return set(letters).intersection(set(phrase))


app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Are your letters in that Phrase?')


@app.route('/hangman')
def hangman_page() -> 'html':
    return render_template('hangman.html', the_title='Lets Play Hangman!!')

@app.route('/search', methods=['POST'])
def do_seach() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title ='Here are those results'
    results = str (search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results,)


if __name__ == '__main__':
    app.run(debug=True)
