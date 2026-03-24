from flask import Flask
app = flask(__name__)

@app.route('/')
def appPage():
    return 'welcome to app'