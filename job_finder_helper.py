import speech_recognition as sr
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Begin Job Finder


def Get_Url(Job: str):
    Template = 'https://www.indeed.com/jobs?q={}&l=New+York%2C+NY'

    Url = Template.format(Job)

    return Url


def Find_Job(Job_Response, Number_Of_Jobs: int):

    # Parses into an HTML Tree Structure
    Job_Soup = BeautifulSoup(Job_Response.text, "html.parser")

    Name_Of_Role = Job_Soup.find_all(
        'div', 'jobsearch-SerpJobCard')  # Role name tag

    Name_Finder = Name_Of_Role[Number_Of_Jobs]

    Name = Name_Finder.h2.a

    # Gets the company name and strips out anything thats not needed
    Company = Name_Finder.find('span', 'company').text.strip()

    Company_Location = Name_Of_Role[Number_Of_Jobs]  # Starting at index

    Location = Company_Location.find('div', 'recJobLoc').get(
        'data-rc-loc')  # gets the role

    # Details = Name['title'] + "\n" + Company + "\n" + Location
    Details = {"name": Name['title'], "company": Company, "location": Location}
    return (Details)


headers = [{'User-Agent': 'Mozilla/5.0'}]


def Find_My_Job(Insert_Job: str):
    Job_List = []

    Job_Url = Get_Url(Insert_Job)  # For the Helper Function Above

    Job_Response = requests.get(Job_Url)  # Getting a Response from the URL

    for i in range(1, 15):
        try:
            Job_List.append(Find_Job(Job_Response, i))
            # print(Find_Job(Insert_Job, i))
        except(IndexError):
            pass
    return Job_List

# End Job Finder


# Begin wav to text
def wav2txt(audioFileName):
    reco = sr.Recognizer()
    reco.energy_threshold = 300

    givenAudioFile = sr.AudioFile(audioFileName)

    with givenAudioFile as srcFile:
        givenAudioFile = reco.record(srcFile)

    userCommand = reco.recognize_wit(
        givenAudioFile, "O7NTCSR3OEK6VZOGW4I65N6P5OTKSI3C")
    if userCommand.find(' in') > -1:
        userCommand = userCommand[(userCommand.find('looking for ') + 12):]
        userCommand = userCommand[:userCommand.find(' in')]
    else:
        userCommand = userCommand[(userCommand.find('looking for ') + 12):]
    if userCommand.find('recent ') > -1:
        userCommand = userCommand[(userCommand.find('recent ') + 7):]

   
    return userCommand

# End wav to text
