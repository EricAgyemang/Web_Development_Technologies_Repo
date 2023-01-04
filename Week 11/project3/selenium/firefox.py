from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
browser.get("https://www.linkedin.com/in/eric-agyemang/")
