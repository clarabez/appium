**Automation project for Yahnac application (Login page)**

This project aims to automate the login flow for Yahnac apk. This project may be found here: https://github.com/malmstein/yahnac

___

**Project structure:**

I am using Pytest strutucture for this project. So, here is an overview for my project:

```
HackerNews/
  pages/
      locators/
          login_locators.py
      base.py
      home.py
      login.py
  setup/
      DeviceId.py
      apks/
          Apk.File
  tests/
      test_yahnac.py
  utils/
      constants.py
```

🗂 **Brief explanation for each folder:**

Pages >> PageObjects related, a .py file for each folder and its functionalities as well.

Setup >> Here we indicate apks to be used and also the the serial number of the device under test (DeviceId.py).

Tests >> Test flow for the execution.

Utils >> Utilities for the project, like constants.
___

**Resources**

🎯  I am using here:

Python<br>
Pytest<br>
Appium-Python-Client<br>
Selenium<br>
(and some complements)<br>

🛠 How to install it?

Just run requirements.txt file by using following command on root path:

```
pip install -r requirements
```
___

💻  **Test environment setup**

Application folder and serial number for Android product are registered on /setup folder. 
Just insert your serial number (adb devices) on DeviceId.py.

After that, indicate 

To run the project, just call pytest on terminal:

```
pytest
```
___

📝  **Report execution**

To perform execution and also generate a report for that, just use following command when calling pytest:

```
pytest --html=report.html  
```

After execution, a file called "report.html" will be generated on root path of the project. Click on it, and it will be opened as a text file. Execute it indicating a browser to render html file. Report will be displayed.

Also, a link will be displayed after execution, so you may access it directly from that.

___

 🌱 **What would I improve in this project?**
 
We are never satisfied about our final solutions and every project would be better in several details. Here are some points that I know would be improved in better conditions for this project(more time to investigate, etc):

- Avoid using Xpath to identify elements: xpath are sensible variables to identify an element on project. As login page is a webview, I had some dificulties to make appium identifies the element to click on it. My solution was using xpath and not ID.
- Make find_element() method more applicable: as some elements are not using same structure to be identified on screen (some with ID, some others with xpath) I used find_method() solution only for native activities. So, on login.py file I used the same structure repeatedly for differents elements. A good solution would be another method to identify only those cases.
- Using more resources from pytest: pytest has a lot of resources to help automation run softly. Would be great to use pytest-incremental to avoid some test to be runned if a "root test" failed, for example. Parametrize the kind of execution (sanity, regression, etc) would also be good.

___

🎬 **Video for the execution**

I also recorded a video for this execution, find it here in this link:
https://drive.google.com/drive/folders/1a_4JJaG1Op6vEanliKcN13RbXKD0r_9C?usp=sharing
