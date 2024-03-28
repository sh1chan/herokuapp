#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'ames0k0'

from flask import Flask, render_template

app = Flask(
  __name__, template_folder='templates', static_folder='static'
)


@app.route('/')
def shichan():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(debug=True)
