from flask import Flask, render_template, request, jsonify
import re
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)