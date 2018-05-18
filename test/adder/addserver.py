from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/adder')
def addtwo():
    num1 = int(request.args['num1'])
    num2 = int(request.args['num2'])
    return jsonify(num1+num2)

app.run(debug=True, port=5001)