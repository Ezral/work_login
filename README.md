# work_login.py
------
This is a little project that I thought of after not being able to handle
the hassle of logging in and out of my company's website

To use:
1. Place the script in your ~/ folder.
2. If you don't have chromium webdriver yet, download from [here](https://chromedriver.chromium.org/downloads) and place it in your ~/ folder.
3. You also need to update the executable_path located in line 23, following the path of your chromium (chromedriver).
4. Packages that you will need to have: selenium, datetime, time, sys, os, threading and re.
5. Update the credentials in line 27 and 28 using your WebHR user and password.
6. If you want the headless to be turned off set options.headless in line 21 to False.
7. You will also need to adjust and make sure that the output path for the webdriver screenshot image in line 30 exists.
