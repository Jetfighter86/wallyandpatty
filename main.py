from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def wedding():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=5005)