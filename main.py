from flask import *
import google.generativeai as genai
import os, requests

genai.configure(api_key="AIzaSyDCX8Nzh7kUvnEEbH-mt4X3dHfErPB6-x8")
app = Flask(__name__)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@app.route("/")
def run_main():
    return "Hello World", 200
    
@app.route("/admin")
def run_admin():
    return "Hello Admin", 200

@app.route("/gemini")
def run_admin():
    response = model.generate_content(request.args.get(""))
    return response.text, 200



if __name__ == "__main__":
    app.run(port=80)