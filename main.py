from flask import *
import google.generativeai as genai
import os, requests, json

genai.configure(api_key="AIzaSyDCX8Nzh7kUvnEEbH-mt4X3dHfErPB6-x8")
app = Flask(__name__)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@app.route("/")
def run_main():
    return "Hello World", 200
    
@app.route("/gemini")
def run_gemini():
    response = model.generate_content(request.args.get(""))
    return response.text, 200

@app.route("/gpt")
def run_gpt():
    response = requests.get("https://api.guruapi.tech/ai/gpt4", params={'username': "Miyan",'query': request.args.get('')}).json()
    return response['msg'], 200

@app.route("/bing")
def run_bing():
    response = requests.get("https://gpt4.guruapi.tech/bing", params={'username': "Miyan",'query': request.args.get('')}).json()
    return response['result'], 200

@app.route("/dalle")
def run_dalle():
    response = requests.get("https://api.gurusensei.workers.dev/dream", params={'prompt': request.args.get('')})
    open("dalle.jpg","wb").write(response.content)
    return send_file("dalle.jpg"), 200



if __name__ == "__main__":
    app.run(port=80,host="0.0.0.0")