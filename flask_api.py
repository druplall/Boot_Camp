# Flask tutorial
# The request is what your browser is doing, searching the internet is a request.. The Response is what you get back.
# Whenever we go to google the request is the following
## GET / HTTP/1.1
## GET IS THE VERB, THE / is the path and the HTTP is the protocol
## HOST: www.google.com
## The get is the verb that tells the server what we think it will return (Protocol)
## Example: GET /download/mac HTTP/1.1
## https:/git-sccm

# What are the main verbs ? GET, POST, PUT and Delete
# Get will retrive something
# POST will recive data, and use it
# PUT Make sure something is there
# DELETE will remove something

# What is the principle of REST API? Its a way of thinking about how a web server responds to your request
# It will response with resources (aka data)
# Is is stateless -- This means one request cannot depend on any other request, the server will only know about the current request and not any of the previous requests



from flask import Flask
# Always us upper case for the first letter for the Class, Lower letter is usually the package

app = Flask(__name__)
# __ is a special variable that gives each file a unique name

# We need to use a decoriate for the Flask to understand
@app.route('/') # 'https://www.google.com/'
def home():
    return "Hello,world!"

app.run(port=5000)
# What is the port ? Is an area of the computer where you will recive a response