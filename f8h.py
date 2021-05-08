import speech_recognition as sr
import os

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

def main():
    audFile = input("Enter audio file name: ")
    wav2txt(audFile)

if __name__ == "__main__":
    main()