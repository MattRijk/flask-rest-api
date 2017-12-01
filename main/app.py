from flask import Flask, render_template
from flask import request
import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# create app
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    if request.method == 'POST':
        return render_template('form.html')

@app.route('/store')
def store():
    return render_template('index.html')

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    return render_template('store.html', name=name)

@app.route('/store/<string:name>')
def get_store(name):
    return render_template('store.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)
