from flask import Flask, render_template, request
import plotly
import plotly.graph_objs as go
import pandas as pd
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/kuis1')
def kuis1():
    return render_template('kuis1.html')

@app.route('/kuis2')
def kuis2():
    return render_template('kuis2.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)