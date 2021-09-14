from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route("/index")
def index():
    return render_template('index.html')
    
@app.route("/aboutFrame")
def aboutFrame():
    return render_template('aboutFrame.html')
    
@app.route("/projectFrame")
def projectFrame():
    return render_template('projectFrame.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
