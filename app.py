import os
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import httpx

app = Flask(__name__)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return "hai twitch"

@app.route('/list')
def show_list():
    r = httpx.get('http://localhost:8420')
    tasks = r.json()
    return render_template('list.html', open_tasks = tasks)

@app.route('/messenger')
def messenger_theme():
    r = httpx.get('http://localhost:8420')
    tasks = r.json()
    return render_template('messenger.html', open_tasks = tasks)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port = int(os.environ.get('PORT', 8069)))
