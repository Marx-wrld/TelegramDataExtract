## TelegramDataExtract

Extracting data from telegram using python.

#### Clone or Download the repo
- Create a ```.env``` file, where you'll paste your api_id, api_hash and phone number then add the following:- 
```
API_ID=
API_HASH=
PHONE_NUMBER=
````

- Create a ``` telegram_code.txt``` file then add the telegram code sent to your device. Edit the file like this, e.g - telegram_code=12345

- Also, create a ```telegram_output.txt``` file where the extracted data will be stored. 

**DISCLAIMER** 

>Ensure you don't leak both files to the public

#### Installations
```
python -m pip > requirements.txt

pip install virtualenv

pip install virtualenvwrapper-win

pip install telethon

pip install pandas

pip install dotenv
```
