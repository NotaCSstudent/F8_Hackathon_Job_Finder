import urllib.request
import json
import os
import requests
import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request, abort
import job_finder_helper as jfh


app = Flask(__name__)

# Install ffmpeg on host/server

# Send a response back to the user
PAGE_ACCESS_TOKEN = 'EAACMn1ZClEwMBAMP3Mwd434nGLaoyzKFaAcZA1zcJQtTGPjdHLuR36S37TEm9ecl9hIThn1Rbm2eqR3RXE2k7YrpUZBXfjuGtrb6V8zptVo2pZBbvZBTwWquuk6idxR187PhcZC3PnK6ZAOZB8kZAW8YUGhVTW1c3868mVc2KHrC08dxXjy4ZC4uYZC0mD49z5BOgURMg1WLMZBhVNVyA9D04ZAWG'


def send_message(recipient_id, text):

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


def messengerClipToWavMac(audioFileName):
    file = AudioSegment.from_file('/'+audioFileName, format="mp4")
    output = file.export("/output.wav", format="wav")


def messengerClipToWav(audioFileName):
    file = AudioSegment.from_file('./'+audioFileName, format="mp4")
    output = file.export("./output.wav", format="wav")


@app.route('/test')
def webhook():
    VERIFY_TOKEN = "test"
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print("Worked")
            return challenge

    return 'success', 200


@app.route('/test', methods=['POST'])
def handleMessage():
    if request.method == 'POST':
        # print(request.json)
        attachmentType = request.json["entry"][0]["messaging"][0]["message"]["attachments"][0]["type"]
        senderId = request.json["entry"][0]["messaging"][0]["sender"]["id"]
        if attachmentType == "audio":
            attachmentUrl = request.json["entry"][0]["messaging"][0]["message"]["attachments"][0]["payload"]["url"]
            urllib.request.urlretrieve(attachmentUrl, "input.mp4")
            messengerClipToWav("input.mp4")
            job = jfh.wav2txt("output.wav")
            listOfJobs = jfh.Find_My_Job(job)
            print(send_message(senderId, listOfJobs))

        return 'success', 200
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
