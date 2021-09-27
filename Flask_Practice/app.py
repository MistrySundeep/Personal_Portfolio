# This is mandatory for Flask projects
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="app")
Bootstrap(app)


# .route() is used to the app which URL should call the associated function
@app.route('/')
def index():
    return render_template("base.html")


# Runs the application
if __name__ == "__main__":
    app.run(debug=True)

