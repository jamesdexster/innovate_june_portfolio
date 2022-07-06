from flask import Flask, render_template
from views import my_view

app = Flask(__name__) # creating an instance of a Flask class called app
app.register_blueprint(my_view)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)


# @app.route('/')
# def index():
#     return render_template("index.html") # Route page, linked to index with render_template function

# # route() - runs depending on browser e.g www.domain.com/""

# @app.route('/james') # 2nd Route
# def james():
#     return render_template("james.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# this if statement is the last thing on our app - it allows the initialisation of the app. Debug is set to true, and we pick a port to run on. 5000 is default, 8000 is linked to debugger