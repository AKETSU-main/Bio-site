from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    age = datetime.now().year - 2009
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(debug=True)