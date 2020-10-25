# flask-twitch-todo
a small flask service that reads from todo-rest


# Usage instructions.
1) Setup todo-rest. [Instructions here]('https://rhodecode.nyx.xyz/todo-rest/')
2) Clone this repository
3) setup venv
```py
python3 -m venv env
pip3 install -r requirments.txt
```
4) change ````sample-config.py```` to ````config.py```` and adjust variables as needed
5) run the app
```py
python3 app.py
```
6) by default the app is running at http://localhost:8069 (nice) you can add this as a browser source in OBS or whatever.
