
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

def find_last():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://www.exploit-db.com/search?q=wordpress')
    time.sleep(4)

    clicks1 = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/label/select')
    clicks1.send_keys("120")
    print('click')
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    last_ = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[9]/a').text
    time.sleep(4)

    print(last_)
    driver.quit()
    return last_

def crawl(url):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(url)
    contents = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/pre/code').text

    contents = contents.split("\n")
    extract_contents = []

    a= ''
    b= ''
    c= ''

    for i in contents:
        if 'Title:' in i:
            a = " ".join(i.split())
        if 'CVE:' in i:
            c = i
        if 'Vulnerable version:' in i:
            b = i
        if a == '':
            contents1 = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div[1]/div/div[1]/h1').text
            a = contents1
    
    extract_contents.append(a)
    extract_contents.append(b)
    extract_contents.append(c)

    print(extract_contents)
    driver.quit()
    return extract_contents

def take_links():

    global links
    last_ = find_last()
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://www.exploit-db.com/search?q=wordpress')
    time.sleep(3)

    clicks1 = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/label/select')
    clicks1.send_keys("120")
    time.sleep(3)

    print('1클릭')
    for i in range(2,int(last_)+2):
        print(i)
        time.sleep(1.5)
        contents = driver.find_elements_by_tag_name('a')
        for j in contents:
            if('https://www.exploit-db.com/exploits/' in j.get_attribute('href')):
                #print(i.get_attribute('href'))
                links.append(j.get_attribute('href'))
        print(len(links))
        print('----')
        if i == 2:
            print('2클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[4]')
            clicks.click()
        elif i == 3:
            print('3클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[5]')
            clicks.click()
        elif i == 4:
            print('4클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[6]')
            clicks.click()
        elif i == 5:
            print('5클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[7]')
            clicks.click()
        elif i == int(last_)-2:
            print( str(i) + '클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[7]')
            clicks.click()
        elif i == int(last_)-1:
            print( str(i) + '클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[8]')
            clicks.click()
        elif i == int(last_):
            print( str(i) + '클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[9]')
            clicks.click()
        elif i == int(last_)+1:
            break
        else :
            print( str(i) + '클릭')
            clicks = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[7]')
            clicks.click()
        time.sleep(3)

def save_links():
    global links

    f = open('listfile.csv', 'w', newline='')
    wr = csv.writer(f)

    for i in links:
        wr.writerow([i])


data = []
url = 'https://www.exploit-db.com/exploits/'
links = []

print("MODE")
print(" 초기 탐색 '1' ")
print(" 만들어진 리스트활용하기 '2' ")
mode = input()

if mode == '1':
    take_links()
    save_links()
    print(len(links))
else:
    f = open('listfile.csv','r')
    rdr = csv.reader(f)
    for i in rdr:
        links.append(i)

print(links[0])

f = open('data.csv', 'w', newline='')
wr = csv.writer(f)
for i in links:
    try:
        wr.writerow(crawl("".join(i)))
    except:
        pass


