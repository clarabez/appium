### Introduction

This is the automation project for [Verivox](https://play.google.com/store/apps/details?id=de.verivox.contractmanager&hl=pt_BR&gl=US) mobile application.

<b>Project structure:</b>

I am using Pytest strutucture for this project. So, here is an overview for my project:

````
verivox/
  pages/
      locators/
          general_locators.py
      base.py
      tarife.py
      vergleich.py
  setup/
      verivox.apk
  tests/
      test_verivox.py
  conftest.py
  README.md
  requirements.txt
````

🗂 <b>Brief explanation for each folder:</b>

Pages >> PageObjects design pattern related, a .py file for each folder and its functionalities as well.

Setup >> Here we indicate apks to be used and also the the serial number of the device under test (DeviceId.py).

Tests >> Test flow for the execution.

Conftest >> Pytest file for all needed configurations.

README.md >> About the project and instructions of how to run it.

requirements.txt >> All the necessary resources to run this project.



🎯 <b>I am using following resources here:</b>

- Python
- Pytest
- Appium-Python-Client
(and some complements)

🛠 <b> How to install them? </b>

Just run requirements.txt file by using following command on root path:

```
pip install -r requirements.txt
```


📝 <b>Report execution </b>

To perform execution and also generate a report for that, just use following command when calling pytest:

````
pytest --html=report.html  
````

After execution, a file called "report.html" will be generated on root path of the project. Click on it, and it will be opened as a text file. Execute it indicating a browser to render html file. Report will be displayed.

Also, a link will be displayed after execution, so you may access it directly from that.

### Scenarios to be tested

<u>Scenario 1: Verify the DSL calculator</u>

<b>GIVEN</b> that I can open the app Home screen<br>
<b>WHEN</b> I select the DSL calculator<br>
<b>AND</b> I enter "030" for my area code<br>
<b>AND</b> I select the "100 Mbit/s" bandwidth option<br>
<b>AND</b> I click the "Jetzt vergleichen" button<br>
<b>THEN</b> I should see a list of available tariffs based on my selection<br>

<u>Scenario 2: Load multiple tariff results</u>

<b>GIVEN</b> the same tariff calculation criteria from scenario 1<br>
<b>WHEN</b> I see the tariff search results screen<br>
<b>THEN</b> I should see the total number of available tariffs listed in the Ermittelte Tarife section<br>
<b>WHEN</b> I scroll to the end of the search results<br>
<b>THEN</b> I should see only the first 20 tariffs displayed<br>
<b>WHEN</b> I click on the button labeled "20 weitere Tarife laden"<br>
<b>THEN</b> I should see the next 20 tariffs displayed<br>
<b>AND</b> I can continue to load any additional tariffs until all tariffs have been displayed<br>

<u>Scenario 3: Load multiple tariff results</u>

<b>GIVEN</b> the same tariff calculation criteria from scenario 1<br>
<b>AND</b> I see the tariff search results screen<br>
<b>WHEN</b> I click on any "Zum Angebot" button to select a tariff offer<br>
<b>THEN</b> I should see the corresponding tariff offer screen for the selected tariff<br>

### Test Environment information

<b>Application version:</b><br>
3.3.1

<b>Information about device under test:</b><br>
Emulated device from Android Studio.<br>
Model: Google Pixel 3. <br>
Android version: 9<br>

<b>IDE for test development: </b><br>
Pycharm