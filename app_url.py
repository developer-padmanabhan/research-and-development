import json
from flask import Flask,request, jsonify, render_template
from flask_cors import CORS
from otp_send import sendotp
from otp_verify import verifyotp
from send_sms import sendsms
from pdf import generatepdf
from aws_sentiment_capture import sentimentcapture
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
   return render_template('home.html')

@app.route('/sendotp',methods=['POST'])
def indexotp():
   return sendotp(request)

@app.route('/optverification',methods=['POST'])
def verify():
   return verifyotp(request)

@app.route('/generatesms',methods=['POST'])
def sendSMS():
   return sendsms(request)

@app.route('/generatepdf',methods=['GET'])
def sendPDF():
   return generatepdf(request)

@app.route('/sentiment',methods=['POST'])
def captureSentiment():
   return sentimentcapture(request)

if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.56.1",port=5000)
