## TelegramDataExtract

Extracting data from telegram using python.

#### Getting your telegram api-id and hash

- Visit the official telegram website - http://my.telegram.org/

- Log in with your phone-number and confirmation code from telegram, to manage your apps using Telegram API or delete your account.

- On the telegram core sub-menu, click on API development tools and fill the required fields. Choose any name and random url for your app.

- After submitting, you will receive your api_id and api_hash

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

>Ensure you don't leak either files to the public

#### Installations

```
python -m pip > requirements.txt

pip install virtualenv

pip install virtualenvwrapper-win

pip install telethon

pip install pandas

pip install python-dotenv

```
