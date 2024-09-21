from flask import Flask, jsonify, abort,Response

app = Flask(__name__)

class HttpMethod():
    GET = "GET"

@app.route('/')
def index():
    return "test index"

@app.route("/getcode", methods=[HttpMethod.GET])
def get_code():
    return jsonify("Random number or message")

@app.route("/plus/<num1>/<num2>", methods=[HttpMethod.GET])
def plus(num1, num2):
    try:
        res = float(num1) + float(num2)
    except Exception as err:
        raise abort(400, err)

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
