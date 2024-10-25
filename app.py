#app.py
from flask import Flask, render_template, request, redirect 

from projects import Project

# Initialize the database table when the app starts
Project.create_table()

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
    all_projects = Project.get_all_projects()
    return render_template("projects.html", projects=all_projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/forms", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        image_file = request.form['image_file']  # Assume the image file is already uploaded in static/images/
        
        new_project = Project(title, description, image_file)
        new_project.save()
        
        return redirect("/projects")

    return render_template("forms.html")

@app.route("/delete/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    Project.delete_project(project_id)  # Call the method to delete the project
    return redirect("/projects")


if __name__ == "__main__":
    app.run(debug=True)
