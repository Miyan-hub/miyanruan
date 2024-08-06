from flask import *

app = Flask(__name__)

@app.route("/")
def run_main():
    return "Hello World", 200
    
@app.route("/admin")
def run_admin():
    return "Hello Admin", 200



if __name__ == "__main__":
    app.run(port=80)