from flask import Flask
from flask import request

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing


@app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    if request.method == 'POST':
        url = request.form['url']
        return url
    return "Sorry"

app.run(port=9999, debug=True)
