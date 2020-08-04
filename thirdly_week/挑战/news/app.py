#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, abort
import os, json

result = {}
directory = os.path.join(os.getcwd(),'..','files')
for i in os.listdir(directory):
    file_path = os.path.join(directory, i)
    with open(file_path) as f:
        result[i[:-5]] = json.load(f)

file_title = {k:v['title'] for k,v in result.items()}

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html',file_title=file_title)

@app.route('/files/<filename>')
def file(filename):
    f = result.get(filename)
    if not f:
        abort(404)
    else:
        return render_template('file.html',content=f)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
