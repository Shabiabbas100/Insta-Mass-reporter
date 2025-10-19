from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pyautogui
import argparse
import sys
import time

reportUser="silence10103"  # Target user(userid) , set it according to yourr target
defaultFile="loginCredentials.txt"   #this is the file where login credentials are saved ,replace with your own file name🙈


def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--userName", type = str, default = "", help = "Username to report.")
    parser.add_argument("-f", "--file", type = str, default =defaultFile, help = "Accounts list ( Defaults to acc.txt in program directory ).")
    options = parser.parse_args(args)
    return options


def reportNow():
    args = getOptions()
    print(args) 

    userName = args.userName
    sampleFile= args.file

    if userName == "" :
        userName = input("Enter your UserName: ")

    a = open(sampleFile, "r").readlines()
    print(a)
    file = [s.rstrip() for s in a] #removing whitespace
    file.reverse()  # so that new accounts are used first
    print(file)    # i wrote it for debugging purpose , so not necessary


    userID = []
    password = []
    for line in file:
        line = line.split(":")
        userID.append(line[0])
        password.append(line[1])

    print(userID)
    print(password)

    service = Service()  # this actually installs the latest chrome driver for connection

    for i in range(len(file)):
        driver = webdriver.Chrome(service=service) #driver is similiar to robot
        wait = WebDriverWait(driver, 15) #wait is better than sleep as wait is max but sleep is fixed , so wait is time efficient 
        driver.get("https://www.instagram.com/accounts/login/")   # go to login address
        time.sleep(2)
        username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        username_field.send_keys(userID[i])
        time.sleep(.5)
        username_password= wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        username_password.send_keys(password[i])
        time.sleep(.5)
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_btn.click()
        time.sleep(8)
        driver.get(f'https://www.instagram.com/{reportUser}')
        time.sleep(5)
        threeDot=wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']")))
        threeDot.click()
        time.sleep(2)
        reportButton=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Report']")))
        time.sleep(2)
        reportButton.click()
        time.sleep(2)
        reportAccount=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Report') and contains(., 'Account')]")))
        time.sleep(2)
        reportAccount.click()
        reason=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'content')]")))
        time.sleep(2)
        reason.click()
        reason2=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'like')]")))
        reason2.click()
        time.sleep(3)
        close=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']")))
        close.click()
        time.sleep(5)
        driver.get("https://www.instagram.com/")
        driver.quit()  # close the browser
    pyautogui.keyDown('ctrl')
    time.sleep(0.25)
    pyautogui.keyDown('w')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('w')
    time.sleep(2)

    
reportNow()  # calling the function




