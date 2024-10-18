#app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return '''
    <h1>Contact Page</h1>
    <p>Get in touch with me here.</p>
    <nav>
        <a href="/">Home</a> | 
        <a href="/about">About</a> | 
        <a href="/resume">Resume</a> | 
        <a href="/projects">Projects</a>
    </nav>
    '''

if __name__ == "__main__":
    app.run(debug=True)
