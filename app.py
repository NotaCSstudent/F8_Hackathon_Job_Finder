from flask import Flask
import requests
import f8h

app = Flask(__name__)


#Tokens 
ACCESS_TOKEN = 'EAANNgPpVsZBgBADi7RcIdxXFKOoQlCkJdkAkXpqKxrYwG2vxEgO3OmFhWX4phhaY5uTz1cLvd4cSEfMY6SpgEVWVaA1dwHbYge7S68dYKeUxT59VVA2pS9dN8MJyu4HUnGT5AngZAjET95dFr5MHi8PQoyXsznHwI4btQw1SBeoZA6LgZCRt'
VERIFY__TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)
##Get and post will be handling our endpoints from the user and the bot
@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'Hello, World!'




def Get_Bot_Response(message : str):
    return "Good morning"

#Verify Our webhook being connected
def Verify_Webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


# Formulate a response to the user and pass it to the function that sends it
def respond(sender, message):
    locate = message
    y = get_location(locate)
    response = get_bot_response(y,"Pizza")
    send_message(sender, response)

# Check if the message is a message from the user
def is_user_message(message):
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))

# Main function flask uses to listen at the "/webhook" endpoint
@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "ok"

# Send a response back to the user
def send_message(recipient_id, text):
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN_CAT
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()

if __name__ == '__main__':
    app.run()