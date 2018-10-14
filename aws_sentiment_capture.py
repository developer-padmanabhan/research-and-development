import boto3
import json
from flask import Flask,request
app = Flask(__name__)
#@app.route("/hello",methods=['POST'])
def sentimentcapture(request):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1', aws_access_key_id='AKIAIOT3E45GM23IIUVQ',
                              aws_secret_access_key='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')
                
    message = request.json['message']

    print('Calling DetectSentiment')

    test=comprehend.detect_sentiment(Text=message,LanguageCode='en')['Sentiment']
    test_score=comprehend.detect_sentiment(Text=message,LanguageCode='en')['SentimentScore']
    result ={
            "Sentiment": test,
            "Sentiment_score" :test_score
        }
    print(json.dumps(result))
    return(json.dumps(result))
    print('End of DetectSentiment\n')

    print ("Done")

#if __name__ == "__main__":
# app.run(host="192.168.56.1",port=5000)
