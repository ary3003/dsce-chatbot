""" for sender, message in messaging_events(payload):
    print "Incoming from %s: %s" % (sender, message)
    if message == "What can I ask you?":
      quick_reply(PAT, sender, message)
    else:
        send_message(PAT, sender, message)
  return "ok"
  """


 
"""
def messaging_events(payload):
  Generate tuples of (sender_id, message_text) from the
  provided payload.
  
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
      if "message" in event and  "text" in event["message"]:
        yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
 #     else:
        #
        """
        

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
