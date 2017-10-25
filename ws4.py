import requests
from bs4 import BeautifulSoup as bs
import json
from selenium import webdriver
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 


class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 




def getsim(w1, w2):
	url = r"http://ws4jdemo.appspot.com/?mode=w&s1=&w1="+w1+"%23n%231&s2=&w2="+w2+"%23n%231"
	# browser = webdriver.PhantomJS()
	# browser.get(url)
	x = Render(url)
	r = x.frame.toHtml()
	soup = bs(r, "html5lib")
	print(soup)
	# s = soup.find("span", attrs={"class": "synset"})
	# print(s.text)

getsim("employee", "car")