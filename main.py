from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def wedding():
    return render_template("home.html")

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/ceremony')
def ceremony():
    return render_template('ceremony.html')

"""IMAGES"""

@app.route('/image/slideshow/<filename>')
def imageslideshow(filename=None):
    return send_from_directory(directory=r'./images/slideshow',filename=filename)

@app.route('/image/homepage/<filename>')
def imagehomepage(filename=None):
    return send_from_directory(directory=r'./images/homepage',filename=filename)

@app.route('/image/aboutus/<filename>')
def imageaboutus(filename=None):
    return send_from_directory(directory=r'./images/aboutus',filename=filename)

@app.route('/image/story/<filename>')
def imagestory(filename=None):
    return send_from_directory(directory=r'./images/story',filename=filename)

@app.route('/image/icon/<filename>')
def imageicon(filename=None):
    return send_from_directory(directory=r'./images/icon',filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5005)
