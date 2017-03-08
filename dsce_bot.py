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
  if payload['object'] == 'page':
    for entry in payload['entry']:
      messages = entry['messaging']
      if messages[0]:
        message = messages[0]
        fb_id = message['sender']['id']
        text = message['message']['text']
        client.run_actions(session_id = fb_id, message=text)
      else:
        return 'Received another event'
  return None

def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val
  

def fb_message(sender_id, text):
  data = {
      'recipient':{'id': sender_id},
      'message': {'text': text}
      }

  qs = 'access_token=' + PAT
  resp = requests.post('https://graph.facebook.com/v2.6/me/messages?' + qs, json=data)
  if resp.status_code != requests.codes.ok:
    print r.text
  return resp.content

def send(request, response):

  fb_id = request['context']
  text = response['text']
  fb_message(fb_id, text)

def get_forecast(request):
    context = request['context']
    entities = request['entities']
    loc = first_entity_value(entities, 'location')
    if loc:
        # This is where we could use a weather service api to get the weather.
        context['forecast'] = 'sunny'
        if context.get('missingLocation') is not None:
            del context['missingLocation']
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']
    return context

actions = {
  'send': send,
  'getForecast': get_forecast,

  }

client = Wit(access_token=WIT_TOKEN, actions = actions)

 

if __name__ == '__main__':
  app.run()
