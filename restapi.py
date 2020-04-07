from flask import Flask, jsonify
from zeep import Client
import json
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
# @token_required
def index():
    client = Client('http://localhost:8000/?wsdl')
    result = client.service.getFaceEmbeddings("nid", "image string")
    return jsonify({
                    "service_status": result})


@app.route('/parse_nid',methods=['GET','POST'])
# @token_required
def parseNid():
    client = Client('http://localhost:8000/?wsdl')
    result = client.service.parseNid("image string")
    return jsonify(json.loads( result.decode('utf8')))

@app.route('/facce_verification',methods=['GET','POST'])
# @token_required
def faceVerification():
    return jsonify({
    "status": "matched",
    "description": "log of face part mach",
    "error": None
})

@app.route('/insert_nid_info',methods=['GET','POST'])
# @token_required
def insertNidInfo():
    return jsonify({
                "status": True,
                "error": None
                })

@app.route('/verify_nid_data',methods=['GET','POST'])
# @token_required
def verifyNidData():
    return jsonify({
            "status": True,
            "error": None
            })

@app.route('/generate_otp',methods=['GET','POST'])
# @token_required
def generateOtp():
    return jsonify({
            "otp": "1569",
            "expiration": 1585280243601,
            "error": None
            })


if __name__ == '__main__':
    app.run(debug=True)