# Importing Flask
from flask import Flask

# Handle Requests
from flask import request

# Create an instance of this class
app = Flask(__name__) 

@app.route('/')
def index():
    return 'index'

# HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "This is post request"
    else:
        return "This is get Request"

