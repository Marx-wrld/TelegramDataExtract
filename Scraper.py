from telethon.sync import TelegramClient

api_id = '22594962'
api_hash = '776fcc612e784a0c92fd74fabf4b1505'
phone_number = '+254740334255'

client = TelegramClient('session_name', api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

group_entity = 'Tech Space KE'  # This can be the group username or chat ID

group_info = client.get_entity(group_entity)

messages = client.get_messages(group_info, limit=10)  # Limiting to 10 messages for example

for message in messages:
    print(f"Post: {message.text}")
    comments = client.get_messages(message.to_id, ids=[message.id], replies=100)  # Retrieve up to 100 replies/comments
    for comment in comments:
        print(f"Comment: {comment.text}")

client.disconnect()
