# F8_Hackathon_Job_Finder

We are creating a job finding application that takes an audio input from the user, such as:
    ```
    I am looking for a software engineer job
    I am looking for a Data Analyst Job
    ```
and will find the seven most recent job postings on Indeed in New York City and New Jersey.

## Contributors

- [Yash Mahtani](https://github.com/gasperjw1)
- [OminaRU](https://github.com/OminaRU)
- [dev-rb](https://github.com/dev-rb)
- [NotaCSstudent](https://github.com/NotaCSstudent)

## Requirements

- To build the application, you run the following command to download the necessary packages 
    ```
    pip3 install Flask 
    pip3 install SpeechRecogntion
    pip3 install bs4
    install ngrok
    install ffmpeg
    create your own page access token 
    
    ```
    
## Deployment

- To run the application, run the following command:
    ```
    python3 main.py
    
    
    ```
    
## Commands
- Once the user says "looking for", our program will take all words until the end or the next stop word 
    and put it in our we scraper to pull those job listings from Indeed.com
