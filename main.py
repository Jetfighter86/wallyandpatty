from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def wedding():
    return render_template("home.html")

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/image/<filename>')
def image(filename=None):
    return send_from_directory(directory=r'C:\Users\Phillip\Dropbox (Ring)\images',filename=filename)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
