import os
from telethon.sync import TelegramClient

def read_telegram_code():
    telegram_code = None
    if os.path.isfile('telegram_code.txt'):
        with open('telegram_code.txt', 'r') as file:
            telegram_code = file.readline().strip()
    elif 'TELEGRAM_CODE' in os.environ:
        telegram_code = os.environ.get('TELEGRAM_CODE')
    return telegram_code

api_id = '22594962'
api_hash = '776fcc612e784a0c92fd74fabf4b1505'
phone_number = '+254740334255'
session_name = 'session_name'
telegram_code = read_telegram_code()


client = TelegramClient(session_name, api_id, api_hash)

# Connect to Telegram
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: ') if telegram_code is None else telegram_code)

# Get list of all dialogs (conversations)
dialogs = client.get_dialogs()

# Iterate over dialogs
for dialog in dialogs:
    # Check if it's a group or channel where you have posted
    if dialog.entity.username:
        # Retrieve all messages from the group or channel
        messages = client.get_messages(dialog.entity, limit=None)  # Set limit to None to retrieve all messages
        # Process messages as needed
        for message in messages:
            # Process each message (e.g., store in a data structure or write to a file)
            with open('telegram_output.txt', 'a', encoding='utf-8') as output_file:
                output_file.write(f"Group: {dialog.name}\n")
                output_file.write(f"Post: {message.text}\n")
                
                # Retrieve up to 1000 replies/comments for each message
                comments = client.get_messages(dialog.entity, ids=[message.id], limit=2000)
                
                # Process each comment
                for comment in comments:
                    output_file.write(f"Comment: {comment.text}\n")


# Disconnect from Telegram
client.disconnect()

