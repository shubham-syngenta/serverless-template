from flask import Flask, jsonify, make_response
import subprocess
import structlog

app = Flask(__name__)



@app.route("/")
def hello_from_root():
    logs= subprocess.getoutput("printenv")
    print(logs)
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    print("logs printing")
    return jsonify(message='Hello from path!')


@app.errorhandler(404)

def resource_not_found(e):
    print(e)
    return make_response(jsonify(error='Not found!'), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
