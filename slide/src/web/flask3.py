from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/images/<f>')
def show_image(f):
    return app.send_static_file('images/' + f)


@app.route('/result.html')
def show_result():
    text = '<html><body>Picture List<br/>'
    import os
    images = []

    for f in os.listdir(os.path.join('images')):
        images.append(f)
    for img in images:
        text += '<img width="200" height="250" src="images/' + img + '"/><br/>'
    text += '</body></html>'
    return text


@app.route('/fac/<n>')
def factorial(n):
    total = 1
    print(type(n))
    m = int(n)
    for i in range(m):
        total = total*(i+1)
    return total


@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing

app.run(port=9999, debug=True)
