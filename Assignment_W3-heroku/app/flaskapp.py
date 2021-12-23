from flask import Flask, request, jsonify
from app.bmi import bmi

# instantiate Flask App
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def bmi_api():
    '''
    Function to calculate the BMI from the parameters that are handed over 
    as json in the api call 
    '''
    params = request.get_json(force=True)

    return jsonify(bmi(params["weight"], params["height"]))