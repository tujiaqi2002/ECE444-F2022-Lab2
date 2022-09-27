from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
boostrap = Bootstrap(app)
moment=Moment(app)

@app.route('/')
def index():
    return render_template('user.html',name='Alfa',current_time=datetime.utcnow())

    

@app.route("/user/<name>")
def user(name):
    return f"<h1> Hello, {name}!</h1>"

"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
"""

if __name__ == "__main__":
    app.run(debug=True)