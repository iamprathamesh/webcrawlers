import bs4 as bs
from selenium import webdriver
import datetime
import time

driver = webdriver.Firefox()
url = 'http://tipz.mobi/nse/gainerp.php'
while True:
    driver.get(url)
    html = driver.execute_script('return document.documentElement.outerHTML')

    soup = bs.BeautifulSoup(html, 'html.parser')

    div = soup.find_all('div', class_='f_left meta')

    currentTime = datetime.datetime.now()

    fileName = currentTime.strftime("%j")

    file = open(fileName+'.txt', 'w')
    space = '\t'
    for ele in range(2, 12):
        name = div[ele].find('div', class_='f_left').text
        data = div[ele].find('div', class_='f_right').text
        file.write(str(name) + str(data.replace("\t","").replace("\n","").replace("\xc2","").replace("\xa0","").encode('utf-8')) + '\n')

    file.close()
    time.sleep(43200)

