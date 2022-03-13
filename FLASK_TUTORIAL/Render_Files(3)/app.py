# Importing Flask
from flask import Flask

# Render Templates
from flask import render_template

# Create an instance of this class
app = Flask(__name__) 

# Render html files
@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # through name we can send parameters to our html file
    return render_template('./hello.html', name=name)