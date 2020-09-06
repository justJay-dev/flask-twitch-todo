import os
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import kanboard



app = Flask(__name__)

app.config.from_pyfile('config.py')


bootstrap = Bootstrap(app)

kb = kanboard.Client(app.config['KANBOARD_ENDPOINT'],app.config['KANBOARD_METHOD'], app.config['KANBOARD_API_KEY'])

@app.route('/')
def index():
    return "hai twitch"

@app.route('/list')
def show_list():
    open_tasks = kb.get_all_tasks(project_id = app.config['KANBOARD_PROJECT_ID'], status_id = 1)
    closed_tasks = kb.get_all_tasks(project_id = app.config['KANBOARD_PROJECT_ID'], status_id = 0)
    return render_template('list.html', open_tasks = open_tasks, closed_tasks = closed_tasks) 



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port = int(os.environ.get('PORT', 8069)))
