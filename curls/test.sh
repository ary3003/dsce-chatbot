curl -X POST -H "Content-Type: application/json" -d '{
  "setting_type" : "call_to_actions",
  "thread_state" : "existing_thread",
  "call_to_actions":[
    {
      "type":"postback",
      "title":"Help",
      "payload":"help"
    },
    {
      "type":"postback",
      "title":"Get Started",
      "payload":"get_started_payload"
    },
    {
      "type":"web_url",
      "title":"View Website",
      "url":"http://dayanandasagar.edu/dsce/"
    }
  ]
}' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAACVBMhfty8BANvGO7uX6JUgu2b42dbDMmiu6dDumN6VUZCiILyXFQy1cbEcaPdAomAdEPPeXmuOLD2OjnNaq25wIMzcvasfwols5ZAsGTLx7ZBRZBFlh1lS8x2rIbaMZB28l9U1Bu8bZB7ZCgsUpNfYCZCQZC9UZC3CVoftfAHoe8zgZDZD"
      
