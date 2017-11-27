# -* coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import  os


# get source from web
def requestSite():
    siteurl = "https://elt.oup.com/student/openforum/2?cc=us&selLanguage=en"
    req = urllib.request.Request(siteurl)
    sitepage = urllib.request.urlopen(req)
    global html
    html = sitepage.read()

#get download url from source
def getData():
    soup = BeautifulSoup(html,'html.parser')
    #url list
    global downloadUrl
    downloadUrl = []
    #iteration url and find all <a> tag
    for urldata in  soup.find_all('a'):
        #cut out special url start by '/elt/students/openforum'
        if '/elt/students/openforum' in urldata['href']:
            downloadUrl.append('https://elt.oup.com'+ urldata['href'])


def download():
    #create store folder
    if not os.path.exists('openforum'):
        os.mkdir('openforum')
    #cd folder
    os.chdir('openforum')

    #start download file with url
    for link in downloadUrl:
        fileName = link.split('/')[-1].split('?')[0]
        print("Downloading: " + fileName)
        urllib.request.urlretrieve(link,fileName)
        print(fileName + ' Downloaded!')


if __name__ == '__main__':
    requestSite()
    getData()
    download()
    print("===========================")
    print('Download Completed!')



