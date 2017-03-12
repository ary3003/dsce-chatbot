from flask import Flask, request
import json
import requests
import os
from sys import argv


app = Flask(__name__)

WIT_TOKEN = os.environ.get('3CBB7JHIEZC66HBN2Y4D56CU6EWCCEQC')
FB_VERIFY_TOKEN = "my_voice_is_my_password_verify_me"
GRAPH_API = "https://graph.facebook.com/v2.6/me/messages?"

greetings = "HI"

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAACVBMhfty8BANvGO7uX6JUgu2b42dbDMmiu6dDumN6VUZCiILyXFQy1cbEcaPdAomAdEPPeXmuOLD2OjnNaq25wIMzcvasfwols5ZAsGTLx7ZBRZBFlh1lS8x2rIbaMZB28l9U1Bu8bZB7ZCgsUpNfYCZCQZC9UZC3CVoftfAHoe8zgZDZD'

@app.route('/', methods=['GET'])
def handle_verification():
  print "Handling Verification."
  if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
    print "Verification successful!"
    return request.args.get('hub.challenge', '')
  else:
    print "Verification failed!"
    return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print "Handling Messages"
  payload = request.get_data()
  print payload
  if payload['object'] == 'page':
    for entry in payload['entry']:
      if messages[0]:
        message = messages[0]
        sender = message['sender']['id']
        text = message['message']['text']
  #for sender, message in messaging_events(payload): 
        print "Incoming from %s: %s" % (sender, text)
    if message == "Get Started":
      quick_reply(PAT, sender, text)
    else:
      send_message(PAT, sender, text)
  return "ok"

def handle_postback():
  data = request.get_data()
  for payload in payload_events(payload):
    if payload == "GET_STARTED_PAYLOAD":
      quick_reply(PAT)


      

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"] # This returns a list
  for event in messaging_events: #This returns a dict
      if "message" in event and  "text" in event["message"]:
        yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
      #else:

def payload_events(payload):
  data = json.loads(payload)
  payload_events = data["entry"][0]['messaging'][0]['postback']
  if 'payload' in payload_events:
    yield payload_events['payload']
  

def greetings_reply(token, user):
  qs = "access_token=%s"%token
  r = requests.post(GRAPH_API+qs,
    data=json.dumps({
        "recipient": {"id": user},
        "message": {
          "text": "Hey there!"}
                     }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.code.ok:
    print r.text
        


    
                      
def quick_reply(access, user, text):
  qs = "access_token=%s"%access
  r = requests.post(GRAPH_API + qs,
    data=json.dumps({
      "recipient": {"id": user},
      "message": {
        "text": "Choose your language.",
        "quick_replies":[
          {
            "content_type":"text",
            "title":"English",
            "payload":"English"
            },
            {
              "content_type":"text",
              "title":"Hindi",
              "payload":"Hindi"
            }
          ]
        }
      }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text
      


def send_message(token, recipient, text):
  """Send the message text to recipient with id recipient.
  """
  qs = "access_token=%s"%token
  r = requests.post(GRAPH_API+qs,
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {
        "attachment":{
          "type":"template",
             "payload":{
               "template_type":"button",
               "text":"Need further assistance? Talk to our representative",
               "buttons":[
                 {
                   "type":"phone_number",
                   "title":"Call our Admission department",
                   "payload":"+919972971606"
                   }
                 ]

               }
          }
        }
      }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text

if __name__ == '__main__':
  app.run()
