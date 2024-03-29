# This is mandatory for Flask projects
from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)


# .route() is used to the app which URL should call the associated function
@app.route('/')
def index():
    return render_template("index.html")


# Runs the application
if __name__ == "__main__":
    app.run(debug=True)

