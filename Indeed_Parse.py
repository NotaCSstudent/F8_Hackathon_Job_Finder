
import requests
from datetime import datetime
from bs4 import BeautifulSoup




def Get_Url(Job :str):
    Template = 'https://www.indeed.com/jobs?q={}&l=New+York%2C+NY'
    Url = Template.format(Job)
    return Url



def Find_Job(Job : str,Number_Of_Jobs :int):
    Job_Url = Get_Url(Job) ##For the Helper Function Above




    Job_Response = requests.get(Job_Url) ## Getting a Response from the URL
    Job_Soup = BeautifulSoup(Job_Response.text,"html.parser") ##Parses into an HTML Tree Structure
    
    
    Name_Of_Role = Job_Soup.find_all('div','jobsearch-SerpJobCard')##Role name tag

    Name_Finder = Name_Of_Role[Number_Of_Jobs]
    Name = Name_Finder.h2.a
    


    Company_Name = Job_Soup.find_all('span','company') ##Finds company html tag

    Company = Name_Finder.find('span','company').text.strip() ## Gets the company name and strips out anything thats not needed




    Company_Location = Name_Of_Role[Number_Of_Jobs] ##Starting at index 
    Location = Company_Location.find('div','recJobLoc').get('data-rc-loc')##gets the role
    
    Details = Name['title'] + "\n" + Company + "\n" + Location
    
    return (Details)


##print(len(Find_Job("Software Engineer")))



##First_Job = Find_Job("Software Engineer",1) 

  




#print(len(First_Job))
##print(First_Job[0])

#print(First_Job[0].h2)
#print(First_Job[0].h2.a)


#Tag = First_Job[0].h2.a
#print(Tag['title'])



def Find_My_Job(Insert_Job : str):
    for i in range(1,7):
        try:
            print(Find_Job(Insert_Job, i));
        except(IndexError):
            pass
        ##Use this to skip any Index Errors
       


##Find_My_Job("Software Engineer")
##Find_My_Job("Data Analyst")
##Find_My_Job("Janitor")
Find_My_Job("Tutor")