# import flask
from flask import Flask, redirect, url_for, render_template

# render_template will let us grab html files and render them. 



# create instance of web application
app = Flask(__name__)


# define website pages
#home page function to display what will be on the home page
#define route - decorate the function
@app.route("/")
@app.rout("/home")
def home():
    return render_template('index.html', content = "Testing")


# # parameter will grap that, when you type something between the brackets, it will grab that and pass that string it as a parameter to the function, and display it
# @app.route("/<name>")
# def user(name):
#     return f"hello {name}!"


# # re-directing to a different page
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name = 'Admin'))

# run the app 
if __name__ == "__main__":
    app.run(debug = True)


