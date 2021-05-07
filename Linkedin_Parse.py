import urllib.request
import bs4 as bs


Job_Finder = urllib.request.urlopen('https://www.indeed.com/jobs?q=software+engineer&l=New+York%2C+NY')

Job_Soup = bs.BeautifulSoup(Job_Finder,'xml')

#print(Job_Soup)