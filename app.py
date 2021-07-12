from flask import Flask , render_template , send_from_directory
import os , io
from tinytag import TinyTag
# import sys
# sys.setrecursionlimit(1500)
app = Flask(__name__)

@app.route('/')
def index():
    quran = os.listdir('quran')   
    map =  [{"index":s,"name":TinyTag.get(f'quran/{s}').title} for s in  quran]
    return render_template('index.html' , quran=map)


@app.route('/soraa/<id>')
def send_file(id):
    return send_from_directory('quran', id)

app.run(debug=True)