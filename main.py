import urllib.request
import json
import os
import requests
import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request, abort
import job_finder_helper as jfh

app = Flask(__name__)


PAGE_ACCESS_TOKEN = 'EAACMn1ZClEwMBAMP3Mwd434nGLaoyzKFaAcZA1zcJQtTGPjdHLuR36S37TEm9ecl9hIThn1Rbm2eqR3RXE2k7YrpUZBXfjuGtrb6V8zptVo2pZBbvZBTwWquuk6idxR187PhcZC3PnK6ZAOZB8kZAW8YUGhVTW1c3868mVc2KHrC08dxXjy4ZC4uYZC0mD49z5BOgURMg1WLMZBhVNVyA9D04ZAWG'


# Send a response back to the user
def sendListOfJobs(recipient_id, text):

    elementsList = []

    for i in range(0, 7):
        newElement = {"title": text[i]["company"],
                      "subtitle": text[i]["name"] + " - " + text[i]["location"]}
        elementsList.append(newElement)

    payload = {
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'attachment': {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elementsList
                }
            }
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        "https://graph.facebook.com/v10.0/me/messages?access_token=" + PAGE_ACCESS_TOKEN,
        params=auth,
        json=payload
    )

    return response.json()


# Converting messenger sent audio to .wav format on MACOS
def messengerClipToWavMac(audioFileName):
    file = AudioSegment.from_file('/'+audioFileName, format="mp4")
    output = file.export("/output.wav", format="wav")


def messengerClipToWav(audioFileName):
    file = AudioSegment.from_file('./'+audioFileName, format="mp4")
    output = file.export("./output.wav", format="wav")


@app.route('/verify')
def webhook():
    VERIFY_TOKEN = "token_verification_f8_hackathon"
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge

    return 'success', 200


@app.route('/message', methods=['POST'])
def handleMessage():
    if request.method == 'POST':
        attachmentType = request.json["entry"][0]["messaging"][0]["message"]["attachments"][0]["type"]
        senderId = request.json["entry"][0]["messaging"][0]["sender"]["id"]
        if attachmentType == "audio":
            attachmentUrl = request.json["entry"][0]["messaging"][0]["message"]["attachments"][0]["payload"]["url"]
            # Download the audio file sent from messenger
            urllib.request.urlretrieve(attachmentUrl, "input.mp4")
            messengerClipToWav("input.mp4")
            job = jfh.wav2txt("output.wav")
            listOfJobs = jfh.Find_My_Job(job)
            # sendListOfJobs(senderId, listOfJobs)  # Send list of jobs to user.
            # Debug to check if message was sent successfully
            print(sendListOfJobs(senderId, listOfJobs))

        return 'success', 200
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
