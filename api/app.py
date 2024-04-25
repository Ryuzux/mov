from flask import jsonify
from models import *
from movie_manage import *
from reporting import *



@app.route('/')
def home():
    return jsonify({
        'message':'hello'
    })

if __name__ == '__main__':
    app.run(debug=True)