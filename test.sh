curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"1330260563705274"
  },
  "message":{
    "text":"Pick a color:",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Red",
        "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
      },
      {
        "content_type":"text",
        "title":"Green",
        "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN"
      }
    ]
  }
}' "https://graph.facebook.com/v2.6/me/messages?access_token=EAACVBMhfty8BANvGO7uX6JUgu2b42dbDMmiu6dDumN6VUZCiILyXFQy1cbEcaPdAomAdEPPeXmuOLD2OjnNaq25wIMzcvasfwols5ZAsGTLx7ZBRZBFlh1lS8x2rIbaMZB28l9U1Bu8bZB7ZCgsUpNfYCZCQZC9UZC3CVoftfAHoe8zgZDZD"    
