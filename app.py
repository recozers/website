from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", is_home=True)

@app.route("/sport")
def sport():
    return render_template("sport.html", is_home=False)

@app.route("/projects")
def projects():
    return render_template("projects.html", is_home=False)

@app.route("/education")
def education():
    return render_template("education.html", is_home=False)

# Routes for each project
@app.route("/project1")
def project1():
    return render_template("project1.html", is_home=False)

@app.route("/project2")
def project2():
    return render_template("project2.html", is_home=False)

@app.route("/project3")
def project3():
    return render_template("project3.html", is_home=False)

@app.route("/project4")
def project4():
    return render_template("project4.html", is_home=False)

@app.route("/project5")
def project5():
    return render_template("project5.html", is_home=False)

@app.route("/project6")
def project6():
    return render_template("project6.html", is_home=False)

if __name__ == "__main__":
    app.run(debug=True)


# ChatGPT4o was used to help with some of the html/css 