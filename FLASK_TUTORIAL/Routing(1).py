# Importing Flask
from flask import Flask
from markupsafe import escape

# Create an instance of this class
app = Flask(__name__)  

# Use Router decorator
@app.route("/")
def app_route():
    return "<p>this is app routing</p>"

@app.route("/index")
def index_route():
    return "<p>this is index routing</p>"



# Variable rules
@app.route("/<name>")  #---> Slug url
def hello(name):
    return f"Hello, {escape(name)}"    #---> Escape is used to prevent from injection attacks

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# Converter Types  ------------>
# string - (default) accepts any text without a slash
# int - accepts positive integers
# float - accepts positive floating point values
# path - like string but also accepts slashes
# uuid - accepts UUID strings