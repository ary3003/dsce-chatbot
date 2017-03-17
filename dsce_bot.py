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


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
   # postback = data['entry'][0]['messaging'][0]['postback']['payload']
   # if(postback == 'GET_STARTED_PAYLOAD'):
    #    reply(sender, postback)


    # prepare API.ai request
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = message

    # get response from API.ai
    api_response = req.getresponse()
    response_str = api_response.read().decode('utf-8')
    response_obj = json.loads(response_str)
    if 'result' in response_obj:
        response = response_obj["result"]["fulfillment"]["speech"]
    reply(sender, response)
    if 'responses' in response_obj:
        response_replies = response_obj['responses'][0]['messages']
        response_title = response_obj['responses'][1]['title'][0]
    reply2(sender, response_replies, response_title)

    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
