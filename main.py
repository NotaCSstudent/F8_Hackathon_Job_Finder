import urllib.request
import json
import os
import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request, abort
import job_finder_helper as jfh


app = Flask(__name__)

# Install ffmpeg on host/server


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

        if attachmentType == "audio":
            attachmentUrl = request.json["entry"][0]["messaging"][0]["message"]["attachments"][0]["payload"]["url"]
            urllib.request.urlretrieve(attachmentUrl, "input.mp4")
            messengerClipToWav("input.mp4")
            job = jfh.wav2text("output.wav")
            jfh.Find_Job(job,0)            
            

        return 'success', 200
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
