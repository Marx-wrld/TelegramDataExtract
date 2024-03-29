import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

def read_telegram_code():
    telegram_code = None
    if os.path.isfile('telegram_code.txt'):
        with open('telegram_code.txt', 'r') as file:
            telegram_code = file.readline().strip()
    elif 'TELEGRAM_CODE' in os.environ:
        telegram_code = os.environ.get('TELEGRAM_CODE')
    return telegram_code

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
phone_number = os.environ.get('PHONE_NUMBER')
session_name = 'session_name'
telegram_code = read_telegram_code()


client = TelegramClient(session_name, api_id, api_hash)

# Connecting to Telegram
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: ') if telegram_code is None else telegram_code)

# Getting the list of all dialogs (conversations)
dialogs = client.get_dialogs()

# Iterating over dialogs
for dialog in dialogs:
    # Checking if it's a group or channel where you have posted
    if dialog.entity.username:
        # Retrieving all messages from the group or channel
        messages = client.get_messages(dialog.entity, limit=None)  # Setting limit to None to retrieve all messages
        # Processing messages as needed
        for message in messages:
            with open('telegram_output.txt', 'a', encoding='utf-8') as output_file:
                output_file.write(f"Group: {dialog.name}\n")
                output_file.write(f"Post: {message.text}\n")
                
                # Retrieving up to 1000 replies/comments for each message
                comments = client.get_messages(dialog.entity, ids=[message.id], limit=5000)
                
                # Processing each comment
                for comment in comments:
                    output_file.write(f"Comment: {comment.text}\n")


# Disconnecting from Telegram
client.disconnect()