from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():

    data = dict(os.environ)

    data['apple'] = 'orange'

    return jsonify(data)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=9000, debug=True)
