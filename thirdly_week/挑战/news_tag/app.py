#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, abort
from db import *

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
