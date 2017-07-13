# -*- coding: utf-8 -*-
import os
import re
import urlparse
import urllib
import urllib2
from bs4 import BeautifulSoup

URL_PWD = "https://laod.cn/hosts/2017-google-hosts.html"
URL_HOST = "https://iiio.io/download/"

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getLatestDate(url):
    nums = tuple("0 1 2 3 4 5 6 7 8 9".split())
    html = getHtml(url)
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    days = "0"
    for link in links:
        href = link.attrs["href"]
        if href.startswith(nums) and href > days:
            days = href
    if days is not "0":
        return urlparse.urljoin(url, days)
    else:
        return url


def schedule(a, b, c):
    per = 100.0 *a * b
    if per > 100:
        per = 100
        print "%.2f%%" % per


def download(url, dest):
    try:
        # urllib.urlretrieve(url, dest, schedule)
        urllib.urlretrieve(url, dest)
    except Exception as e:
        print e
        print "error to download file: " + url

def getHostFile(url):
    html = getHtml(url)
    soup = BeautifulSoup(html, "html.parser")
    file_link = ""
    for link in soup.find_all("a"):
        if "dows" in link.contents[0].string:
            if u"系列" in link.contents[0].string:
                file_link = link.attrs["href"]
                break
    local = "./"
    # local = os.path.join("./", "Downloads")
    # local = os.path.abspath(local)
    # if not os.path.exists(local):
    #     os.mkdir(local)
    local = os.path.join(local, "host.zip")
    file_link = urlparse.urljoin(url, file_link)
    download(file_link, local)

def getPassword(url):
    html = getHtml(url)
    soup = BeautifulSoup(html, "html.parser")
    pwd_regexp = re.compile(u".+密码：(.+)$")
    pwd = soup.find(text=pwd_regexp)
    if pwd:
        pwd = pwd.string
        pwd = pwd_regexp.search(pwd).group(1)
        return pwd
    else:
        raise Exception(u"未查找到密码")

url_date = getLatestDate(URL_HOST)
getHostFile(url_date)
print getPassword(URL_PWD)

