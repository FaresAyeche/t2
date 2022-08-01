from selenium import webdriver
import pytest
import time

def test_OpenBE():
        driver = webdriver.Chrome('C:/Users/fayeche/PycharmProjects/Testsel2/driver/chromedriver.exe')
        driver.get("https://www.talan-academy.com/")

