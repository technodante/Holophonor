from flask import Flask, render_template, request, jsonify
import json
import google.generativeai as genai

app = Flask(__name__)

@app.route('/')
def index():
  return 'oof' # render_template('test.html')