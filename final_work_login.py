# Importing packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time, sys, threading, re, os

'''Place the script in your ~/ folder.
If you don't have chromium webdriver yet, download from https://chromedriver.chromium.org/downloads
and place it in your ~/ folder. The version needs to follow your Google Chrome app version.
You also need to update the executable_path located in line 23, following the path of your chromium (chromedriver).
Packages that you will be needing to run this script: selenium, datetime, time, sys, threading and re.
Update the credentials in line 27 and 28 using your WebHR user and password.
If you want the headless to be turned off set options.headless in line 21 to False.
You will also need to adjust and make sure that the output path for the webdriver screenshot image in line 30 exists.'''

# Set the headless option to True/False for webdriver
options = Options()
options.headless = True
# Executable path for webdriver
webdriver_path = '/Path/of/your/choice/chromedriver'
# URL for website
url = 'https://companywebsite.com'
# Credentials
user = 'email'
password = 'password'
# Path and file name for webdriver screenshot
now = datetime.now().strftime("%Y%m%d-%H%M")  # Define time str format
scrshot = "/Path/of/your/choice/hr_screenshot_{}.png".format(now)
# Dictionaries
btnDict = {
'1':'btnAttendanceSignIn' , '2':'btnAttendanceBreakOut',
'3':'btnAttendanceBreakIn', '4':'btnAttendanceLunchOut',
'5':'btnAttendanceLunchIn', '6':'btnAttendanceSignOut'
}
outDict = {
'1':'Signed in to WebHR', '2':'Out for break',
'3':'Returned from break', '4':'Out for lunch',
'5':'Returned from lunch', '6':'Signed out from WebHR'
}
errDict = {
'1':'signed in to WebHR', '2':'taken your break',
'3':'returned from break', '4':'taken your lunch break',
'5':'returned from lunch', '6':'signed out from WebHR'
}
# User selection for WebHR status option
print("\nDocDoc WebHR status option:")
answer = input("\t1 For signing in\n\t2 For going to break\n\t3 For returning from break\n\t4 For going to lunch\n\t5 For returning from lunch\n\t6 For signing out\n\nInput your selection: ")
# Restricting answer and error message
if not re.match("[1-6]", answer):
    print("\n"+"Error: Only numbers 1 to 6 allowed!")
    sys.exit()
# Assigning the dictionary value that will be used to variables
btnClick = btnDict[answer]
message=outDict[answer]
error=errDict[answer]
# Running the webdriver
driver = webdriver.Chrome(options=options, executable_path = webdriver_path)
# Function to login to webhr
def webhr_login():
    driver.get(url)
    driver.find_element_by_id('u').send_keys(user)      # id='u' for the user field
    driver.find_element_by_id('p').send_keys(password)  # id='p' for the password field
    driver.find_element_by_id('btnLogin').click()       # id='btnLogin' for the login button
    time.sleep(3)                                       # 3s sleep to let webhr page load
# Defining the animation
def animated_loading():
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r'+'Loading '+char+' ')
        time.sleep(.1)
        sys.stdout.flush()
# Defining the thread
the_process = threading.Thread(name='process', target=webhr_login)
the_process.start()
# Running the animation while thread is alive
while the_process.isAlive():
    animated_loading()
# Clear the loading animation line once threading is finished
sys.stdout.write('\r'+'     '+'     ')
# 2s timeout to allow webpage to load
time.sleep(2)
# Function to execute button clicking
def execute():
    try:
        elem = driver.find_element_by_id(btnClick)
        if elem.is_displayed() and elem.is_enabled():   # Check that the element is displayed and clickable
            print('\n'+"Success: {}".format(message))   # Print message text str in terminal
            elem.click()                                # Click the element
    except NoSuchElementException:                      # In the event that element is not found
        print('\n'+"You have {} today.".format(error))  # Print error text str in terminal

# Executing function
try:
    if driver.find_element_by_id('btnAttendanceSignIn').is_displayed() and btnClick != 'btnAttendanceSignIn':
        print("\n"+"Error: You haven't signed in!")
        os._exit
    else:
        execute()
except:
    execute()

driver.get_screenshot_as_file(scrshot)      # Taking screenshot from webdriver
driver.quit()                               # Close webdriver
