# Test Automation using PyTest


## Pre-steps

#### 1. Copy project folder to your local machine

#### 2. Open IDE and install required modules

#### 3. Restore "AdventureWorks2012" database to MSSQL Server

#### 4. Connect to MSSQL Server
Test automation process requires connection with MSSQL Server to perform autotests.

Go to **../settings/db_conn.py** to set up variables to work with Database locally.

To create a new user visit [this link](https://www.tutorialspoint.com/ms_sql_server/ms_sql_server_create_users.htm).

## Launch autotests

Open **../tests.py** in IDE and use a command in terminal:
```
pytest -v -s tests.py
```
Autotests were created to replace manual testing activities for test cases presented in git root folder.

## Tests results
###### Allure report tool is used to generate test reports for this project. Read [information](https://docs.qameta.io/allure-report/#_installing_a_commandline) about installation process.

To generate reports in json format run in IDE the following command:
```
pytest -v -s --alluredir="allure-reports" tests.py
```
Than copy the path to Allure **bin** repository and run a command in CLI:
```
allure serve <path to the allure bin directory>
```
See example of tests report **../PyTest_report_example1.PNG**

and **../PyTest_report_example2.PNG**
