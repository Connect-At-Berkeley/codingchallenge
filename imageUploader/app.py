# Code based on pythonbuddy.com

from flask import Flask, render_template, request, jsonify, session

# Configure Flask App
# Remember to change the SECRET_KEY!
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

@app.route('/')
def index():
    """Display home page
        :return: index.html
    """
    session["count"] = 0
    return render_template("index.html")

'''
BEGIN TASK 1
'''
# Should you use a GET or POST Request?
# @app.route('/submit_image', methods=['POST'])
# @app.route('/submit_image', methods=['GET'])
def submit_image():
    """Adds an image to our server and adds it to our webpage. 
        Automatically refreshes our webpage so that user can see the image appended
    """
    # How do we store images in our server?

'''
END TASK 1
'''