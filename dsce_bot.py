from flask import Flask, request
import json
import requests
import os
from sys import argv
from wit import Wit

app = Flask(__name__)

WIT_TOKEN = os.environ.get('3CBB7JHIEZC66HBN2Y4D56CU6EWCCEQC')
FB_VERIFY_TOKEN = "my_voice_is_my_password_verify_me"

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
  for sender, message in messaging_events(payload):
    print "Incoming from %s: %s" % (sender, message)
    if message == "What can I ask you?":
      quick_reply(PAT, sender, message)
    else:
        send_message(PAT, sender, message)
  return "ok"


      

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
      if "message" in event and  "text" in event["message"]:
        yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
 #     else:
        #
        

"""def function(token, user):
  r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=%s"%token1,
      data = json.dumps({
        "recipient": {"id": user},
        "message": {
        "text": "You selected OPTION 1"},
        }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text
        
  

def postback_events(payload):
  data = json.loads(payload)
  postback_events = data["entry"][0]["postback"]
  for event in postback_events:
    yield postback["postback"]["payload"]
  

def postback_received(token1, postback):
  r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=%s"%token1,
      data = json.dumps({
        "recipient": {"id": user1},
        "message": {
        "text": "You can ask: ",
        "quick_replies":[
          {
            "content_type":"text",
            "title":"Option1",
            "payload":"OPTION1_PAYLOAD"
            },
            {
              "content_type":"text",
              "title":"Option2",
              "payload":"OPTION2_PAYLOAD"
            }
          ]
        },
          "postback": {
          "payload": "GET_STARTED_PAYLOAD"
          }
          
        
        }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text

    """

    
                      
          
        
    
    

def quick_reply(access, user, text1):
  r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=%s"%access,
    data=json.dumps({
      "recipient": {"id": user},
      "message": {
        "text": "You can ask: ",
        "quick_replies":[
          {
            "content_type":"text",
            "title":"Option1",
            "payload":"DEVELOPER_DEFINED_PAYLOAD"
            },
            {
              "content_type":"text",
              "title":"Option2",
              "payload":"DEVELOPER_DEFINED_PAYLOAD"
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

  r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=%s"%token,
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
