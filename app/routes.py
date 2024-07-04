from flask import Flask         # From the flask module import the Flask class

# OOP
app = Flask(__name__)           # Create an instance of the Flask class (an object)

@app.get("/")                   # Flask decorator that helps us create routes
def about():
    me = {                      # this is a dictionary
        "first_name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff and watching TV",
        "is_online": True
    }
    return me                  # Flask will convert compatible dictionaries into JSON for us!
