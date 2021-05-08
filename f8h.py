import speech_recognition as sr
import os
import converter


def wav2txt(audioFileName):
    reco = sr.Recognizer()
    reco.energy_threshold = 300

    givenAudioFile = sr.AudioFile(audioFileName)

    with givenAudioFile as srcFile:
        givenAudioFile = reco.record(srcFile)

    print(reco.recognize_wit(givenAudioFile, "O7NTCSR3OEK6VZOGW4I65N6P5OTKSI3C"))

    txtFile = open("audioAsText.txt", "w+")
    txtFile.write(reco.recognize_wit(givenAudioFile, "O7NTCSR3OEK6VZOGW4I65N6P5OTKSI3C"))
    txtFile.close()

def clip2wav(audioFileName):
    c = Converter()
    conv = c.convert(audioFileName, 'audio.mp3', {'format':'mp3','audio':{'codec': 'mp3','bitrate':'22050','channels':1}})
    for timecode in conv:
        pass    
    os.system("mpg123 -w audio.wav audio.mp3")
    wav2txt("audio.wav")


def main():
    audFile = input("Enter audio file name: ")
    clip2wav(audFile)
    

if __name__ == "__main__":
    main()