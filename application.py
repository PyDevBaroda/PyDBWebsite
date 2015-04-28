from flask import *
from os.path import isfile
from os import getcwd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<pagename>')
def page(pagename):
    if isfile(getcwd() + '/templates/' + pagename + '.html' ) :
        return render_template(pagename + '.html')
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
