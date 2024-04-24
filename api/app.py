from models import *
from user import *
from movie_manage import *
from reporting import *
from topup import *


@app.route('/')
def home():
    return jsonify({
        'message':'welcome'
    })

if __name__ == '__main__':
    app.run(debug=True)