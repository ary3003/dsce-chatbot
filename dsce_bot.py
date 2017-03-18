import requests
import json
from flask import Flask, request
import apiai
import logging
import sys

ACCESS_TOKEN = 'EAACVBMhfty8BAEnEn1RZAuJFD202uuERpIfD9alerlK97MflZAmg8jqRUwZA0tPlv0ZA4J3gAdUEDYZClniPDaOqMauefq2F2kHmXjxgfKLsvzys3ITy4rkNZCci8pJ8E72Cm0F1gmnstbJwPHeJ9ZBtEFd8xnilPFq5medOMHgMwZDZD'

CLIENT_ACCESS_TOKEN = 'e65e41471aeb417584138ea544ef3497'

ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/', methods=['GET'])
def handle_verification():
    print "Handling Verification."
    if request.args.get('hub.verify_token') == 'my_voice_is_my_password_verify_me':
        print "Verification successful!"
        return request.args.get('hub.challenge')
    else:
        print "Verification failed!"
        return 'Error, wrong validation token'


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


def quick_reply(user_id, msg):
    data1 = {
        "recipient": {"id": user_id},
        "message": {
            "text": msg,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Aryan",
                    "payload": "PAYLOAD1"
                },
                {
                    "content_type": "text",
                    "title": "Rashi",
                    "payload": "PAYLOAD2"
                }
            ]
        }
    }
    resp1 = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data1)
    print(resp1.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']

    # prepare API.ai request for text messages
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = message

    # get response from API.ai
    api_response = req.getresponse()
    response_str = api_response.read().decode('utf-8')
    response_obj = json.loads(response_str)

    if 'result' in response_obj:

        response = response_obj["result"]["fulfillment"]['speech']
        '''reply(sender, response)
        type1 = response_obj["result"]["fulfillment"]['messages'][1]["type"]
        if type1 == 2:
            title = response_obj["result"]["fulfillment"]['messages'][1]["title"]
            replies = response_obj["result"]["fulfillment"]['messages'][1]['replies']'''
        print "Working! WOOHOO!"
        quick_reply(sender, response)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
