curl -X POST -H "Content-Type: application/json" -d '{
  "greeting":[
    {
      "locale":"default",
      "text":"Hello {{user_first_name}}! Welcome. I am fify, your guide for everything DSCE. Tap or type Get Started to get going."
    }
  ] 
}'  "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAACVBMhfty8BAFngRPtEJ0yqwtoyEmFXqEMQb1ZA0ZBfeRcCOtWHvE4CjVJO0RvRTnZBVYZC7hMZCkIyg2dVMgrNzTAPMYWUvCJHWZASvmuGVOTl35I2XUL1hzQHJXnaWqQ80uZAj3AtZBThO6WbZCYA3cNk7QtLUKTshIRP0SMAfHAZDZD"
